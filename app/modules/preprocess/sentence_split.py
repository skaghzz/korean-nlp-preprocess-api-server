import kss


class SentenceSplit:
    punct = "/-'?!.,#$%\'()*+-/:;<=>@[\\]^_`{|}~" + '""“”’' + '∞θ÷α•à−β∅³π‘₹´°£€\×™√²—–&'
    punct_mapping = {"‘": "'", "₹": "e", "´": "'", "°": "", "€": "e", "™": "tm", "√": " sqrt ", "×": "x", "²": "2", "—": "-", "–": "-", "’": "'", "_": "-", "`": "'", '“': '"', '”': '"', '“': '"', "£": "e", '∞': 'infinity', 'θ': 'theta', '÷': '/', 'α': 'alpha', '•': '.', 'à': 'a', '−': '-', 'β': 'beta', '∅': '', '³': '3', 'π': 'pi', }

    def __init__(self, sentences: str):
        self.sentences: str = sentences

    def get_sentences(self) -> list[str]:
        sentence_tokenized_text: list = []
        for sent in kss.split_sentences(self.sentences.strip()):
            sentence_tokenized_text.append(self.__clean_punc(sent.strip()))
        return sentence_tokenized_text

    @staticmethod
    def __clean_punc(text, punct=punct, mapping=punct_mapping):
        for p in mapping:
            text = text.replace(p, mapping[p])

        for p in punct:
            text = text.replace(p, f' {p} ')

        specials = {'\u200b': ' ', '…': ' ... ', '\ufeff': '', 'करना': '', 'है': ''}
        for s in specials:
            text = text.replace(s, specials[s])

        return text.strip()
