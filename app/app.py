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


@app.route("/split-sentence", methods=['POST'])
def split_sentence() -> dict:
    data = request.get_json()
    sentence_list = splitter.split_sentence(data['paragraphs'])
    return response(sentence_list)


@app.route("/clean-text", methods=['POST'])
def clean_text() -> dict:
    data = request.get_json()
    text_list = cleaner.clean_text(data['text'])
    return response(text_list)


if __name__ == '__main__':
    app.run(debug=True)
