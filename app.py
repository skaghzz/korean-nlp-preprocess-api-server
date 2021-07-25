from flask import Flask, request
from flask_cors import CORS

from preprocess import split_sentence as splitter
from preprocess import clean_text as cleaner

app = Flask(__name__)
CORS(app, resources={
    r"/v1/*": {"origin": "*"},
    r"/api/*": {"origin": "*"}
})


def response(success=True, error=None, result=None) -> dict:
    return {
        'success': success,
        'error': error,
        'result': result
    }


def get_input_texts():
    json_data = request.get_json()
    return json_data['texts']


@app.route('/')
def index():
    return response(success=True, result="korean nlp preprocess server is on.")


@app.route("/api/split-sentence", methods=['POST'])
def split_sentence() -> dict:
    texts = get_input_texts()
    sentence_list = splitter.split_sentence(texts)
    return response(success=True, result=sentence_list)


@app.route("/api/clean-text", methods=['POST'])
def clean_text() -> dict:
    texts = get_input_texts()
    text_list = cleaner.clean_text(texts)
    return response(success=True, result=text_list)


if __name__ == '__main__':
    app.run(debug=True)