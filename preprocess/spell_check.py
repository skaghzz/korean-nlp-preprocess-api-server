from preprocess.py_hanspell import spell_checker


def spell_check(texts: list[str]) -> list[str]:
    ret = []
    for checked in spell_checker.check(texts):
        ret.append(checked.checked)
    return ret
