자연어처리
https://heave.tistory.com/73
GPT3 vs bert fine tunning할 데이터가 적으면 bert가 낫다.

```python
# https://wikidocs.net/92961
# !pip install hanspell
!pip install --pre git+https://github.com/haven-jeon/PyKoSpacing.git
!pip install h5py==3.1.0
!pip install numpy==1.19.3
# !pip install git+https://github.com/ssut/py-hanspell.git

# https://stackoverflow.com/questions/71009659/message-note-this-error-originates-from-a-subprocess-and-is-likely-not-a-prob
# This particular error is caused by not having a C/C++ compiler installed. As said in the error message, either install MSVC or another compiler to compile it.

# 불용어 처리
import pandas as pd
stopwords = pd.read_csv('stopwords_ko.csv')['0'].to_list()

# 보편적인 한국어 불용어(https://www.ranks.nl/stopwords/korean)
# (https://github.com/stopwords-iso/stopwords-ko/blob/master/stopwords-ko.txt)
# filename = 'korean stopwrods.csv'
# filename = 'stopwords-ko.txt'
# with open(filename, 'rb') as f:
#     result = chardet.detect(f.readline())  # or read() if the file is small.
#     print(result['encoding'])

# stopwords_ko = []

# filename = 'korean stopwrods.txt'
# with open(filename, 'r') as f:
#     stopwords_ko.append(f.readlines())

# filename = 'stopwords-ko.txt'
# with open(filename, 'r',encoding='UTF8') as f:
#     stopwords_ko.append(f.readlines())

# rmv = re.compile('\n')
# stopword_ko = list(set(list(map(lambda x: rmv.sub('',x), stopwords_ko[0])) + list(map(lambda x: rmv.sub('',x), stopwords_ko[1]))))
# print(len(stopword_ko))
# pd.DataFrame(stopword_ko).to_csv('stopwords_ko.csv',index=False, encoding='utf-8')
```

```python



# NLP
import re
rmv = '\(.*\)|춘천.*점$'     # 정규표현식
re.compile(rmv).sub('',x)   # ''으로 변환할 문자열 x

# 정규표현식
# \(.*\) : ()괄호와 안에있는 문자열 제거

# 텍스트 유사도 알고리즘
# String 텍스트 유사도 알고리즘3가지 : https://peanut159357.tistory.com/77
# Hamming Distace 
# LCS algorithm, levenshtein, n-gram
# jaro-winkler similarity : https://hexists.tistory.com/230
# levenshtein_distance : 같아질라면 몇번을 반복해야햐나

#!pip install jellyfish
# help(jellyfish)
# jellyfish.jaro_distance(t_txt[0])
# 단어 유사도로 찾기
import jellyfish
jellyfish.jaro_similarity(x, text)

import jellyfish
jellyfish.jaro_similarity('그리브', '그리브카페')
```