### Pandas Dataframe
```python
# dataframe option
# ======================================================================================================

# https://www.delftstack.com/ko/howto/python-pandas/how-to-pretty-print-an-entire-pandas-series-dataframe/
# pd.set_option('display.max_rows', None)     #
# pd.set_option('display.max_columns', None)  #
# pd.set_option('display.width', None)        #
# pd.set_option('display.max_colwidth', -1)   #

# ipynb 에서 한 cell에 dataframe 여러개 표시방법
# https://stackoverflow.com/questions/26873127/show-dataframe-as-table-in-ipython-notebook

# =================================================================================================
# python pandas update a dataframe value from another dataframe
# https://stackoverflow.com/questions/49928463/python-pandas-update-a-dataframe-value-from-another-dataframe
a.update(b.set_index('a'))
a.reset_index()


# about dataframe function apply
# https://www.delftstack.com/ko/howto/python-pandas/pandas-apply-function-to-every-row/
# https://www.w3resource.com/pandas/series/series-apply.php

# isinstance(object, classinfo), 오브젝트 유형비교
# isinstance(a,list) 

# version 차이에 따른 warning ignore
# warnings.filterwarnings(action='ignore')

# a = pd.DataFrame({'a':[1,2],'b':[3,4]})
# b = pd.DataFrame({'a':[5,6],'b':[3,4]})
# if column 명이 다르면 full join 함, 따라서 열이름 맞춰야함
# can pd.DataFrame(columns=['a','b'])
# print(a.append(b,ignore_index=False))

# Pandas concat vs append vs join vs merge
# https://stackoverflow.com/questions/15819050/pandas-dataframe-concat-vs-append

# Concat gives the flexibility to join based on the axis( all rows or all columns)
# Append is the specific case(axis=0, join='outer') of concat (being deprecated use concat)
# Join is based on the indexes (set by set_index) on how variable =['left','right','inner','couter']
# Merge is based on any particular column each of the two dataframes, this columns are variables on like 'left_on', 'right_on', 'on'

# +--------+---------------------------------+---------------------------------+
# |        | ignore_index=False              | ignore_index=True               |
# +--------+---------------------------------+---------------------------------+
# | size   | append | concat | append/concat | append | concat | append/concat |
# +--------+--------+--------+---------------+--------+--------+---------------+
# | small  | 0.4635 | 0.4891 | 94.77 %       | 0.4056 | 0.3314 | 122.39 %      |
# +--------+--------+--------+---------------+--------+--------+---------------+
# | medium | 0.5532 | 0.6617 | 83.60 %       | 0.3605 | 0.3521 | 102.37 %      |
# +--------+--------+--------+---------------+--------+--------+---------------+
# | large  | 0.9558 | 0.9442 | 101.22 %      | 0.6670 | 0.6749 | 98.84 %       |
# +--------+--------+--------+---------------+--------+--------+---------------+

# FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
# print(pd.concat([a, b],axis=0, ignore_index=False))

for idx, row in dataframe.iterrows():
    row[0], row[1]

dataframe[~dataframe.column.isna()] # ~는 not의 의미
dataframe[dataframe.column.isin(list)]
dataframe.column.str.split()
dataframe.column.ljust(20)

pd.DataFrame.from_dict(dataframe, orient='index')   # orient : 지향하게 하다, (특정목적에) 맞추다.

# 가끔 excel 과 한셀에서 utf-8이어도 깨지는 경우가 있음. 그래서 인코딩을 sig로 변경해주면 해결됨.
dataframe.to_csv('mapping_table.csv',encoding='utf-8-sig')
```