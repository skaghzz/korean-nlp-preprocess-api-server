from flask import Flask, request

from modules.preprocess import split_sentence as splitter
from modules.preprocess import clean_text as cleaner

app = Flask(__name__)


def response(result) -> dict:
    return {
        'success': True,
        'error': None,
        'result': result
    }


def get_input_texts():
    data = request.get_json()
    return data['texts']


@app.route("/split-sentence", methods=['POST'])
def split_sentence() -> dict:
    texts = get_input_texts()
    sentence_list = splitter.split_sentence(texts)
    return response(sentence_list)


@app.route("/clean-text", methods=['POST'])
def clean_text() -> dict:
    texts = get_input_texts()
    text_list = cleaner.clean_text(texts)
    return response(text_list)


if __name__ == '__main__':
    app.run(debug=True)
