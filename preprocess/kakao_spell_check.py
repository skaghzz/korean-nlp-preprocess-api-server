from preprocess.py_hanspell import spell_checker
from preprocess.split_sentence import split_sentence
import io

NAVER_SPELL_CHECK_MAX_LENGTH = 500


def split_sentence_under_500(text: str) -> list[str]:
    split_text = []
    if len(text) < NAVER_SPELL_CHECK_MAX_LENGTH:
        return [text]
    for sentence in split_sentence([text]):
        if len(sentence) > NAVER_SPELL_CHECK_MAX_LENGTH:
            for phrase in sentence.split(','):
                split_text.append(phrase)
        else:
            split_text.append(sentence)
    return split_text


def spell_check(text: str) -> str:
    checked_result = io.StringIO()
    text_list = split_sentence_under_500(text)
    for t in text_list:
        checked = spell_checker.check(t)
        checked_result.write(checked.as_dict()['checked'])
    return checked_result.getvalue()
