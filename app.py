from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


# Эндпоинт для отображения графика
@app.route('/graph')
def get_data():
    return render_template('graph.html')


if __name__ == '__main__':
    app.run()
