# api server preprocess korean for nlp
한국어 전처리를 각 기능을 api로 제공합니다.   
한국어 전처리 웹사이트 구축 프로젝트의 일부입니다.

## 사용 방법
```commandline
pip install -r requirements.txt
```

## 기능
| 기능 | 출처 |
| --- | --- |
|  문장분리  | [한국어전처리] |

## API specification
### 0. 공통
#### request
- 인풋은 모두 texts에 있으며, list[str] 형태입니다.
- request case
```json
{
  "texts": ["문장1", "문장2와 그 뒤", "문장3"]
}
```

#### reseponse
- success case
```json
{
  "success": true,
  "error": null,
  "result": []
}
```
- fail case
```json
{
  "success": false,
  "error": "error 정보",
  "result": null
}
```

### 1. 문장 분리
- api : /split-sentence
- kss를 이용하여 문장을 분리한 결과를 반환한다.
- request
```json
{
    "texts":["어우지금입니다. 아니요. 강하다.", "댈저해두제더"]
}
```
- response
```json
{
    "error": null,
    "result": [
        "어우지금입니다.",
        "아니요.",
        "강하다.",
        "댈저해두제더"
    ],
    "success": true
}
```

### 2. 불필요 키워드 제거
- api : /clean-text
- 정규식을 이용하여 문장을 정제합니다. 주로 불필요한 키워드를 제거합니다.
- 정규식 적용 순서는 아래와 같습니다.
    - 구두점 제거
    - 숫자 제거
    - 소문자 변경
    - 여러개의 공란은 한개로 변경
    - html 태그 제거
    - 여러개의 공란은 한개로 변경
    - 문장 시장 공란 제거, 끝 공란 제거
- request
```json
{
    "texts":["어우지금##입12321니다. 아니22요. 강하다.", "댈저해두제더"]
}
```
- response
```json
{
    "error": null,
    "result": [
        "어우지금##입니다. 아니요. 강하다.",
        "댈저해두제더"
    ],
    "success": true
}
```

## 참고
- [한국어 전처리][한국어전처리]
- [문장분리][kss]

[한국어전처리]: https://colab.research.google.com/drive/1FfhWsP9izQcuVl06P30r5cCxELA1ciVE?usp=sharing#scrollTo=8nIXezslMdDC
[kss]: https://github.com/hyunwoongko/kss