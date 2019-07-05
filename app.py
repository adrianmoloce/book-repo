import os
from flask import Flask
from util import import_json_data

FILE_PATH = os.getenv('DATA_FILE_PATH')

app = Flask(__name__)


@app.route('/')
def display_data():
    return ''.join([str(person) + '\n' for person in import_json_data(FILE_PATH)])


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
