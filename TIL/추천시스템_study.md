- flask : https://okky.kr/articles/1318880
    - flask가 기본 제공하는 서버인 Werkzeug이고, app.run()함수 내부를 보면 threaded 옵션을 True로 설정하고 있다. 그래서 기본적으로 동시 요청을 쓰레드로 처리한다.
    - 즉, flask는 들어오는 요청을 병렬 처리하기때문에 추가적으로 수정할 필요가 없다.


- AWS What is Recommendation : [URL](https://rstudio-pubs-static.s3.amazonaws.com/668748_d374e1a7f0584c74af50cf7b0aac79ca.html)

---
---

- ### 추천 시스템 도서

    > Recommender System

    ![img](https://media.springernature.com/w184/springer-static/cover/book/978-3-319-29659-3.jpg?as=webp)

    - 1\. 추천 시스템 소개
        - 1.2 목표
            - 예측모델 : 행렬 완성
            - 랭킹 모델 : top-k 추천 문제
            - 관령성, 참신성, 의외성, 다양성


        - 1.3 기본 모델
            - 1.3.1 협업 필터링 
                - 메모리 기반 방법(이웃 기반 협업 필터링) : , 경험을 기반으로 하지만 유사도 기반 모델로 간주할 수 있음

                    > 이웃이 다른 이웃을 돕는다면 우리의 커뮤니티는 더 강해집니다 - 제니퍼 팔카

                    - 사용자 기반 협업 | 유사한 유저들의 평점을 이용, 사용자간의 유사도
                    - 아이템 기반 협업 | 비슷한 아이템들의 평점을 이용, 아이템간의 유사도

                    다음 두 가지 중 하나의 방법으로 계산
                    - 유저-아이템 조합의 평점 값 예측. | 사용자-아이템의 평점 행렬, 누락값은 평점은 예측된다.
                    - 상위-k 아이템(사용자) 결정 | 가장 관련있는 상위-k의 사용자나 아이템을 결정


                - 모델 기반 방법론
                    - 의사결정트리
                    - 룰 기반 모델
                    - 베이지안 방법론
                    - 잠재요인분석 Latent factor
                
                - 평점의 종류
                    - 인터벌 기반평점 : 순서가 정렬된 서로 다른 숫자의 인터벌 형태로 정량화
                    - 짝 수개의 인터벌 기반 평점 : ㅍ여점 척도의 불균형이 있음, 강제 선택 평가 시스템
                    - 서수 평점 : 순서형의 범주형 값
                    - 이진 평점 : 좋고 싫음
                    - 단항 평점 : 호감만 표시, 암시적인 데이터에서 흔하게 보임., 긍정적 선호만을 의미하기에 긍정적 선호 효용행렬이라고 부름
                    - 명시적 평점 : 사용자가 직접 입력하는
                    - 암시적 평점 : 사용자 행동을 기반으로 만들어지는 평점, 누락된 평점을 대체하는 것을 권장하지 않음(분석의 큰 편향이 발생) 그러나 누락된 평점을 대체하면  큰양의 과적합을 방지해주는 이점이 있어 이 관계에서의 트레이드-오프가 형성
                
                협업 필터링은 예측이 행 방식이 아닌 항 방식으로 수행하는 분류와 회귀 모델링의 ㅇ일반화다. ㅎ애렬 완성 문제는 분류 및 회귀문제에서 전이 환경(ㅎ테스트 인스턴스는 학습 과정에 포함, 학습할때 존재하지 않는 테스트 인스턴스를 예측하는 일은 어려운 경우가 많음)과 많은 특징을 공유한다. 이와 반대로 새로운 인스턴스에 대한 예측을 쉽게 할 수 있는 모델(나이브 베이즈 모델)을 귀납적이라고 한다. 이 점은 모델 기반 협업필터링 방법론의 경우 더욱 심각. 하지만 최근의 행렬완성모델은 표본에서 벗어난 사용자나 아이템의 평점도 예측 할 수 있도록 귀납적으로 다자인 됨.
            
            - 1.3.2 콘텐츠 기반 추천 시스템.
            
                아이템의 설명 속성을 활용.
                평점 데이터가 충분하지 않은 새로운 아이템에 대한 추천에 있어 
                키워드나 내용 때문에 명백한 추천을 제공해 이용한 적이 없는 아이템을 절대 추천하지 않을 것이다. 이런 현상은 다양성을 줄이는 바람직하지 않은경우
                새로운 사용자에게 제안하는 추천은 효과적이지 않음.

                지식 기반 시스템과 매우 밀접하게 연관, 때로는 두 가지 간의 명백한 경계가 존재하는지 의문이 제기되기도 한다.

            - 1.3.3 지식 기반 추천 시스템.

                자주 구매하지 않는 아이템에 대해서 특히나 유용.

                1. 제약기반(constraint-based) | 사용자가 아이템에 대한 요구 사항과 제한 내용을 기입
                2. 사례기반 | 특정 사례는 앵커 포인트(anchor points)로 저장되고, 비슷한 결과가 표시 된다.
                

                - 1.3.3.1 효용 기반 추천 시스템.

                    효용 함수는 사용자가 아이템을 좋아할 확률을 계산하기 위해 제품 피처에 정의한다.

            - 1.3.4 인구 통계학적 추천 시스템.

                사용자에 대한 인구통계학적 정보를 구매 성형과 연결할 수 있는 분류 모델을 학습하는데 활용.  
                독립적인 활용으로 최상의 결과를 제공하지는 않지만 하이브리드 또는 앙상블 모델의 구성요소로서 힘을 크게 보탠다.
            
            - 1.3.5 하이브리드와 앙상블 기반 추천 시스템.

                여러 유형의 기계 학습 알고리즘의 힘을 결합하여 더욱 견고한 모델을 만든다.
            
            - 1.3.6 추천 시스템 평가

        - 1.4 도메인 특화 과제

            - 1.4.1 컨텍스트 기반 추천 시스템

                시간, 위치, 소셜 데이터 포함    
            
            - 1.4.2 시간에 민감한 추천 시스템

                커뮤니티 태도가 진화하고 사용자의 관심이 시간 흐름과 함께 변할 수 있다.  
                아이템의 평점은 특정 주기에 따라 달리질 수 있다.

            - 1.4.3 위치 기반 추천 시스템

                - 사용자별 지역성 | 사용자의 지리적 위치는 선호도에 중요한 역할
                - 아이템별 지역성 | 아이템의 지리적 위치는 사용자의 현재 위치에 따라 관련성에 영향을 미칠 수 있다.
            
            - 1.4.4 소셜 추천 시스템

                - 노드와 링크의 구조적인 추천 | 다양한 유형의 네트워크는 노드와 링크로 구성되어 이를 추천하는 것이 바람직함
                - 사회적 영향을 고려한 제품과 콘텐츠 추천 | 네트워크 연결 및 기타 사회적 신호를 통해 수행하는 이런 문제들을 바이럴 마케팅이라고도 한다.
                - 신뢰할 수 있는 추천 시스템 | 다양한 피드백 매커니즘을 통해 신뢰할 수 있는 정보를 통합하는 것은 강력한 추천으로 이어질 수 있다.
                - 소셜 태그 피드백을 활용한 추천 | 피드백을 통합하는 방법으로 '소셜 태깅'이 일반적,
        
        - 1.5 고급 주제 및 애플리케이션

            - 1.5.1 콜드 스타트
            - 1.5.2 공격에 강한 추천 시스템

    ---

    2. 이웃기반 협업 필터링

        아이템에 대한 평점 분포는 롱테일형태.  
        극히 일부만 자주 평가.(즉, 자주 평가한 아이템의 수가 적어 다양함에 부정적이고 유명한 것들만 추천해줘 지루함을 줄 수 있다)

        - 평점 예측

            이웃 기반 모델 | 유사한 사용자들은 같은 상품에 대해 비슷한 평점을 준다.
            아이템 기반 모델 | 유사한상품은 동일한 사용자에게 비슷한 방식으로 평점이 매겨진다.

            - 사용자 기반 이웃 모델

                모든 사용자와의 유사도 계산, 두 사용자간의 유사도를 알아내는 방버브로 피어슨 계수.

                계산을 위한 첫번째 단계는 명시된 평점을 활용하여 각 사용자 u에 대한 평점의 평균 계산   
                $\mu_u = \frac{\sum_{k \in I_u} r_{uk}}{|I_u|}$  
                
                그리고 u와 v의 행간의 피어슨 상관계수는 아래와 같다.  
                $sim(u,v) = Pearson(u,v) = \frac{\sum_{k \in I_u \cap I_v}(r_{uk-\mu_u}) \cdot (r_{vk} - \mu_v)}{\sqrt{\sum_{k \in I_u \cap I_v}(r_{uk} - \mu_u)^2} \cdot \sqrt{\sum_{k \in I_u \cap I_v}(r_{vk} - \mu_v)^2}}$
                
                평균 중심 과정  
                $ \hat{r}_{uj} = \mu_u + \frac{\sum_{v \in P_u(j)} sim(u,v) \cdot (r_{vj} - \mu_v) }{\sum_{v \in P_u(j)}|sim(u, v)}  $
                ($P_u(j)$는 아이템 j에 대해 평점을 매긴 타깃 사용자 u의 최근접 사용자 k명의 집합 1이다.)

                - 유사도 함수 변형

                    RawCosine - 코사인 함수를 평균 중심 평점에 쓰는 것이 아닌 평점 그자체에 사용하는 것.
                    보편적으로는 피어슨 상관계수는 평균 중심에서는 bias 조정 효과가 있기 때문에 rawcosine이 더 바람직하다.
                    유사도 함수의 신뢰도는 사용자간의 공통 평점 개수 $|I_u \cap I_v|$에 종종 영향을 받는다. 만일 두 명의 사용자가 공통적으로 평점을 부여한 수가 적다면, 유사도 함수는 두 사용자 쌍의 중요도를 덜 강조하기 위해 할인 요인을 적용해 낮춘다. 이 방법론을 `중요도 가중`이라고 한다. 할인 요인 값은 $min{|I_u \cap I_v|, \beta} \over \beta$와 같고 (0,1) 범위 이다.
                
                - 예측 함수의 변형

                    이웃 기반 협업 필터링 방법론은 가까운 이웃 분류(회귀) 방법론의 일반화다.
                    $sim(u,v) = Pearson(u,v)^{\alpha}$라는 유사도 함수를 가지고 있다고 생각하면 이는 이웃 회귀 방법론이다.

                - 피어 그룹 필터링의 변형

                    타깃 사용자에 대한 피어 그룹은 다양한 방법으로 정의되고 필터링 될 수 있다. 예측함수가 기술적으로는 약하거나 부정적 평점을 활용할 수는 있지만 이웃 방법론의 광범위한 원칙과 일관되지 않아 약하거나 음의 상관관계를 가진 평점은 필터링 돼 제외되는 경우가 많다.

                - 롱테일의 영향

                    실제 컨텍스트에서의 평점 분포는 롱테일 분포를 따른다.이런 평점은 사용자간의 차별성이 적기 때문에 추천 품질을 악화시킬 수 있다. 
                    이 케이스에서도 역문도서빈도(idf)의 개념을 활용할 수 있는데,   
                    $w_j = log(\frac{m}{m_j})$(단, m은 총 사용자 수, $m_j$는 아이템 j에 대한 평점 개수)
                    하면 피어슨 상관계수는  
                    $$sim(u,v) = Pearson(u,v) = \frac{\sum_{k \in I_u \cap I_v}w_k\cdot(r_{uk-\mu_u}) \cdot (r_{vk} - \mu_v)}{\sqrt{\sum_{k \in I_u \cap I_v}w_k\cdot(r_{uk} - \mu_u)^2} \cdot \sqrt{\sum_{k \in I_u \cap I_v}w_k\cdot(r_{vk} - \mu_v)^2}}$$
                    와 같이 변형이 가능하다.

            - 아이템 기반 이웃 모델

                피어 그룹은 사용자가 아닌 아이템으로 구성.
                $$AdjustedCosine(i,j) = \frac{\sum_{u \in U_i \cap U_j}s_{ui} \cdot s_{uj}}{\sqrt{\sum_{u \in U_i \cap U_j}s^2_{ui}} \cdot \sqrt{\sum_{u \in U_i \cap U_j}s^2_{uj}}}$$

                사용자 u의 타깃 아이템 t에 대한 예측 평점 $\hat{r}_{ut}$는 다음과 같다.
                $$ \hat{r}_{ut} = \frac{\sum_{j \in Q_t(u)}AdjustedCosine(j,t) \cdot r_{uj}}{\sum_{j \in Q_t(u)}|AdjustedCosine(j,t)|}$$
                ($Q_t(u)$ :사용자 u가 평점을 지정한 아이템 t에 상위-k로 매칭되는 아이템들)

            
            - 효율적 구현 및 계산 복잡성

                이웃 기반 방법론은 항상 오프라인, 온라인 단계로 나뉜다.
                오프라인은 유사도 값, 피어 그룹이 계산.
                온라인 단계는 이 유사도 값과 피어그룹을 활용해 예측을 수행한다.
                이웃 기반 방법론의 주요한 계산상의 복잡성은 종종 수행돼야 하는 오프라인 단계에 있다.

            - 클러스터링과 이웃 기반 방법론

                이웃 기반 방법론의 주요 문제점은 오프라인 단계에서의 복잡성이다. 이 문제는 사용자의 수보다 아이템의 수가 굉장히클때 더 크게 나타난다. 클러스터링 기반 방법론의 주요 관점은 오프라인에서의 가장 근접한 이웃 단계를 클러스터링단계로 대체하는 것이다.

            - 차원 축소와 이웃 기반 방법론.

                차원 축소 방법론은 이웃 기반 방법론의 품질과 효율성을 높이는 데 쓰일 수 있다. 차원 축소는 잠재 요인에 있어 저차원이 가능하도록 한다. 이런 경우 잠재 요인 모델이라고도 한다. 비록 두 사용자가 공통으로 평점을 매긴 아이템이 매우 적다 하더라도, 저차원 잠재 벡터에서는 그 거리가 계산될 수 있다. 더 나아가 피어 그룹을 결정하는데 더욱 효율적이다.
                행렬 R( m x n) 영점 행렬을 주성분 분석을 이용해 저차원으로 변환시킨다. 결과 행렬 R'는
                SVD(특이값 분해)

                - 바이어스 문제 처리

                    행렬 $R_f$는 불특정 항목을 행 또는 열에 따라 평균 값으로 작성해 불완전행렬 R에서 파생된다는 점에 유의해야한다.

                    1. 최대 우도 추정 - 공분산 행렬을 추정하기 위해 EM(expectation-maximaize)알고리즘과 같은 확률적 기술의 사용을 제안한다.
                    1. 불완전한 데이터의 직접 행렬 인수분해 - 최대 우도 추정 방법은 데이터가 희소한 경우 효과적이지는 않다. 행렬이 희박하면 공분산 추정치가 통계적으로 신뢰할 수 없다. 좀 더 직접적인 방법은 행렬 인수분해 방법을 사용하는 것이다. 특이값 인수분해와 같은 방법은 본질적으로 행렬 인수분해 방법이다.

            - 이웃 방법론의 회귀 모델링 관점
                
                 .86

- 1장. 추천 시스템 소개
    - 1.1 개요
    - 1.2 추천 시스템의 목표
    - 1.21 추천 애플리케이션의 범위
    - 1.3 추천 시스템의 기본 모델
    - 1.3.1 협업 필터링 모델
    - 1.3.1.1 평점의 종류
    - 1.3.1.2 결측치 분석과의 관계
    - 1.3.1.3 분류와 회귀 모델링의 일반화로써의 협업 필터링
    - 1.3.2 콘텐츠 기반 추천 시스템
    - 1.3.3 지식 기반 추천 시스템
    - 1.3.31 효용 기반 추천 시스템
    - 1.3.4 인구 통계학적 추천 시스템
    - 1.3.5 하이브리드와 앙상블 기반 추천 시스템
    - 1.3.6 추천 시스템의 평가
    - 1.4 추천 시스템의 도메인 특화 과제
    - 1.4.1 컨텍스트 기반 추천 시스템
    - 1.4.2 시간에 민감한 추천 시스템
    - 1.4.3 위치 기반 추천 시스템
    - 1.4.4 소셜 추천 시스템
    - 1.4.4.1 노드와 링크의 구조적 추천
    - 1.4.4.2 사회적 영향을 고려한 제품과 콘텐츠 추천
    - 1.4.4.3 신뢰할 수 있는 추천 시스템
    - 1.4.4.4 소셜 태그 피드백을 활용한 추천
    - 1.5 고급 주제 및 애플리케이션
    - 1.5.1 추천 시스템의 콜드 스타트 문제
    - 1.5.2 공격에 강한 추천 시스템
    - 1.5.3 그룹 추천 시스템
    - 1.5.4 다중 기준 추천 시스템
    - 1.5.5 추천 시스템의 능동 학습
    - 1.5.6 추천 시스템의 개인정보보호
    - 1.5.7 애플리케이션 도메인
    - 1.6 요약
    - 1.7 참고문헌
    - 1.8 연습 문제

- 2장. 이웃 기반 협업 필터링
    - 2.1 개요
    - 2.2 평점 행렬의 주요 특징
    - 2.3 이웃 기반 방법론의 평점 예측
        - 2.3.1 사용자 기반 이웃 모델
        - 2.3.1.1 유사도 함수 변형
        - 2.3.1.2 예측함수의 변형
        - 2.3.1.3 피어 그룹 필터링의 변형
        - 2.3.1.4 롱테일의 영향
        - 2.3.2 아이템 기반 이웃 모델
        - 2.3.3 효율적 구현 및 계산 복잡성
        - 2.3.4 사용자 기반 방법론과 아이템 기반 방법론의 비교
        - 2.3.5 이웃 기반 방법론의 장점과 단점
        - 2.3.6 사용자 기반과 아이템 기반 방법론의 통합된 관점
    - 2.4 클러스터링과 이웃 기반 방법론
    - 2.5 차원 축소와 이웃 기반 방법론
        - 2.5.1 바이어스 문제 처리
        - 2.5.1.1 최대 우도 추정
        - 2.5.1.2 불완전한 데이터의 직접 행렬 인수분해
    - 2.6 이웃 방법론의 회귀 모델링 관점
        > 사용자 기반 및 아이템 기반 방법론 모두에 대한 중요한 발견은 이웃 사용자의 동일 항목 또는 이웃 항목의 동일 사용자의 평점의 선형함수로 평점을 예측한다는 것이다. 예측 평점은 동일한 아이템의 다른 평점의 가중 선형 조합이다.
        즉, 사용자 기반 이웃 방법론의 경우 예측 평점은 동일 아이템의 다른 평점의 가중 선형 조합입니다. 조합가중치로 유사도 값을 사용하는 것은 오히려 휴리스틱적이고 임의적입니다. 모델링 관점에서의 최적성으로 인해 평점을 결합한 가중치가 더 합리적입니다.

        - 2.6.1 사용자 기반 최근접 이웃 회귀
            > 최적화 모델의 통합버전과 인수분해된 버전 모두 최소 제곱 최적화 문제다.
        - 2.6.1.1 희소성 및 바이어스 문제
            > 
        - 2.6.2 아이템 기반 가장 근접 이웃 회귀
            > 
        - 2.6.3 사용자 기반 및 아이템 기반 방법 결합
            >
        - 2.6.4 유사도 가중치를 이용하는 조인트 보간법
            >Joint interpolation, 
        - 2.6.5 희소 선형 모델(SLIM)
            >
    - 2.7 이웃 기반 방법에 대한 그래프 모델
        - 2.7.1 사용자-아이템 그래프
        - 2.7.1.1 랜덤 워크를 이용한 이웃 정의
        - 2.7.1.2 카츠 척도를 이용한 이웃 정의
        - 2.7.2 사용자-사용자 그래프
        - 2.7.3 아이템-아이템 그래프
    - 2.8 요약
    - 2.9 참고문헌
    - 2.10 연습 문제

- 3장. 모델 기반 협업 필터링
    - 3.1 개요
        > 이웃 기반 방법은 k-최근접 이웃 분류 모델의 일반화로 볼 수 있고, 이 방법ㅇ들은 인스턴스 기반 방법으로 효율적인 구현을 위한 선택적 전처리 단계 이외의 예측을 위한 모델을 만들지 않는다. 또한, 사례 기반 학습 방법 또너ㅡㄴ 예측할 데이터 사례에 특화된 접근 방법을 취하는 '게으른 학습 방법'의 일반화다. 
    - 3.2 의사 결정 및 회귀 트리
    - 3.2.1 의사 결정 트리를 협업 필터링으로 확장
    - 3.3 규칙 기반 협업 필터링
    - 3.3.1 협업 필터링을 위한 레버리지 연관 규칙의 활용
    - 3.3.2 아이템별 모델 대 사용자별 모델
    - 3.4 나이브 베이즈 협업 필터링
    - 3.4.1 과적합 조정
    - 3.4.2 이진 평점에 대한 베이즈 방법의 적용 예
    - 3.5 임의의 분류 모델을 블랙 박스로 사용
    - 3.5.1 예: 신경망을 블랙 박스로 사용
    - 3.6 잠재 요인 모델
    - 3.6.1 잠재 요인 모델에 대한 기하학적 직관
    - 3.6.2 잠재 요인 모델에 관한 저차원 직관
    - 3.6.3 기본 행렬 인수분해 원리
    - 3.6.4 제약 없는 행렬 인수분해
    - 3.6.4.1 확률적 경사하강법
    - 3.6.4.2 정규화
    - 3.6.4.3 점진적 잠재성분 훈련
    - 3.6.4.4 최소 제곱과 좌표 하강의 교차 적용
    - 3.6.4.5 사용자 및 아이템 바이어스 통합
    - 3.6.4.6 암시적 피드백 통합
    - 3.6.5 특이값 분해
    - 3.6.5.1 SVD에 대한 간단한 반복 접근법
    - 3.6.5.2 최적화 기반 접근법
    - 3.6.5.3 표본 외 추천
    - 3.6.5.4 특이값 분해의 예
    - 3.6.6 비음행렬 인수분해
    - 3.6.6.1 해석 가능성의 장점
    - 3.6.6.2 암시적 피드백을 사용한 인수분해에 대한 고찰
    - 3.6.6.3 암시적 피드백에 대한 계산 및 가중치 문제
    - 3.6.6.4 좋아요와 싫어요가 모두 있는 평점
    - 3.6.7 행렬 인수분해 계열의 이해
    - 3.7 분해와 이웃 모델 통합
    - 3.7.1 베이스라인 추정 모델: 개인화되지 않은 바이어스 중심 모델
    - 3.7.2 모델의 이웃 부분
    - 3.7.3 모델의 잠재 요인 부분
    - 3.7.4 이웃 및 잠재 요인 부분의 통합
    - 3.7.5 최적화 모델 풀기
    - 3.7.6 정확도에 대한 고찰
    - 3.7.7 잠재 요인 모델을 임의 모델과 통합
    - 3.8 요약
    - 3.9 참고문헌
    - 3.10 연습 문제

- 4장. 콘텐츠 기반 추천 시스템
    - 4.1 개요
    - 4.2 콘텐츠 기반 시스템의 기본 구성 요소
    - 4.3 전처리 및 피처 추출
    - 4.3.1 피처 추출
    - 4.3.1.1 상품 추천의 예
    - 4.3.1.2 웹 페이지 추천의 예
    - 4.3.1.3 음악 추천의 예
    - 4.3.2 피처 표현 및 정제
    - 4.3.3 사용자가 좋아하는 것과 싫어하는 것 수집
    - 4.3.4 지도 피처 선택과 가중치 설정
    - 4.3.4.1 지니 계수
    - 4.3.4.2 엔트로피
    - 4.3.4.3 X2-통계
    - 4.3.4.4 정규화된 편차
    - 4.3.4.5 피처 가중치 설정
    - 4.4 사용자 프로파일 학습 및 필터링
    - 4.4.1 최근접 이웃 분류
    - 4.4.2 사례 기반 추천 시스템과의 연결
    - 4.4.3 베이즈 분류 모델
    - 4.4.3.1 중간 확률 추정
    - 4.4.3.2 베이즈 모델의 예
    - 4.4.4 규칙 기반 분류 모델
    - 4.4.4.1 규칙 기반 방법의 예
    - 4.4.5 회귀 기반 모델
    - 4.4.6 기타 학습 모델 및 비교 개요
    - 4.4.7 콘텐츠 기반 시스템에 관한 설명
    - 4.5 콘텐츠 기반 대 협업 필터링 추천
    - 4.6 협업 필터링 시스템을 위한 콘텐츠 기반 모델 사용
    - 4.61 사용자 프로파일 활용
    - 4.7 요약
    - 4.8 참고문헌
    - 4.9 연습 문제

- 5장. 지식 기반 추천 시스템
    - 5.1 개요
    - 5.2 제약 조건 기반 추천 시스템
    - 5.2.1 관련 결과의 반환
    - 5.2.2 상호작용 방법론
    - 5.2.3 일치하는 아이템의 순위 매기기
    - 5.2.4 허용되지 않는 결과 또는 공집합 처리
    - 5.2.5 제약 조건 추가
    - 5.3 사례 기반 추천
    - 5.3.1 유사도 메트릭
    - 5.3.1.1 유사도 계산에 다양성 통합
    - 5.3.2 수정 방법론
    - 5.3.2.1 간단한 수정
    - 5.3.2.2 복합적 수정
    - 5.3.2.3 동적 수정
    - 5.3.3 수정에 대한 설명
    - 5.4 지식 기반 시스템의 지속적인 개인화
    - 5.5 요약
    - 5.6 참고문헌
    - 5.7 연습 문제

- 6장. 앙상블 기반과 하이브리드 추천 시스템
    - 6.1 개요
    - 6.2 분류 관점에서 본 앙상블 방법
    - 6.3 가중 하이브리드
    - 6.3.1 다양한 유형의 모델 조합
    - 6.3.2 분류에서 배깅 적응
    - 6.3.3 무작위성의 주입
    - 6.4 스위칭 하이브리드
    - 6.4.1 콜드 스타트 문제를 위한 스위칭 메커니즘
    - 6.4.2 모델 버킷
    - 6.5 캐스케이드 하이브리드
    - 6.5.1 추천의 연속적인 재정의
    - 6.5.2 부스팅
    - 6.5.2.1 가중 기본 모델
    - 6.6 피처 증강 하이브리드
    - 6.7 메타 레벨 하이브리드
    - 6.8 피처 결합 하이브리드
    - 6.8.1 회귀 및 행렬 인수분해
    - 6.8.2 메타 레벨 피처
    - 6.9 혼합 하이브리드
    - 6.10 요약
    - 6.11 참고문헌
    - 6.12 연습 문제

- 7장. 추천 시스템 평가
    - 7.1 개요
    - 7.2 평가 패러다임
        - 7.2.1 사용자 연구
        - 7.2.2 온라인 평가
        - 7.2.3 과거 데이터 세트를 사용한 오프라인 평가
    - 7.3 평가 디자인의 일반적 목표
        - 7.3.1 정확성
        - 7.3.2 커버리지
        - 7.3.3 신뢰도와 신뢰
        - 7.3.4 참신성
        - 7.3.5 의외성
        - 7.3.6 다양성
        - 7.3.7 강건성과 안정성
        - 7.3.8 확장성
    - 7.4 오프라인 추천 평가의 설계 문제
        - 7.4.1 넷플릭스 프라이즈 데이터 세트 사례 연구
        - 7.4.2 학습 및 테스트 평점 분류
        - 7.4.2.1 홀드 아웃
        - 7.4.2.2 교차 검증
        - 7.4.3 분류 설계와 비교
    - 7.5 오프라인 평가의 정확도 지표
        - 7.5.1 평점 예측의 정확도 측정
        - 7.5.1.1 RMSE 대 MAE
        - 7.5.1.2 롱테일의 영향력
        - 7.5.2 상관관계를 통한 순위 평가
        - 7.5.3 유용성을 통한 순위 평가
        - 7.5.4 수신자 조작 특성을 통한 순위 평가
        - 7.5.5 어떤 순위 측정 척도가 가장 좋은가?
    - 7.6 평가 측정 척도의 한계
        - 7.6.1 평가 조작 방지
    - 7.7 요약
    - 7.8 참고문헌
    - 7.9 연습 문제

- 8장. 컨텍스트에 맞는 추천 시스템
    - 8.1 개요
    - 8.2 다차원 접근법
        - 8.2.1 계층 구조의 중요성
    - 8.3 컨텍스트 사전 필터링: 감소 기반 접근 방식
        - 8.3.1 앙상블 기반 개선 사항
        - 8.3.2 다단계 추정
    - 8.4 사후 필터링 방법론
    - 8.5 컨텍스트별 모델링
        - 8.5.1 이웃 기반 방법
        - 8.5.2 잠재 요인 모델
            - 8.5.2.1 인수분해 머신
            - 8.5.2.2 2차 인수분해 머신의 일반화
            - 8.5.2.3 잠재 파라미터화의 다른 적용 사례
        - 8.5.3 콘텐츠 기반 모델
    - 8.6 요약
    - 8.7 참고문헌
    - 8.8 연습 문제

- 9장. 시간과 위치에 민감한 추천 시스템
    - 9.1 개요
    - 9.2 시간적 협업 필터링
    - 9.2.1 최신성 기반 모델
    - 9.2.1.1 감쇠 기반 방법
    - 9.2.1.2 윈도우 기반 방법
    - 9.2.2 주기적 컨텍스트 처리
    - 9.2.2.1 사전 필터링과 사후 필터링
    - 9.2.2.2 시간적 컨텍스트의 직접적인 포함
    - 9.2.3 시간 함수로서의 평점 모델링
    - 9.2.3.1 시간-SVD++ 모델
    - 9.3 이산 시간 모델
    - 9.3.1 마르코프 모델
    - 9.3.1.1 선택적 마르코프 모델
    - 9.3.1.2 다른 마르코프 대안
    - 9.3.2 순차 패턴 마이닝
    - 9.4 위치 인식 추천 시스템
    - 9.4.1 선호 지역
    - 9.4.2 여행 지역
    - 9.4.3 선호도와 여행 위치 조합
    - 9.5 요약
    - 9.6 참고문헌
    - 9.7 연습 문제

- 10장. 네트워크의 구조 추천
    - 10.1 개요
    - 10.2 순위 알고리듬
    - 10.2.1 페이지랭크
    - 10.2.2 개인화된 페이지랭크
    - 10.2.3 이웃 기반 방법에 대한 응용
    - 10.2.3.1 소셜 네트워크 추천
    - 10.2.3.2 이종 소셜 미디어의 개인화
    - 10.2.3.3 전통적인 협업 필터링
    - 10.2.4 유사도랭크
    - 10.2.5 검색과 추천의 관계
    - 10.3 집단 분류에 의한 추천
    - 10.3.1 반복 분류 알고리듬
    - 10.3.2 랜덤 워크를 통한 레이블 전파
    - 10.3.3 소셜 네트워크에서 협업 필터링에 대한 적용성
    - 10.4 친구 추천: 링크 예측
    - 10.4.1 이웃 기반 척도
    - 10.4.2 카츠 척도
    - 10.4.3 랜덤 워크 기반 척도
    - 10.4.4 분류 문제로서의 링크 예측
    - 10.4.5 링크 예측을 위한 행렬 인수분해
    - 10.4.5.1 대칭 행렬 인수분해
    - 10.4.6 링크 예측과 협업 필터링 간의 연결
    - 10.4.6.1 협업 필터링에 링크 예측 알고리듬 사용
    - 10.4.6.2 협업 필터링 알고리듬을 사용한 링크 예측
    - 10.5 사회적 영향 분석 및 입소문 마케팅
    - 10.5.1 선형 임계값 모델
    - 10.5.2 독립 캐스케이드 모델
    - 10.5.3 영향 함수 평가
    - 10.5.4 소셜 스트림의 목표 영향 분석 모델
    - 10.6 요약
    - 10.7 참고문헌
    - 10.8 연습 문제

- 11장. 사회와 신뢰 중심 추천 시스템
    - 11.1 개요
    - 11.2 사회적 맥락을 위한 다차원 모델
    - 11.3 네트워크 중심과 신뢰 중심 방법론
    - 11.3.1 신뢰 네트워크 구축을 위한 데이터 수집
    - 11.3.2 신뢰 전파 및 집계
    - 11.3.3 신뢰 전파가 없는 단순 추천 모델
    - 11.3.4 TidalTrust 알고리듬
    - 11.3.5 MoleTrust 알고리듬
    - 11.3.6 TrustWalker 알고리듬
    - 11.3.7 링크 예측 방법론
    - 11.3.8 행렬 인수분해 방법론
    - 11.3.8.1 로지스틱 함수의 개선
    - 11.3.8.2 소셜 신뢰 성분의 변형
    - 11.3.9 소셜 추천 시스템의 장점
    - 11.3.9.1 논란의 여지가 있는 사용자와 아이템에 대한 추천
    - 11.3.9.2 콜드 스타트의 유용성
    - 11.3.9.3 공격 저항
    - 11.4 소셜 추천 모델의 사용자 상호작용
    - 11.4.1 포크소노미 표현하기
    - 11.4.2 소셜 태깅 시스템의 협업 필터링
    - 11.4.3 의미 있는 태그 선택
    - 11.4.4 평점 행렬이 없는 소셜 태깅 추천 모델
    - 11.4.4.1 컨텍스트 민감 시스템을 위한 다차원 방법론
    - 11.4.4.2 순위 기반 방법론
    - 11.4.4.3 콘텐츠 기반 방법론
    - 11.4.5 평점 행렬을 사용한 소셜 태깅 추천 모델
    - 11.4.5.1 이웃 기반 접근법
    - 11.4.5.2 선형 회귀
    - 11.4.5.3 행렬 인수분해
    - 11.4.5.4 콘텐츠 기반 방법
    - 11.5 요약
    - 11.6 참고문헌
    - 11.7 연습 문제

- 12장. 공격 방지 추천 시스템
    - 12.1 개요
    - 12.2 공격 모델의 트레이드 오프 이해
    - 12.2.1 공격 영향 계량화
    - 12.3 공격 유형
    - 12.3.1 랜덤 공격
    - 12.3.2 평균 공격
    - 12.3.3 밴드 왜건 공격
    - 12.3.4 인기 공격
    - 12.3.5 사랑/증오 공격
    - 12.3.6 역밴드 왜건 공격
    - 12.3.7 탐지 공격
    - 12.3.8 세그먼트 공격
    - 12.3.9 기본 추천 알고리듬의 효과
    - 12.4 추천 시스템에서 공격 탐지
    - 12.4.1 개인 공격 프로파일 탐지
    - 12.4.2 그룹 공격 프로파일 탐지
    - 12.4.2.1 전처리 방법
    - 12.4.2.2 온라인 방법
    - 12.5 강력한 추천 디자인을 위한 전략
    - 12.5.1 CAPTCHA를 사용한 자동 공격 방지
    - 12.5.2 사회적 신뢰 사용
    - 12.5.3 강력한 추천 알고리듬 설계
    - 12.5.3.1 클러스터링을 이웃 방법에 통합
    - 12.5.3.2 추천 시간 동안 가짜 프로파일 탐지
    - 12.5.3.3 연관 기반 알고리듬
    - 12.5.3.4 강건한 행렬 인수분해
    - 12.6 요약
    - 12.7 참고문헌
    - 12.8 연습 문제


- 13장. 추천 시스템의 고급 주제
    - 13.1 개요
    - 13.2 순위학습
    - 13.2.1 쌍별 순위학습
    - 13.2.2 목록 순위학습
    - 13.2.3 다른 도메인에서의 순위학습 방법과 비교
    - 13.3 멀티암 밴딧 알고리듬
    - 13.3.1 나이브 알고리듬
    - 13.3.2 e-탐욕 알고리듬
    - 13.3.3 상계(신뢰상한) 방법
    - 13.4 그룹 추천 시스템
    - 13.4.1 협업 및 콘텐츠 기반 시스템
    - 13.4.2 지식 기반 시스템
    - 13.5 다중 기준 추천 시스템
    - 13.5.1 이웃 기반 방법
    - 13.5.2 앙상블 기반 방법
    - 13.5.3 전체 평점 없는 다중 기준 시스템
    - 13.6 추천 시스템의 능동적 학습
    - 13.6.1 이질성 기반 모델
    - 13.6.2 성능 기반 모델
    - 13.7 추천 시스템의 개인정보보호
    - 13.7.1 응축 기반 개인정보보호
    - 13.7.2 고차원 데이터에 대한 도전
    - 13.8 흥미로운 응용 분야
    - 13.8.1 포털 콘텐츠 개인화
    - 13.8.1.1 동적 프로파일러
    - 13.8.1.2 구글 뉴스 개인화
    - 13.8.2 전산 광고 대 추천 시스템
    - 13.8.2.1 멀티암 밴딧의 중요성
    - 13.8.3 상호 추천 시스템
    - 13.8.3.1 하이브리드 방법 활용
    - 13.8.3.2 링크 예측 방법 활용
    - 13.9 요약
    - 13.10 참고문헌


---
---

- ### 추천 시스템 목표
    - Goals of Recommender System
        - Relevance(관련성)    : 추천된 아이템이 유저에게 관련이 있는가?
        - Novelty(참신성)      : 색다른 아이템이 추천되는가?(예상 가능)
        - Serendipity(의외성)  : 새로운 아이템을 추천하는가?(예상 불가능)
        - Diversity(다양성)    : 추천된 top k 아이템에 다양한 아이템이 포함되는가?    

    <br>
    
- ### 추천 시스템 평가
    <!-- https://sungkee-book.tistory.com/11 -->
    - evaluation metrix 
        1. Ranking based
            - Precision@K/Recall@K : confusion matrix에서의 Precision과 Recall의 의미와 같다, @K는 추천 아이템의 개수를 의미
                - Precision@K   : 1로 예측한 것 중에 실제 1이 얼마나 있는지, 내가 추천한 아이템 중 사용자가 관심있어 하는 아이템의 비율
                - Recall@K      : 실제 1 중에서 내가 1로 예측한 것이 얼마나 있는지, 사용자가 관심있어하는 아이템 중 추천한 아이템이 얼마나 포함되는지
            - Mean Average Precision@K  : 성능평가에 순서 개념을 도입함.
                - Average Precision@K       : AP@K = $\frac{1}{m}\sum_{i=1}^{K}$ Precision@i • rel(i), rel(i) : relevance로 가중치 0 or 1
                - Mean Average Precision@K  : MAP@K = $\frac{1}{|U|}\sum_{u=1}^{|U|}(AB@K)_{u}$
            - NDCG@K(Normalized Discounted Cumlative Gain) : 순서별로 가중치 값 rel(i)의 값을 다르게 적용하여 계산한다.
                - Cumulative Gain, $CG_{k}$ : $\sum_{i=1}^{K}rel_{i}$, 추천한 아이템의 Relevance 합
                - Discounted Cumulative Gain, $DCG_{k}$ : $\sum_{i=1}^{K}\frac{rel_{i}}{\log_{2}(i+1)}$, CG에 순서에 따른 할인 개념을 도입한 것
                - Ideal DCG, $IDCG_{k}$ : $\sum_{i=1}^{K}\frac{rel_{i}^{opt}}{\log_{2}(i+1)}$, 최선의 추천을 했을 때 받는 DCG 값 
                - Normailzed DCG, $NDCG_{k}$ : $\frac{DCG}{IDCG}$, DCG에 정규화를 적용한 갓
                - 결론적으로 NDCG@K는 가장 이상적인 추천 조합 대비 현재 모델의 추천 리스트가 얼마나 좋은지를 나타내는 지표이며 DCG와 달리 K에 독립적이고 정규화를 통해 비교가 용이
            - Hit Rate      : 전체 사용자 수 대비 적중한 사용자 수를 의미
                - $Hit Rate = \frac{\# of Hit User}{\# of User}$

        1. rating predict based
            - MAE   : 예측 평점 간 절대 오차에 대해서 평균
            - RMSE  : 예측 평점과 실제 평점의 오차 제곱의 평균에 루트를 취한 값.

    <br>

- ### 추천 피드 종류
    ![image](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fk.kakaocdn.net%2Fdn%2FnWrQK%2FbtraFD2DBB1%2FfNS1yLvzfkpLZbKSev6KS0%2Fimg.png)

    1. Collaborative Filtering
        
        > Cold Start        : 충분한 User와 평가 정보가 확보 되어야 한다.   
        > Sparsity          : User-Item matrix가 희소행렬이다.   
        > First rater       : 평가되지 않은 item은 추천 되지 않는다.   
        > Poplarity Bias    : 독특한 취향의 user에게는 적합한 추천이 어렵다   
        > Long tail problem : pareto rules(사용자들이 관심을 많이보이는 소수의 인기있는 콘텐츠만 추천)

        - find 'Similar' user 
            - Jaccard similarity measure : rating 값 자체는 반영 안되는 단점.
            - Cosine similarity measure : 등급이 낮아도 불이익을 받지 않는 단점
                - 주로 item-based CF 에서 사용, (1,1), (5,5) 를 유사하다고 평가하는 단점.
            - Peason correlation coefficient : 평균을 뺸 이후 cosine similarity
                - 주로 User based CF 에서 사용, 값에 절대적인 크기를 고려할때

        - Model-based
            
            > sparse 한 데이터도 처리가 가능하나 결과의 설명력이 낮음.
            > sparse 한 NaN 값들을 0이나 평균으로 대체 그러나 평균이 대체로 성능이 좋음
            > 또한, 행에 대한 평균이나 열에 평균등으로 나뉘어짐
            
            1. Non-Parametric Approach(비모수접 접근법)

                - KNN

            </br>
                
            1. Matrix Factorization based Algorithm
                - Naive Bayes model
                - Latent factor based(잠재 모델 기반)
                    - ALS(Alternating Least Squares)
                    - SGD(user-bias, item-bias 포함하기 즉, 별점을 후한 사람은 편향을 높이 설정)
                    - SVD(Singular value decomposition) : 최소의 오차(SSE, RMSE 와 유사)를 가지지만 구체적인 설명이나 이유가 없음.
                        
                        1. SVD의 문제점

                            ![차원의 저주](https://user-images.githubusercontent.com/90318043/158060061-99570121-3601-4e7c-980f-44d04022544b.png)
                            *차원의 저주*
                            
                            ![SVD + 매개변수](https://user-images.githubusercontent.com/90318043/158059965-a0aac8d8-39f1-4d97-a0cc-4ef8f6eeba6d.png)
                            *SVD + 매개변수 : 정확도 높힌 Collaborative filtering Rec_sys*

                - Non-Negative Matrix Factorization    
                    - rating matrix 에서 음수를 허용 안함. 즉, 의미 해석이 가능해짐.

        </br>

        - Memory-Based(neighborhood-based)  
        
            > 쉽고 결과의 설명려이 좋으며 도메인에 의존적이지 않으나, 데이터 축적이 안되고 sparse한 경우 성능과 확장성이 낮음
            
            - User-Based  : 나와 유사한 사용자를 찾고 그 사람이 좋아한 item 추천  
                &rarr; user-item matrix에서 user와 user의 similarity 측정
            - item-Based  : 특정 item을 좋아한 사용자를 찾고 공통적으로 좋아한 다른 item을 찾음.  
                &rarr; item-user matrix에서 item과 item의 similarity 측정

        <br>

        - Deep Learning(Deep Recommender Systems)

            - Mutli-layered neural nets(including embedding layers)
            
        <br>

    1. Content-based Recommender Systems(TF-IDF, Bag of Word, Word2Vec)
        - feature extraction : 모든 item들의 feature가 정의되어야 하고, 이는 keyword 등이 있다.
        - Nearest Neighbor Classification
        - Bayes Classification
        - Linear Regression-Based Models
        - CounterVectorizer:  텍스트에서 단어 출현 횟수를 카운팅하다. 조사, 지시 대명사 같이 의미 없는 글자들도 카운팅한다. 가장 단순하지만 효과가 떨어지는 방법이다.
        - TfidfVectorizer: CounterVectorizer을 보완했다. 해당 문장 안에서 많이 등장하지만 다른 문서들에서는 적게 사용된 단어들 위주로 카운팅한다. 변별력 있는 단어들을 비중 있게 카운팅한다.

    1. Knowledge based Recommender Systems(구매 이력이 적은 경우, 사용자가 필요한 조건을 직접 입력한다.)
        <!-- Knowledge based Recommender Systems : https://blog.naver.com/jamesoh0813/222461663923 -->
        - constraint-based  : query 처럼 작동, 원하는 조건을 입력과 성능 향상을 위해 반복적인 작업
        - case-based        : 특정 item과 비슷한 top k의 아이템들을 얻고 critquing을 통해 애트리뷰트 조절.
        

    1. Hybrid Recommender Systems(Ensemble-based)
        - Method
            - Weighted
            - Switching
            - Feature Combination
            - Feature Augmentation
            - Cascade
            - Meta-level

    1. Popularity Model
        <!-- https://velog.io/@readymadelife/%EC%B6%94%EC%B2%9C%EC%8B%9C%EC%8A%A4%ED%85%9C%EC%9D%98-%EC%9D%B8%EA%B8%B0%EB%8F%84-%EA%B8%B0%EB%B0%98-%EC%B6%94%EC%B2%9C -->
        - Most Popular, 조회수가 가장 많은 아이템 추천
            - Hacker news formula : $ score = \frac{pageviews - 1}{(age+2)^{gravity}}$
            - Reddit formula : $ score = \log_{2}(ups-downs) + \frac{sign(ups-downs) * seconds}{45000}$
        - Highly Rated, 평점 평균이 가장 높은 아이템
            - steam rating Formula : $ avg\_rating = \frac{\# of positive reviews}{\# of reviews}$, $avg\_rating - (avg\_rating -0.5)*2^{-\log(\# of reviews)}$

#### NIPA 성능 검증 test
> user, restaurant, score matrix에서의 평점 예측을 통한 RMSE 측정.  
> 추천 시스템에서 accuracy로 RMSE를 사용할 시 Matrix Factorizaition base의 평점 예측을 사용해야함.   

- surprise model.(SVD best rmse.)
    > 테스트 데이터 및 환경 통제가 가능해 RMSE가 안정적인 평가 지표이므로 test 진행 시 RMSE로 진행.

<br><br>

REFERENCES

---

1. [Deep Neural Networks for YouTube Recommendations](https://medium.com/curg/알수있는-유투브-추천-알고리즘-1fbeb1a6d5db)
    - 후보 생생(candidate generation)과 랭킹(ranking)을 분리하여 설계
    - 해당 논문에서 유튜브는 추천 시스템을 구현하는데 고려할 사항을 3가지로 나눔
        - Scale : 유투브는 많은 데이터를 가지고있어 평범한 딥러닝 방식으로는 처리가불가능, 따라서 데이터를 분산시켜 학습
        - Freshness : 영상의 추가, 삭제에 따라 추천이 빠르게 업데이트 되어야한다
        - Noise : 과거데이터만으로는 정확하게 예측이 어려우며, 과거 데이터로 추천한 영상에 대한 정확한 피드백을 얻지 못한다. implicit feedback(암시적 피드백인 추천한 영상을 얼마나 시청했는지에 대한 정보)를 활용.
    - input data : watch vector, search vector, geographic embedding(범주형 자료를 연속형 벡터로 치환하는 것), example age, 성별 등의 특성을 embedding함.
        - 검색과 영상 vector 시간 순서대로 처리하지 않고 average 처리를 하는데 최근 검색 부분에서만 추천이 된다면 사용자들이 다양한 분야의 영상을 접할 수 없기때문.
        - example age란? 영상에 나이를 의미하고 새로운 영상에 대한 수요가 높다는 것을 반영할 수 있다.
        - 사용될 라벨과 영상의 context를 선택할 때 한 사용자당 최대 개수를 지정하여 모든 사용자가 균등한 가중치를 가질 수 있도록 함. 즉, Long tail problem(pareto rule) 해결.
        - label의 과거 데이터를 이용하여 다음을 예측하는 것이 더 효과적이라고 함. 예를 들면, 우리가 시리즈물을 보고있으면 다음 시리즈의 label을 볼 가능성이 크기때문에 과거 데이터를 기반으로 추천하는 것이 전체 범위에서 랜덤으로 영상을 추천하는 것보다 더 효율적이다.

    - Training
        - fully-connected layer와 ReLU를 사용, output은 유저의 선호도(user vector)이다.
            - user vector에 negative 샘플링을 사용하여 개수를 줄임.
            - softmax를 통해 나온 영상별 가중치 벡터를 nearest neighbor 알고리즘으로 순위를 정함
        - ranking
            - 사용자와 영상의 언어, 마지막 시청 시간, 사용자의 시청 여부 등 다양한 특징 활용
            - 영상 클릭 여부가 아닌 영상의 시청 시간을 가중치로 두는 이유는 광고성, 낚시성 영상을 걸러내기 위함.
    - 결론
        - 2010에 발표한 논문(filtering)보다 DNN을 황용한 방법이 성능이 좋음.(example age와 사용자의 시청 시간별로 가중치를 준 것이 성능향상에 큰 영향이라고 함.)
        - 실제 사용자가 추천 영상을 보지 않고 시간이 지나면 랭킹이 내려가야 하는데 이를 위해 유투브에서는 초 단위로 모델이 노출 이후의 시간을 확인하면서 추천을 바꾸고 있다고 한다.
        - 이러한 결과를 도출하기 위해 특성을 가공하는 비중이 생각보다 커 feature engineering이 굉장이 중요하다고 함.


1. [Netfliex 평가제도 개선 후 평가활동의 두 배 이상의 증가 및 매치 지수 표현 가능.](https://brunch.co.kr/@cysstory/159)
    
    > 넷플릭스 회원은 20개 이내의 타이틀 검토 후 영화를 결정하지 못하면 1분후에 흥미를 잃는다.

    - 고객을 자주 방문하게 만들고 최대한 오래 붙잡아 두는 게 OTT 플랫폼 성공의 핵심 요소이다.

1. [추천의 핵심은 오랫동안 머물 도록 하는 것](https://post.naver.com/viewer/postView.nhn?volumeNo=28425732&memberNo=41516152) -

    > Algorithm is KING - Omar Kbiri

    - 나이브 베이즈를 통해 정확도 등을 표시 가능.
        

1. [왓챠](https://dbr.donga.com/article/view/1901/article_no/9065/ac/a_view)
    - 헤비유저에 집중해 기초 데이터 확보 : 알고리즘 개발 시 가장 중요한 자원은 고객 데이터. 
    - 어떻게 유의미한 데이터를 최대한 많이 모을 수 있을까? &rarr; 헤비 유저(관심이 많은) 공략.
    - A/B 테스트에 대한 집착으로 추천 알고리즘의 성능을 고도화함.
        - A/B 테스트란? 알파/베타 테스트로 2-표본 가설 검정이다.

1. [카카오 AI추천 방식](https://tech.kakao.com/2021/12/27/content-based-filtering-in-kakao/)
    - 강화 학습 알고리즘 중 하나인 Multi-Armed Bandits을 사용. : 카지노에서 어떤 슬롯머신에 투자를 해야 이익을 최대화할 수 있을지에 대한 문제를 풀기 위한 알고리즘으로 알려져있음.


1. [다양한 추천 알고리즘](https://davinci-ai.tistory.com/13)
    - Facebook : Edge Rank Algorithm
        - 친밀도(Affinity) > 가중치(Weight) > 시간(Decay) 순서로 점수에 가중치 부여
        - Affinity  : 사용자와 게시글 작성자 간의 관계, 좋아요, 댓글, 공유, 태그 등
        - Weight    : 과거 사용자가 반응한 게시물과 현재 평가하고자 하는 게시물의 유사성과 그에 대한 반응
        - Decay     : 게시물 작성된 시간, 마지막 반응 시간, 작성자와 관계를 맺은 시기 등 기준으로 계산합
        - 그 외 : Story Bumping(스토리 범핑, 지나간 게시물 분석), Last Actor(라스트 액터, 최근 50개)
    - Netflix : Cine-match Algorithm(Content-based와 Collaborative filtering의 Hybrid 알고리즘)
        - Bayesian Classifier : A영화를 본사람이 B영화를 볼 확률
        - Association Analysis : 동시 발생 상관관계(A,B가 동시에 좋다고 판단할 때 A,B의 상관관계를 알아보는 방법)
        - NN : 소비자 선호 분야를 포함한 영화적 Attrivute들에 대해 가중치 결정
    - Watcha : Collaborative filtering을 사용
        - 소비습관 기반의 넷플릭스와 다르게 사용자 평점 토대이다
        - 소비자가 집접 콘텐츠를 평가하여 자신의 성향을 분석해 추천
        - Collaborative filtering의 단점이 그대로 들어남.

    - Amazon : Amazon A9(item to item collaboration filtering)
        - 제품들간의 유사성을 계산해서 특정 제품을 구매한 모든 고객에 대해서 각 고객이 구매한 다른 제품과 이 제품과의 유사성의 합을 계산
    - 추천 시스템 이슈
        - 감정 조작 실험 : 뉴스피드가 긍정적이면 우리의 감정도 긍정적이 됨.
        - 정교한 추천 시스템을 위한 데이터 구성이 쉽지 않다
        - 평가하기가 까다로운 추천 시스템
        - 지나친 개인 소비 패턴 노출

1. [try make to better than Cinematch algorithm](https://github.com/storieswithsiva/Movie-Recommendation-Netflix)
    - learn about how to feature visualization & feature engineering.

1. [Evaluating RecSys](https://medium.com/fnplus/evaluating-recommender-systems-with-python-code-ae0c370c90be)
    - its concluding 7 parts of recommendation.
    - evaluation : two different sub-processes(offline evaluating, online A/B testing)
    - offline metrics는 개발할때만 사용하고 현실 세계의 user들에게는 끔찍하게 안먹힐 수도있다.
    - 위에 관한 문제를 Youtube에서는 'THE SURROGATE PROBLEM'로 부르며 연구를 하고 있다.
    - 그러면 우리는 왜 offline metrics를 사용해야하는가? A/B test는 비용과 시간이 많이 들어서.
    
    | ![image](https://miro.medium.com/max/1100/1*OocsyZ_QUxySU_wxKsmypg.jpeg) |
    |:--:|
    | Source: HT2014 Tutorial Evaluating Recommender Systems — Ensuring Replicability of Evaluation|
    
    - offline metrics
        - Mean Absolute Error (MAE)
        - Root Mean Square Error (RMSE) : MAE를 쓰는 것보다의 이점은 error가 높을때 페널티를 부여하는 것이다.
            - in real world, MAE나 RMSE나 의미없다. 중요한것은 유저에게 추천된 top N 개와 유저들이 반응한 것이 중요하다.
        - Hit Rate (HR) : (HITS IN TEST) / (NUMBER OF USERS), generate top N recommendations, hard with large dataset.
        - Average Reciprocal Hit Rate (ARHR) : 랭크가 높은 item에 hit할때 더 높은 가중치
        - Cumulative Hit Rate (cHR) : 특정 treshold보다 낮으면 버림.
        - Rating Hit Rate (rHR) : 예상 등급 점수로 분류
        - Coverage : percentage of possible recommendations(<user>, <item> pair) that system can predict
        - Diversity(다양성) : variety of items in system (1- Similarity)
        - Novelty(참신함) : more important strike balance between Novelty and Trust
        - Churn(휘돌다) : How often do recommendations change?, same recommendations all the time is bad, but high churn score is bad too. so we must understand the trade-offs between them
        - Responsiveness : How quickly does new user behavior influence recommendations, 

    - focus on which metric?
        > 'NONE OF THE METRICS THAT WE DISCUSSED MATTER MORE THAN HOW REAL CUSTOMERS REACT TO RECOMMENDATION YOU PRODUCE IN REAL WORLD!'

        - we must understand the trade-offs between them


1. [Naver Ranking Algorithm](https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=nvr_design&logNo=221567739896)
    - 다중 파라미터 랭킹 알고리즘 &rarr; 둘러보는 탐색에 적합.
        - weighted sum(Affinity, Popularity, Recency)
    - Affinity(계정에 대한 친밀도, 구독 시점 콘텐츠 클릭수 등)
    - Popularity(콘텐츠의 가치, 구독자 조회, 좋아요 수 등)
    - Recency(콘텐츠의 최신성, 콘텐츠 생성 시점, 노출 시점)
    - 해당 알고리즘 적용 후 hit content가 평균 3칸 상단에 노출.

<!-- 추천 시스템 : https://github.com/woowacourse-teams/2021-jujeol-jujeol -->

[wiki/Recommender_system](https://en.wikipedia.org/wiki/Recommender_system)  

[추천 시스템 종류](https://dsbook.tistory.com/334)  
[추천 시스템 기본](https://kmhana.tistory.com/30)  
[추천 시스템 개념 및 알고리즘](https://wooono.tistory.com/135)  
[추천 시스템 개념 상세 설명](https://blog.naver.com/mm323/222838558675)  

[RMSE or MAE](https://towardsdatascience.com/evaluating-recommender-systems-root-means-squared-error-or-mean-absolute-error-1744abc2beac)  

    - asd


추천 시스템 성능 평가 : https://sungkee-book.tistory.com/11

BERT 모델 장점과 파인 튜닝 흐름정리 : https://m.blog.naver.com/antler07/222066071573  
BERT Fine-Tuning Tutorial with PyTorch : https://mccormickml.com/2019/07/22/BERT-fine-tuning/  
when get 'user come in' event, just show most popular item : https://www.quora.com/How-do-you-recommend-to-new-users  

인기도 기반 모델 : https://velog.io/@readymadelife/추천시스템의-인기도-기반-추천

Collaborative Filtering(example code) : https://pub.towardsai.net/recommendation-system-in-depth-tutorial-with-python-for-netflix-using-collaborative-filtering-533ff8a0e444  
상위 k개의 item들의 평균 평점을 활용 collaborative-filtering : https://skifree64.github.io/machine_learning/2019/11/25/collaborative-filtering.html  
ALS RecSys(example code): https://github.com/SJD1882/Big-Data-Recommender-Systems/blob/master/notebooks/MovieLens27M-ALS-Recommender-System.ipynb  
recommendation-with-pytorch(example code) : https://betterprogramming.pub/building-a-recommendation-engine-with-pytorch-d64be4856fe7  


hybrid : https://blog.naver.com/jamesoh0813/222471455189  
7-types-of-hybrid : https://medium.com/analytics-vidhya/7-types-of-hybrid-recommendation-system-3e4f78266ad8  
sparse-datasets-using-hybrid : https://ai.plainenglish.io/how-to-improve-recommendations-for-highly-sparse-datasets-using-hybrid-recommender-systems-1a4366e65cff  
Hybrid Recommender System based on Autoencoders : https://paperswithcode.com/paper/hybrid-recommender-system-based-on  
CBCF(contents booted collaborative filtering) : https://www.cs.utexas.edu/~ml/papers/cbcf-aaai-02.pdf  


real-time recommendation  : https://eugeneyan.com/writing/real-time-recommendations/   
svd 행렬분해 : https://blog.naver.com/pjt3591oo/222646297214  
install error(need microsoft c++) : https://somjang.tistory.com/entry/Python-pip-install-%EC%8B%9C-error-Microsoft-Visual-C-140-is-required-%EC%98%A4%EB%A5%98-%ED%95%B4%EA%B2%B0-%EB%B0%A9%EB%B2%95  


netfliex prize : http://www.shalomeir.com/2014/11/netflix-prize-1/  
NMF : https://medium.com/logicai/non-negative-matrix-factorization-for-recommendation-systems-985ca8d5c16c  
Latent Factor Models : https://blog.naver.com/wlssud132/222811472537  
netflix-recommendations-beyond-the-5-stars : https://netflixtechblog.com/netflix-recommendations-beyond-the-5-stars-part-1-55838468f429


<!-- https://sungkee-book.tistory.com/10 -->


--- 

<!-- https://medium.com/naver-place-dev/naver-g플레이스ai개발-부서의-mlops-kubernetes-기반-1f234d82b238 -->
- MLOps란? rarr; Develpment + Operations를 시작으로 Ops 개념이 확장

    ![image](https://miro.medium.com/max/720/1*O5Wvs__NWtoQjW6cs776Tw.png)
    ![image](https://miro.medium.com/max/1100/1*d0GLPoYeq1zNkEAKKzwfaw.png)
    *<center>Ops(왼쪽) MLOps(오른쪽)</center>*
    
    - 개발의 여로 요소들을 실체화해서 새로운 부분을 지속가능하게 하도록 하는 솔루션을 Ops로 생각한다. 따라서 보통 플랫폼 형태로 구현되고 적용된다.
    - 즉, MLOps는 새로운 요소를 머신러닝 중심으로 봤을 때, 나머지 공통 용소를 MLOps의 관심사로 생각


- HTTP API : HTTP라는 통신 규칙으로 소통하는 API, Method(GET, POST, PUT, DELETE)
    - HyperText Transfer Protocol
    - 클라이언트 - 서버 구조 : 클라이언트 요청이 있을때만 서버에서 응답을 반환. 즉, 단방향 통신/
    - 무상태(Stateless) 프로토콜 지향 : 연결/상태 정보를 보존하지 않는다.
    - 비연결성 : TCP/IP 연결을 끊어 유지하지 않는 것. 새로 연결될때마다 3-handshake에 따른 시간이 추가
    - HTTP Header
        - General 헤더 : 요청 및 응답 메세지 모두에서 공통적으로 사용 가능
        - Entity 헤더 : 내용 길이, 컨텐츠 언어, 인코딩, 만료 날짜 및 기타 중요한 정보와 같은 정보.
    - 요청 헤더
        - Host : 서버 호스트 이름과 포트번호
        - User-agent : 현재 사용자의 클라이언트(OS, 브라우저 포함)
        - Accept : 응답 타입 명시
        - Referer : 바로 직전에 머물렀던 웹 링크 주소.
    - 응답 헤더
        - location, Sever, age, ...
    - 메시지 바디
        - 실제 전송할 데이터를 담는 부분.

- Socket 통신 : Socket이란? 네트워크상에서 동작하는 프로그램 간 통신의 종착점(Endpoint)이다.
    - 클라이언트와 서버 양쪽에서 소로에게 데이터 전달을 하는 방식의 양방향 통신.
    - 보통 스트리밍이나 실시간 채팅 등 실시간으로 데이터를 주고 받아야 하는 경우 자주 맺고 끊는 HTTP 통신보다 소켓 통신이 적합하다. 


- REST API : Respresentational State Transfer, HTTP의 장점을 최대한 활용할 수 있는 아키텍처
    - HTTP와의 정확한 차이점으로 자원의식별, 메세지를통한 리소스 조작, 자기 서술적 메세지, 애플리케이션의 상태에 대한 엔진으로서 하이퍼미디어(HATEOAS)
- Fast API : Python에서 restful API를 개발하기 위한 웹 프레임 워크이다.
<!-- https://www.imaginarycloud.com/blog/flask-vs-fastapi/ -->
- Flask : 웹 프레임워크
- 시간에 제한이 있으면 플라스크, 항상 동작해야하면 fastapi
- Python은 다소 퍼포먼스가 낮은 프로그래밍 언어이기 때문에 성능을 높게 요구하는 애플리케이션에 대해서 많은 고민이 필요. 최적화 같은 경우.