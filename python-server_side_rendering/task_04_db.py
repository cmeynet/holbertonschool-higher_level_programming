from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    try:
        with open('items.json', 'r') as f:
            data = json.load(f)
            items_list = data.get("items", [])
    except Exception as e:
        print(f"{e}")
        items_list = []
    return render_template('items.html', items=items_list)

@app.route('/products')
def products():
    source = request.args.get("source")
    product_id = request.args.get("id")

    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error='Wrong source')
    
    if source == "json":
        try:
            with open("products.json", "r") as f:
                products = json.load(f)
        except FileNotFoundError:
            return render_template('product_display.html', error='File not found')

    elif source == "csv":
        try:
            with open("products.csv", newline='') as f:
                reader = csv.DictReader(f)
                products = list(reader)
        except FileNotFoundError:
            return render_template('product_display.html', error='File not found')
    
    elif source == 'sql':
        try:
            conn = sqlite3.connect('products.db')
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            if product_id:
                cursor.execute('''
                    SELECT * FROM Products WHERE id = ?;
                            ''', (product_id,))
                result = cursor.fetchone()
                if result:
                    return render_template('product_display.html', products=[result])
                else:
                    return render_template('product_display.html', error='Product not found')
            else:
                cursor.execute('''
                    SELECT * FROM Products;
                            ''')
                result = cursor.fetchall()
                return render_template('product_display.html', products=result)
        except Exception:
            return render_template('product_display.html', error='Not database found')
        finally:
            conn.close()

    else:
        return render_template('product_display.html', error="Wrong source")
    
    # Filter by ID if provided
    if product_id:
        products = [p for p in products if str(p.get('id')) == product_id]
        if not products:
            return render_template('product_display.html', error='Product not found.')

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
