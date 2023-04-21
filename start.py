from flask import Flask, render_template, request, redirect, url_for
from product import Product
from user import User
import json
app = Flask("Grocery")

@app.route('/')
def home_page():
    return render_template("index.html")

@app.route("/owner")
@app.route("/owner/<login>/<password>")
def owner_page(login = None, password = None):
    with open("cookies.json", "r") as file:
        temp = json.load(file) 
    if login == None or password == None:
        if len(temp) == 0:
            return redirect(url_for("login"))
    
        login = temp['name']
        password = temp['password']
    
    return render_template("owner.html", login = login, password = password)

@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/register_validation', methods=["POST"])
def about():
    with open("logins.json", "r") as file:
        temp = json.load(file)

    if 'login' in request.form and request.form['login'] != "" and \
        'password' in request.form and request.form['password'] != "": 
        if request.form['login'] not in temp:
            temp[request.form['login']] = request.form['password']
        else:
            return render_template("error_notification.html", error = "Извините, указанный email уже существует.")
        with open("logins.json", "w") as file:
            json.dump(temp, file, indent=3)
            
        temp = {}
        temp["name"] = request.form['login']
        temp["password"] = request.form['password']
        with open("cookies.json", "w") as file:
            json.dump(temp, file, indent=3)
            
    else:
        return render_template("error_notification.html", error = "Имя или пароль пустые")
        
    return redirect(url_for("home_page"))

@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/login_validation', methods=["POST"])
def home():
    with open("logins.json", "r") as file:
        temp = json.load(file)
    if 'login' in request.form and request.form['login'] != "" and \
        'password' in request.form and request.form['password'] != "": 
        if request.form['login'] not in temp or temp[request.form['login']] != request.form['password']:
            return render_template("error_notification.html", error = "Имя или пароль неверные.")
        temp = {}
        temp["name"] = request.form['login']
        temp["password"] = request.form['password']
        with open("cookies.json", "w") as file:
            json.dump(temp, file, indent=3)
    else:
        return render_template("error_notification.html", error = "Имя или пароль пустые") 
    
    return redirect(url_for("owner_page", login = request.form['login'], password = request.form['password']))


@app.route('/add_product')
def add_product():
    return render_template("add_product.html")

@app.route('/log_out')
@app.route('/log_out', methods=["POST"])
def exit():
    temp = {}
    with open("cookies.json", "w") as file:
        json.dump(temp, file, indent=3)
    return redirect(url_for("login"))
        
@app.route('/products')
@app.route('/products', methods=["POST"])
def products():
    with open("products.json", "r") as file:
        temp = json.load(file)

    if len(request.get_data()) != 0:
        if 'name' in request.form and request.form['name'] != "" and \
            'link' in request.form and request.form['link'] != "" and \
            'price' in request.form and request.form['price'] != "":
            temp[request.form['name']] = {"photo": request.form['link'], "price": request.form['price']}
            with open("products.json", "w") as file:
                json.dump(temp, file, indent=3)
        elif 'delete_name' in request.form and request.form['delete_name'] != "" :
            if request.form['delete_name'] in temp.keys():
                temp.pop(request.form['delete_name'])
                print(request.form['delete_name'])
                with open("products.json", "w") as file:
                    json.dump(temp, file, indent=3)

    spisok = []
    for name in temp:
        spisok.append(Product(temp[name]['photo'], name, temp[name]['price']))
    return render_template("products.html", spisok=spisok)





app.run(debug=True)




