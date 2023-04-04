from flask import Flask, render_template, request
from product import Product
from user import User
from saper import field
import json
app = Flask("Grocery")

@app.route('/')
def about():
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

    # spisok = [Product("https://www.meme-arsenal.com/memes/5ba73d1f4ff36b59825c28574db0de4b.jpg", 
    #                                                           "удивленный котик", "50 рублей"),
    #                                                   Product("http://memchik.ru/images/mems/5d94977f21248.jpg",
    #                                                           "котик дебошЫр", "200 уе в час"),
    #                                                   Product("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS8vD0_zkG3Fnn45L49ZwlODXgPtRxwaRHxwA&usqp=CAU",
    #                                                           "милаха", "бесценен"),
    #                                                   Product("https://img-fotki.yandex.ru/get/4407/79015228.136/0_9d230_33ef3c68_XL.jpg",
    #                                                           "котик наркоман", "отдадим бесплатно в хороше руки")]
    # products = {}

    # for product in spisok:
    #     products[product.name] = {}
    #     products[product.name]["photo"] = product.link
    #     products[product.name]["price"] = product.price

    # print(products)
    # with open("products.json", "w") as file:
    #     json.dump(products, file)

    with open("products.json", "r") as file:
        temp = json.load(file)
    if request.form['name'] != "" and request.form['link'] != "" and request.form['price'] != "":
        temp[request.form['name']] = {"photo": request.form['link'], "price": request.form['price']}
        with open("products.json", "w") as file:
            json.dump(temp, file, indent=3)
    return render_template("products.html")


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

@app.route('/saper_post')
def saper_post():
    return render_template ("saper_post.html")
    



@app.route('/saper/<height>_<width>_<bombs>')
@app.route('/saper', methods=["POST"])
def saper(height = 8, width = 8, bombs = 10):
    print(request.form['height'])
    try:
        if int(request.form['height']) <= 0 or int(request.form['width']) <= 0 or int(request.form['bombs']) <= 0:
            raise ValueError("Все параметры должны быть положительными")
        if int(request.form['bombs']) > int(request.form['height']) * int(request.form['width']):
            raise ValueError("Количество бомб не должно быть больше чем количество клеток")
    except ValueError as e:
        print("Ошибка:", e)
        return render_template("saper_post.html")
    except TypeError as e:
        print("Ошибка:", e)
        return render_template("saper_post.html")
    return render_template("saper.html", game_field = field(int(request.form['height']), int(request.form['width']), int(request.form['bombs'])))

app.run(debug=True)





# Реализовать сайт c продуктами, должны присутствовать страницы:

# - О сайте
# - Товаров (Название, Цена, Картинка)
# - Профиль владельца (Имя, Возраст, Фото)
