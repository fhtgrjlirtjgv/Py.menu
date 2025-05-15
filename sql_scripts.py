import sqlite3

def get_all_dishes():
    conn = sqlite3.connect('menu.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM dishes')
    dishes = cursor.fetchall()
    conn.close()
    
    return dishes

def get_dish(dish_id):
    conn = sqlite3.connect('menu.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM dishes WHERE id=?', [dish_id] )
    dish = cursor.fetchone()
    conn.close()
    
    return dish

def get_all_categories():
    conn = sqlite3.connect('menu.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM categories')
    dishes = cursor.fetchall()
    conn.close()
    
    return dishes


def get_by_categories(category_id):
    conn = sqlite3.connect('menu.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM dishes WHERE category_id=?',[category_id])
    dishes = cursor.fetchall()
    conn.close()
    
    return dishes

def search_categories(search_query):
    conn = sqlite3.connect('menu.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM dishes WHERE title LIKE ?', ['%'+search_query+'%'])
    dishes = cursor.fetchall()
    conn.close()

    return dishes