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


    

