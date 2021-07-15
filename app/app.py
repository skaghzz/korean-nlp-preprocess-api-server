from flask import Flask, request
import logging

from modules.preprocess import split_sentence as splitter

app = Flask(__name__)


@app.route("/split-sentence", methods=['POST'])
def split_sentence() -> dict:
    data = request.get_json()
    print(type(data['paragraphs']))
    logging.debug(data)
    sentence_list = splitter.split_sentence(data['paragraphs'])
    response = {
        'success': True,
        'result': {
            'sentences': sentence_list
        },
        'error': None
    }
    return response


if __name__ == '__main__':
    app.run(debug=True)
