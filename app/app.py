from flask import Flask, render_template
import json

app = Flask(__name__)


def load_services():
    with open('services.json', 'r') as json_file:
        services = json.load(json_file)
    return services


@app.route('/')
def home():
    services = load_services()
    return render_template('home.html', services=services)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
