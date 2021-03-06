from unittest import TestCase
from preprocess.split_sentence import split_sentence


class TestSentenceSplit(TestCase):
    def setUp(self) -> None:
        self.target_sentences = """제임스 얼 "지미" 카터 주니어는 민주당 출신 미국 39번째 대통령 이다.

지미 카터는 조지아주 섬터 카운티 플레인스 마을에서 태어났다.

조지아 공과대학교를 졸업하였다.

그 후 해군에 들어가 전함·원자력·잠수함의 승무원으로 일하였다.

1953년 미국 해군 대위로 예편하였고 이후 땅콩·면화 등을 가꿔 많은 돈을 벌었다.

그의 별명이 "땅콩 농부" 로 알려졌다.

1962년 조지아 주 상원 의원 선거에서 낙선하나 그 선거가 부정선거 였음을 입증하게 되어 당선되고, 1966년 조지아 주 지사 선거에 낙선하지만 1970년 조지아 주 지사를 역임했다.

대통령이 되기 전 조지아주 상원의원을 두번 연임했으며, 1971년부터 1975년까지 조지아 지사로 근무했다.

조지아 주지사로 지내면서, 미국에 사는 흑인 등용법을 내세웠다.

1976년 대통령 선거에 민주당 후보로 출마하여 도덕주의 정책으로 내세워, 포드를 누르고 당선되었다."""

    def test_splitting(self):
        sentences_list = split_sentence([self.target_sentences])
        self.assertIsInstance(sentences_list, list)
        self.assertTrue(len(sentences_list) > 0)
