import unittest
from preprocess.spell_check import spell_check
from preprocess.kakao_spell_check import split_sentence_under_500, NAVER_SPELL_CHECK_MAX_LENGTH


class MyTestCase(unittest.TestCase):
    def test_something(self):
        text = "카카오뱅크의 '휴면예금·보험금 찾기' 서비스를 통해 969만원을 찾은 고객이 나왔다. 카카오뱅크는 '휴면예금·보험금 찾기' 서비스가 출시 2주 만에 조회 건수가 100만 건을 돌파했다고 5일 밝혔다. 카카오뱅크 앱을 통해 휴면예금과 휴면보험금을 찾아간 건수는 전날 자정 기준으로 총 27만5000건이며, 금액은 총 56억원을 기록했다. 이중 최고 지급 금액은 약 969만원으로, 1인당 평균 3만371원의 휴면예금 및 보험금을 수령했다. 100만원 이상 고액을 찾아간 고객도 766명에 달한다. 연령대별로는 중장년층이 많은 금액을 수령한 것으로 나타났다. 40대 이상 중장년층이 59.2%로 가장 높았으며, 30대가 30.8%, 20대 이하가 10% 차지했다. '휴면예금/보험금 찾기' 서비스 이용을 위해 가입한 신규회원 중 40대 이상 중장년층 비중은 67%에 달한다. '휴면예금·보험금 찾기'는 카카오뱅크 계좌 개설 고객은 누구나 이용할 수 있는 서비스다. 한번에 휴면예금은 물론, 휴면보험금까지 간편하게 조회하고 신청할 수 있다. 또 8월31일까지 ‘휴면예금/보험금 찾기’ 고객 이벤트를 진행하고 있다. 이 기간 중 휴면예금과 휴면보험금을 조회하고 이벤트에 참여한 고객에게는 커피쿠폰을 추첨하여 제공한다. 자세한 사항은 카카오뱅크 앱 및 홈페이지를 통해 확인할 수 있다."
        result = split_sentence_under_500(text)
        self.assertIsInstance(result, list)
        for r in result:
            self.assertTrue(len(r) < NAVER_SPELL_CHECK_MAX_LENGTH)


if __name__ == '__main__':
    unittest.main()
