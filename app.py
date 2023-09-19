from flask import Flask 
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
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
        <div>  
            Flask — фреймворк для создания веб-приложений на языке
            программирования Python, использующий набор инструментов
            Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
            называемых микрофреймворков — минималистичных каркасов

            веб-приложений, сознательно предоставляющих лишь самые ба-
            зовые возможности.
        </div>

        <footer>
            &copy; Карина Махмад, ФБИ-14, 3 курс, 2023
        </footer>
    </body>
</html>
"""