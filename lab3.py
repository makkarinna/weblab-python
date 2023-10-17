from flask import Blueprint, render_template, request
lab3 = Blueprint('lab3', __name__)


@lab3.route('/lab3/')
def lab():
    return render_template('lab3.html')


@lab3.route('/lab3/form1')
def form1():
    errors = {}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните поле!'

    errors1 = {}
    age = request.args.get('age')
    if age == '':
        errors1['age'] = 'Заполните поле!'

    sex = request.args.get('sex')
    return render_template('form1.html', user=user, age=age, sex=sex, errors=errors, errors1=errors1)

@lab3.route('/lab3/order')
def order():
    return render_template('order.html')


@lab3.route('/lab3/pay')
def pay():
    price = 0
    drink = request.args.get('drink')
    if drink == 'coffee': 
        price = 120
    elif drink == 'black-tea':
        price = 80
    else:
        price = 70

    if request.args.get('milk') == 'on':
        price += 30
    if request.args.get('sugar') == 'on':
        price += 10

    return render_template('pay.html', price=price)

@lab3.route('/lab3/success')
def succsess():
    return render_template('success.html')


@lab3.route('/lab3/ticket')
def ticket():
    errors2 = {}
    name1 = request.args.get('name1')
    if name1 == '':
        errors2['name1'] = 'Заполните поле!'

    errors3 = {}
    age1 = request.args.get('age1')
    if age1 == '':
        errors3['age1'] = 'Заполните поле!'
    
    errors4 = {}
    fam1 = request.args.get('fam1')
    if fam1 == '':
        errors4['fam1'] = 'Заполните поле!'

    errors5 = {}
    otc1 = request.args.get('otc1')
    if otc1 == '':
        errors5['otc1'] = 'Заполните поле!'

    errors6 = {}
    punktnaz = request.args.get('punktnaz')
    if punktnaz == '':
        errors6['punktnaz'] = 'Заполните поле!'

    errors7 = {}
    punktv = request.args.get('punktv')
    if punktv == '':
        errors7['punktv'] = 'Заполните поле!'

    errors8 = {}
    data1 = request.args.get('data1')
    if data1 == '':
        errors8['data1'] = 'Заполните поле!'

    type1= request.args.get('type1')
    bag = request.args.get('bag')

    polk = ''
    polk = request.args.get('polk')
    if polk == 'niz':
        polk = 'Нижняя'
    elif polk == 'niz-bok': 
        polk = 'Нижняя боковая' 
    elif polk == 'verh': 
        polk = 'Верхняя' 
    else: 
        polk= 'Верхняя боковая' 

    
    return render_template('ticket.html', name1=name1, fam1=fam1, age1=age1, otc1=otc1, type1=type1, bag=bag, punktv=punktv, punktnaz=punktnaz, data1=data1, polk=polk,  errors2=errors2,
                           errors3=errors3, errors4=errors4, errors5=errors5, errors6=errors6, errors7=errors7, errors8=errors8)



@lab3.route('/lab3/success2')
def succsess2():
    return render_template('success2.html')