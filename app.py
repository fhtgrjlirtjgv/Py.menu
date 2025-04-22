from flask import Flask, render_template
from sql_scripts import *

app = Flask(__name__)  # Створюємо веб–додаток Flask


@app.route("/")  # Вказуємо url-адресу для виклику функції
def index():
    dishes = get_all_dishes()
    categories = get_all_categories()
    return render_template("index.html", dishes=dishes,categories=categories)  # html-сторінка, що повертається у браузер

@app.route("/categories/<int:category_id>")  # Вказуємо url-адресу для виклику функції
def category_pg(category_id):
    dishes = get_by_categories(category_id)
    categories = get_all_categories()
    return render_template("index.html", dishes=dishes,categories=categories)  # html-сторінка, що повертається у браузер



if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True  # автоматичне оновлення шаблонів
    app.run(debug=True)  # Запускаємо веб-сервер з цього файлу в режимі налагодження

