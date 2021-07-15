import kss


def split_sentence(paragraphs: list[str]) -> list[str]:
    sentence_tokenized_text: list = []
    for paragraph in paragraphs:
        for sent in kss.split_sentences(paragraph.strip()):
            sentence_tokenized_text.append(sent.strip())
    return sentence_tokenized_text
