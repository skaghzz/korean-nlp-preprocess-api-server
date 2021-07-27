from flask import Flask, request
from flask_cors import CORS

from preprocess import split_sentence as splitter
from preprocess import clean_text as cleaner
from preprocess import spell_check as spell_checker
from preprocess import kakao_spell_check

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


@app.route("/api/spell-check", methods=['POST'])
def spell_check() -> dict:
    texts = get_input_texts()
    text_list = spell_checker.spell_check(texts)
    return response(success=True, result=text_list)


def response_kakao_chatbot_simple_text(text: str) -> dict:
    return {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "교정 결과<br>" + text
                    }
                }
            ]
        }
    }


def get_input_text_kakao_chat():
    print(request.get_json())
    json_data = request.get_json()
    return json_data['action']['params']['spell_check_text']


@app.route("/api/spell-check/kakao", methods=['POST'])
def spell_check_kakao() -> dict:
    text = get_input_text_kakao_chat()
    checked_text = kakao_spell_check.spell_check(text)
    return response_kakao_chatbot_simple_text(text=checked_text)


if __name__ == '__main__':
    app.run(debug=True)
