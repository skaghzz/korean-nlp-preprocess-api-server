import re


def clean_text(texts: list[str]) -> list[str]:
    corpus = []
    for t in texts:
        tt = re.sub(r'[@%\\*=()/~#&\+á?\xc3\xa1\-\|\.\:\;\!\-\,\_\~\$\'\"]', '', t)  # remove punctuation
        tt = re.sub(r'\d+', '', t)  # remove number
        tt = tt.lower()  # lower case
        tt = re.sub(r'\s+', ' ', tt)  # remove extra space
        tt = re.sub(r'<[^>]+>', '', tt)  # remove Html tags
        tt = re.sub(r'\s+', ' ', tt)  # remove spaces
        tt = re.sub(r"^\s+", '', tt)  # remove space from start
        tt = re.sub(r'\s+$', '', tt)  # remove space from the end
        corpus.append(tt)
    return corpus
