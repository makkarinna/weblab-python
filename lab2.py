from flask import Blueprint, redirect, url_for, render_template
lab2 = Blueprint('lab2', __name__)


@lab2.route('/lab2/example')
def example():
    name = 'Махмад Карина'
    number = '2'
    number_kurs = '3 курс'
    number_group = 'ФБИ-14'
    fruits = [ 
        {'name': 'личи', 'price': 500},
        {'name': 'манго', 'price': 321}, 
        {'name':'банан', 'price': 60},
        {'name':'кокос', 'price':350},
        {'name':'авокадо', 'price': 200}
    ]
    books = [
        {'autor': 'Клуб романтики', 'name': 'Секрет небес. Яблоко Раздора', 'zhanr': 'Новеллизации', 'str': 320},
        {'autor': 'Владимир Сурдин', 'name': 'Темная сторона Вселенной', 'zhanr': 'Естественные науки', 'str': 368},
        {'autor': 'Габор Матэ', 'name': 'Когда тело говорит "нет". Цена скрытого стресса', 'zhanr': 'Красота и здоровье', 'str': 496},
        {'autor': 'Темми Хаф', 'name': 'Идеальный союз', 'zhanr': 'Современная зарубежная проза', 'str': 320},
        {'autor': 'Жорж Вигарелло', 'name': 'Искусство привлекательности. История телесной красоты от Ренессанса до наших дней', 'zhanr': 'Красота. Мода. Стиль. Этикет', 'str': 400},
        {'autor': 'Джейн Остен', 'name': 'Гордость и предубеждение', 'zhanr': 'Романтическая проза', 'str': 464},
        {'autor': 'Юлия Дростен', 'name': 'Когда тело говорит "нет". Цена скрытого стресса', 'zhanr': 'Красота и здоровье', 'str': 496},
        {'autor': 'Евгения Лёзина', 'name': 'Венская рапсодия', 'zhanr': 'Современная зарубежная проза', 'str': 384},
        {'autor': 'Габор Матэ', 'name': 'ХX век. Проработка прошлого', 'zhanr': 'Социология. Обществознание', 'str': 584},
        {'autor': 'Артур Дойл', 'name': 'Затерянный мир', 'zhanr': 'Детская художественная литература', 'str': 224}
    ]
    return render_template('example.html', 
                           name=name, number=number, number_kurs=number_kurs, 
                           number_group=number_group, fruits=fruits, books=books)


@lab2.route('/lab2/')
def labb():
    return render_template('lab2.html')


@lab2.route('/lab2/old_money')
def old():
    return render_template('old_money.html')



    
