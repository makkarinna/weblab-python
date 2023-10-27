from flask import Blueprint, render_template, request, session, redirect, url_for
lab4 = Blueprint('lab4', __name__)


@lab4.route('/lab4/')
def lab():
    return render_template('lab4.html')


@lab4.route('/lab4/login/', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
        
    username = request.form.get('username')
    password = request.form.get('password')
    if username == 'alex' and password == '123':
        return render_template('success1.html', username=username)
    
    
    error1 = ''
    if username == '':
        error1 = 'Введите логин!'

    if 'username' == session:
        render_template(username=username)
        
    if 'password' == session:
        render_template(password=password)

    error2 = ''
    if password == '':
        error2 = 'Введите пароль!'
    
   
    error = 'Неверные логин и/или пароль!'
    return render_template('login.html', error=error, error1=error1, error2=error2, username=username, password=password)


@lab4.route('/lab4/ice', methods=['GET', 'POST'])
def ice():
    if request.method == 'GET':
        return render_template("ice.html")
    
    temperature = request.form.get('temperature')
    if  not temperature:
        result = 'ошибка: не задана температура!'
    elif int(temperature) < -12:
        result = 'не удалось установить температуру — слишком низкое значение'
    elif int(temperature) > -1:
        result = 'не удалось установить температуру — слишком высокое значение'
    elif int(temperature) > -12 and int(temperature) < -9:
        result = f"Установлена температура: {temperature}°C ***"
    elif int(temperature) >= -8 and int(temperature) <= -5:
        result = f"Установлена температура: {temperature}°C **"
    elif int(temperature) >= -4 and int(temperature) <= -1:
        result = f"Установлена температура: {temperature}°C *"

    return render_template("ice.html", result=result)



@lab4.route('/lab4/zerno')
def zerno():
    if request.method == 'GET':
        return render_template("zerno.html")
    
    return render_template('zerno.html')


@lab4.route('/lab4/pay1', methods=['GET', 'POST'])
def pay():
    if request.method == 'GET':
        return render_template("pay1.html")
    
    zerno = request.form.get('zerno')
    if zerno == 'yach':
        zer = 'Ячмень'
    elif zerno == 'ov': 
        zer = 'Овес' 
    elif zerno == 'pchen': 
        zer = 'Пшеница' 
    else: 
        zer= 'Рожь' 

    price = 0
    zerno = request.form.get('zerno')
    if zerno == 'yach': 
        price = 12000
    elif zerno == 'ov':
        price = 8500
    elif zerno == 'pchen':
        price = 8700
    else:
        price = 14000
    
    ves = int(request.form.get('ves'))

    if ves > 50:
        total_price = (ves * price) - (((ves * price) // 100) * 10)
        idk = 'Поздравляем! Применена скидка 10% за большой объем.'
    else:
        total_price = ves * price
        idk = ''

    if ves > 500:
        total_price = 'Ошибка!'
        idk = 'Такого объема сейчас нет в наличии!'

    if ves <= 0:
        total_price = 'Ошибка!'
        idk = 'Неверное значение веса'

        
    return render_template('pay1.html', zerno=zerno, price=price, zer=zer, ves=ves, total_price=total_price, idk=idk)
 
    
  






    


