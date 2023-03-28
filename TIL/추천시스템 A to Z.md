
ppt 한번 정리하기. 어느정도 다 알던 내용들.
> # Chapter 01.overview

> ## 02. 추천 시스템 분류

- 요건 : Best(Popularity가 높은 아이), Related, Personalized, Context-aware
- 데이터 : Explicit, Implicit
- 모델 : CBF, CF, Hybrid
- 계량 방식 : Ration Prediction, Top-K Rec.


> ## 03. 추천 시스템 성능 평가

이력 데이터 - 시간에 따라 데이터를 바꿈.


RMSE : 큰 오차에 큰 페널티, 작은 오차에 작은 페널티
MAE : 오차 만큼페널티 부
> ## 04. 추가적인 고려 사항
>
> UI/UX 그저 list에서 다양한 의견과 취향을 반영하여 디자인이 바뀜(Netflex)
> 추천 시스템을 만들때 어떻게 하느냐는 특정 시스템을 만들때 사람들이 어떻게 접근하느냐에 대해 접근해야한다. 모델에 대해 정확도로만 따지는 DS들은 중요하지만 추천시스템에서는 효과가 발휘되는 방식들이 상당히 다양하고 여러 관점에서 바라보아야하고 우리가 얻고싶은 목적에따라 어떤 추천시스템을 고려해야하는지 지속적으로 생각해야함.

```python
%run liblecture.py
```

user based 가 item based보다 정확도가 더 높지만 계산 cost가 더 많다. 현실에서는 item보다 user의 수가 더 많기 때문에.


> # Chapter 3. E-commerce 추천
```python
%sql postgresql+psycopg2://user:@0.0.0.0:5432/db-name

# %문법?

%%sql # sql script
select * from table;

# sql 안에서
copy cmc_envet from :event_file
# :뒤는 변수로서 들어간다고 생각하면 됨.
```
> ## 01. 커머스 추천 개요

> ## 02. Best 추천

> ## 03. 연관 상품 추천

> ## 04. 개인화 추천


SVD
A = U\sigmaV^T

A를 회전변환, 크기 변환, 회전변환으로 나누어 표현.