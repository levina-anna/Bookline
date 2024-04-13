import requests
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/graph')
def graph():
    api_url = 'http://127.0.0.1:8000/products_and_categories'

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as e:
        return str(e), 500

    category_counts = {}
    for entry in data:
        category = entry['category_name']
        category_counts[category] = category_counts.get(category, 0) + 1

    return render_template('graph.html', categories=category_counts)


if __name__ == '__main__':
    app.run()
