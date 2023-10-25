from flask import Blueprint, render_template, request, session
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

    if 'username' is session:
        render_template(username=username)
        
    if 'password' is session:
        render_template(password=password)

    error2 = ''
    if password == '':
        error2 = 'Введите пароль!'
    
   
    error = 'Неверные логин и/или пароль!'
    
    return render_template('login.html', error=error, error1=error1, error2=error2, username=username, password=password)



    

