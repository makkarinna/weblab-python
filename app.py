from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
    return redirect("/menu", code=302)


@app.route('/lab2/example')
def example():
    name = 'Махмад Карина'
    return render_template('example.html', name=name)


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

        <div>
            <li><a href='/menu'>Меню</a></li>
        </div>

         <div id='rout'>
            <h1>Реализованные Роуты</h1>
            <ol>
                <li><a href='/lab1/oak'>Дуб</a></li>
                <li><a href='/lab1/student'>Студент</a></li>
                <li><a href='/lab1/python'>Питон</a></li>
                <li><a href='/lab1/curator'>Куратор</a></li>
            </ol>
        </div>

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


@app.route('/lab1/student')
def student():
    return '''
<!DOCTYPE html>
<html>
<link rel="stylesheet" href="''' + url_for('static', filename='student.css') + '''">
    <body>
       <h1>Махмад Карина Абдуловна</h1>
       <img src="''' + url_for('static', filename='fb.png') + '''">
    </body>
</html>
'''


@app.route('/lab1/python')
def python():
    return '''
<!DOCTYPE html>
<html>
<link rel="stylesheet" href="''' + url_for('static', filename='python.css') + '''">
    <body>
       <h1>Python</h1>
       <div>Python — высокоуровневый язык программирования общего назначения с динамической строгой типизацией 
       и автоматическим управлением памятью, ориентированный на повышение производительности разработчика, читаемости кода и его качества, 
       а также на обеспечение переносимости написанных на нём программ.</div>
       <div>Python является мультипарадигменным языком программирования, поддерживающим императивное,
        процедурное, структурное, объектно-ориентированное программирование,
        метапрограммирование и функциональное программирование.</div>

       <img src="''' + url_for('static', filename='python.png') + '''">
    </body>
</html>
'''


@app.route('/lab1/curator')
def curator():
    return '''
<!DOCTYPE html>
<html>
<link rel="stylesheet" href="''' + url_for('static', filename='curator.css') + '''">
    <body>
       <div>
            <h1>Школа кураторов 2023</h1>
            <id="fla" img src="''' + url_for('static', filename='one.jpg') + '''">
       </div>

       <di><img src="''' + url_for('static', filename='two.jpg') + '''" class="text">
            <p class="text1"> Куратор – это компетентный студент, который является проводником первокурсников в студенческую жизнь. Он необходим первокурсникам, еще вчерашним школьникам, 
            для того чтобы безболезненно вступить в новый жизненный этап. Цель работы куратора – адаптировать первокурсников к особенностям обучения в НГТУ. </p>

            <p>Школа Кураторов — проект, уже ставший традицией в НГТУ. Кураторы помогают первокурсникам адаптироваться в университете: вовлекают во внеучебную жизнь, находят ответы на вопросы, а также помогают завести новые знакомства. 
            Чтобы стать куратором, необходимо пройти отбор и обучение. 
            Отбор кандидатов происходит в два этапа: заочный, на котором надо было заполнить анкету, завершился в конце недели. Второй этап, на котором участники будут проходить собеседования.
            Основной день Школы состоялся в конце августа. Будущие кураторы систематизируют знания о самых необходимых первокурсникам ресурсах. Например, о внутренних правилах НГТУ, о студенческих организациях, медиа, Студсовете.
            Также участники смогут познакомиться друг с другом и разобрать возможные конфликтные ситуации, которые встречаются в работе группы.
            Второй блок обучения - разбор адаптационного тренинга, который кураторы проведут для первокурсников в первых числах сентября.</p>
            
       </div>

        <br> 

       <div>
            <h1 class="text3">Наша группа ФБИ-32</<h1>
            
       </div>

       <div><img src="''' + url_for('static', filename='tr.jpg') + '''" class="kartinka"></div>

       
    </body>
</html>
'''
