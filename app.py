from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
    return redirect("/menu", code=302)


@app.route("/menu")
def menu():
    return """
<!DOCTYPE html>
<html>
    <head>
        <title>Махмад Карина Абдуловна, лабораторная 1</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторные работы
        </header>

        <h1>НГТУ, ФБ, WEB-программирование часть 2. Список лабораторных</h1>
        <li><a href='/lab1'>Лабораторная 1</a></li>

        <footer>
            &copy; Карина Махмад, ФБИ-14, 3 курс, 2023
        </footer>
    </body>
</html>
"""


@app.route('/lab1')
def lab1():
    return """
<!DOCTYPE html>
<html>
    <head>
        <title>Махмад Карина Абдуловна, лабораторная 1</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <h1>web-сервер на flask</h1>
        <h3> <div>  
            Flask — фреймворк для создания веб-приложений на языке
            программирования Python, использующий набор инструментов
            Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
            называемых микрофреймворков — минималистичных каркасов веб-приложений, сознательно предоставляющих лишь самые базовые возможности.
        </div></h3>

        <footer>
            &copy; Карина Махмад, ФБИ-14, 3 курс, 2023
        </footer>
    </body>
</html>
"""


@app.route('/lab1/oak')
def oak():
    return '''
<!DOCTYPE html>
<html>
<link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    <body>
       <h1>Дуб</h1>
       <img src="''' + url_for('static', filename='oak.jpeg') + '''">
    </body>
</html>
'''
