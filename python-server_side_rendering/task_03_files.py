from flask import Flask, render_template, request
import json
import csv

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

@app.route('/product_display')
def product_display():
    source = request.args.get("source")
    product_id = request.args.get("id")

    if source not in ['json', 'csv']:
        return render_template('product_display.html', error='Wrong source')
    
    if source == "json":
        try:
            with open("products.json", "r") as f:
                products = json.load(f)
        except FileNotFoundError:
            return render_template('product_display.html', error='Not file found')

    elif source == "csv":
        try:
            with open("products.csv", newline='') as f:
                reader = csv.DictReader(f)
                products = list(reader)
        except FileNotFoundError:
            return render_template('product_display.html', error='Not file found')
    
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
