from flask import Blueprint, redirect, url_for, render_template, Blueprint, request, session
from db import db

from db.models import users, articles
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, current_user, logout_user

lab6 = Blueprint('laba6', __name__)

@lab6.route('/lab6/check')
def main():
    my_users = users.query.all()
    print(my_users)
    return 'console'

@lab6.route('/lab6/checkarticles')
def checkarticles():
    my_articles = articles.query.all()
    print(my_articles)
    return 'console'

@lab6.route('/lab6/registr', methods=["GET", "POST"])
def registrPage():
    errors = []

    if request.method == "GET":
        return render_template('registr6.html', errors=errors)
     
    username_form = request.form.get("username")
    password_form = request.form.get("password")

    
    hashPassword = generate_password_hash(password_form, method='pbkdf2')

    isUserExist = users.query.filter_by(username=username_form).first()
    if isUserExist is not None:
        errors.append("Пользователь уже существует")
        return render_template('registr6.html', errors=errors)
    
    if username_form is None or password_form is None or username_form.strip() == '' or password_form.strip() == '':
        errors.append("Пожалуйста, заполните все поля")
        print(errors)
        return render_template('registr6.html', errors=errors)
    if len(password_form) < 5:
            errors.append("Пароль должен содержать не менее 5 символов")
            print(errors)
            return render_template('registr6.html', errors=errors)

    

    newUser = users(username=username_form, password=hashPassword)

    db.session.add(newUser)
    db.session.commit()

    return redirect('/lab6/login')


@lab6.route('/lab6/login', methods = ['GET', 'POST'])
def login():
    errors = []
    if request.method == 'GET':
        return render_template('login6.html')

    username_form = request.form.get('username')
    password_form = request.form.get('password')

    my_user = users.query.filter_by(username=username_form).first()

    if my_user is not None:
        if check_password_hash(my_user.password, password_form):
            login_user(my_user, remember = False)
            return redirect('/lab6/glav')
        else: 
            errors.append("Неправильный пароль")
            return render_template('login6.html', errors=errors)
        
    if not (username_form or password_form):
        errors.append("Пожалуйста заполните все поля")
        return render_template("login6.html", errors=errors)
    if username_form == '':
        errors.append("Пожалуйста заполните все поля")
        print(errors)
        return render_template('login6.html', errors=errors)
    if password_form == '':
        errors.append("Пожалуйста заполните все поля")
        print(errors)
        return render_template('login6.html', errors=errors)
    
    else: 
        errors.append('Пользователя не существует')
        return render_template('login6.html', errors=errors)

    

@lab6.route('/lab6/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect('/lab6/glav')


@lab6.route('/lab6/glav', methods = ["GET", "POST"])
def lab6_glav():
    username_form = session.get('username')
    return render_template('glav6.html', username = username_form)


@lab6.route("/lab6/articles")
def articles_list():
    show_all_articles = request.args.get('show_all') == '1'
    if current_user and not show_all_articles:
        my_articles = articles.query.filter_by(user_id=current_user.id).all()
    elif current_user and show_all_articles:
        my_articles = articles.query.all()
    return render_template("articles6.html", articles=my_articles,show_all_articles=show_all_articles)



@lab6.route("/lab6/articles/<int:article_id>")
@login_required
def viewArticle(article_id):
    article = articles.query.get(article_id)
    username_form = session.get('username')
    if article:
        return render_template('articleN6.html', title=article.title, content=article.article_text, username_form=username_form)
    else:
        return "Статья не найдена"
    

@lab6.route("/lab6/newtitle", methods=["GET", "POST"])
@login_required
def createArticle():
    if request.method == "GET":
        return render_template("newtitle6.html")

    article_text = request.form.get("article_text")
    title = request.form.get("article_title")

    if len(article_text) == 0:
        errors = ["Заполните текст"]
        return render_template("newtitle6.html", errors=errors)

    new_article = articles(user_id=current_user.id, title=title, article_text=article_text)
        

    db.session.add(new_article)
    db.session.commit()
    
    return redirect("/lab6/articles")


def lab6_glav():
    username_form = session.get('username')
    return render_template('glav6.html', username = username_form)