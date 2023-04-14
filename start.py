from flask import Flask, render_template, request
from product import Product
from user import User
import json
app = Flask("Grocery")

@app.route('/register')
def register():
    return render_template("login.html")

@app.route('/')
@app.route('/', methods=["POST"])
def about():
    
    with open("logins.json", "r") as file:
        temp = json.load(file)
        
    if 'login' in request.form and request.form['login'] != "" and \
        'password' in request.form and request.form['password'] != "":
        temp[request.form['login']] = request.form['password']
        
        with open("logins.json", "w") as file:
            json.dump(temp, file, indent=3)
                    
    return render_template("about.html")


@app.route('/owner/<name>_<descr>')
@app.route('/profile')
@app.route('/owner')    
def owner(name = "Пират Робертс", descr = """Ужасный Пират Робертс (Dread Pirate Roberts) настолько озабочен своей безопасностью, что не доверяет интернет-мессенджерам.<p>
Забудьте о телефоне и Skype. Всего один раз за 8 месяцев переговоров об интервью я предложил ему встретиться в любом месте за пределами США.<p>
«Исключено, – отрезал Робертс. – Я не встречаюсь даже со своими ближайшими помощниками».<p>
Когда я задал вопрос о его настоящем имени и национальности, он отказался отвечать и на месяц прекратил общение."""):
    user = User("https://cs8.pikabu.ru/post_img/big/2017/10/19/10/1508435537126155184.jpg", name, descr)
    return render_template("owner.html", link = user.link, name= user.name, descr = user.descr)


@app.route('/add_product')
def add_product():
    return render_template("add_product.html")


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



@app.route('/user/<user>')
def user_page(user):
    return f"Hello i am {user}"

@app.route('/odd_or_even/<number>')
def odd_or_even(number):
    return f"number {number} is even" if int(number) % 2 == 0 else f"number {number} is odd"



@app.route('/fio/<name>_<father>_<surname>')
def fio(name, father, surname):
    return f"""
Имя {name}<p>
Отчество {father}<p>
Фамилия {surname}
"""

app.run(debug=True)




