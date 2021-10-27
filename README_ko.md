# KoAEDA

한국어 AEDA 모듈

# 설치

```zsh
  $ pip install koaeda

  $ sudo apt-get install g++ openjdk-8-jdk python3-dev python3-pip curl

  $ bash <(curl -s https://raw.githubusercontent.com/konlpy/konlpy/master/scripts/mecab.sh)
```

# 사용법

## 기본 사용법

```python
  from koaeda import AEDA

  ko_aeda = AEDA()

  text = "이 주변에 맛집이 어디 있나요?"

  result = ko_aeda(text)

  print(result)
  >> 이 ?  주변에  : 맛집이 ;  어디 있나요?
```
