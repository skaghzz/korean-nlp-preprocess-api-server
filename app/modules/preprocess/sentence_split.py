import kss


class SentenceSplit:
    def __init__(self, sentences: str):
        self.sentences: str = sentences

    def get_sentences(self) -> list[str]:
        sentence_tokenized_text: list = []
        for sent in kss.split_sentences(self.sentences.strip()):
            sentence_tokenized_text.append(sent.strip())
        return sentence_tokenized_text
