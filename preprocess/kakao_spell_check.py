from preprocess.py_hanspell import spell_checker


def spell_check(text: str) -> str:
    checked = spell_checker.check(text)
    return checked.as_dict()['checked']
