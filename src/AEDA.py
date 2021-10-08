import random
from typing import List
from copy import deepcopy
from konlpy.tag import Mecab

mecab = Mecab()
text = "이 주변에 맛집이 어디 있나요?"
print(mecab.morphs(text))
a = []
for i in text.split():
    k = mecab.morphs(i)
    print(k)
    a.extend(k)
print(a)


def morphs_except_specialToken(text, morph_func, special_tokens):
    text_list = text.split()
    morph_list = []
    for word in text_list:
        if word in special_tokens:
            morph_list.extend([word, " "])
        else:
            words = morph_func(word)
            morph_list.extend([*words, " "])
    morph_list.pop()  # delete last space
    return morph_list


class AEDA:
    def __init__(
        self,
        special_tokens=[],
        punc_ratio=0.3,
        random_punc=True,
        punc_list=[".", ",", ";", ":", "?", "!"],
    ):
        self.tag = Mecab()
        self.special_tokens = special_tokens
        self.punc_ratio = punc_ratio
        self.random_punc = random_punc
        self.punc_list = punc_list

    def __call__(self, *args, **kwds):
        return self.aeda(*args, **kwds)

    def aeda(self, text: str, add_special_tokens: List[str] = []) -> str:
        # 인덱스 기준으로 나누기
        special_tokens = deepcopy(self.special_tokens) + add_special_tokens
        punc_ratio = self.punc_ratio

        morph_list = morphs_except_specialToken(text, self.tag.morphs, special_tokens)

        aug_word_index_list = [
            index for index in range(len(morph_list)) if morph_list[index] != " "
        ]
        punc_num = (
            random.randint(1, int(punc_ratio * len(aug_word_index_list) + 1))
            if self.random_punc
            else int(punc_ratio * len(aug_word_index_list) + 1)
        )

        aug_word_index_list = random.sample(aug_word_index_list, punc_num)

        # AUG 만들기 repete 쓰기

        for index in range(morph_list):
            if index in aug_word_index_list:
                morph_list[index]  # 여기부터 수정

        return text
