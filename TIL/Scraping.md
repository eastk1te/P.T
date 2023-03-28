
합법적으로 스크래핑 하는 법.
https://yozm.wishket.com/magazine/detail/877/
https://brunch.co.kr/@8d1b089f514b4d5/35 

- 스크래핑 합법과 불법의 경계
    
    [합법적으로 '웹 크롤링'하는 방법 (下)](https://brunch.co.kr/@8d1b089f514b4d5/35)
    
    [합법적으로 '웹 크롤링'하는 방법 (上) | 요즘IT](https://yozm.wishket.com/magazine/detail/877/)


- 크롤링 법적 문제
    1. [사람인vs잡코리아](http://news.bizwatch.co.kr/article/mobile/2017/09/27/0023) (2017년 판결)
    2. [야놀자vs여기어때](https://www.lawtimes.co.kr/Legal-News/Legal-News-View/Content/Article?serial=178683) (2022년 판결)
    3. [크롤링-불법인지 합법인지 애매모호](https://biz.chosun.com/site/data/html_dir/2020/09/23/2020092300325.html)
    4. [robot.txt는 강제성이 아니라 권고이다.](https://imcreator.tistory.com/102)
    
    [크롤링, 어디까지 할 수 있을까](https://www.venturesquare.net/861831)
    
- [Selenium](https://coding-kindergarten.tistory.com/151) **으로 개발했으나, 비추천한다.** 
Selenium은 RAM, CPU를 많이 사용하는 무거운 라이브러리이다.
한번에 많은 드라이버를 구동하면 RAM과 CPU 초과로 자동으로 종료된다.
많은 양의 데이터를 수집할때는 Selenium 사용을 비추천 한다. 
→ 다른 가벼운 크롤링 툴을 사용하거나 , 리눅스 기반에서도 크롤링을 할 수 있다.
- **IP 차단 문제와 해결법**
5시간 정도 크롤링을 진행하면 , IP가 해당사이트에서 사용하지 못하게 막혀버린다. 
그래서 핸드폰의 핫스팟을 이용했다. 비행기모드 킨 후 다시 핫스팟을 실행하면 핸드폰 핫스팟 IP가 바뀐다. 핫스팟을 5시간 주기로 껐다가 켰다가 반복하면서 크롤링을 작업했었다.

상황이 바뀐 건  22년 1월. 통신사 (SKT, KT, LG) 모두 무제한 핫스팟 서비스를 없앴다. 핫스팟 30~50 기가만 제공으로 서비스를 바뀌었다.  네이버 크롤링을 진행하려면, 300기가 넘은 시점에서 더 이상 같은 방법으로 크롤링을 할 수 없었다.

생각해낸 방법은, Galaxy s10e 기준으로, 와이파이를 틀어놓고, 핫스팟을 틀 수 있었다. 무제한으로 사용이 가능해 보이나 단점은 데이터 전송속도가 일반 핸드폰의 핫스팟보다 느렸다는 점이다.
- **스크래핑시 시크릿  모드 option**
구글 크롬 드라이버를 기준으로, 시크릿 모드를 하면 2가지 장점이 있다.
1. 상대방 웹사이트 관리자로 부터 내가 크롤링한 기록을 최대한 감출 수 있다. 
2. 드라이버가 기록을 저장하지 않아, RAM 사용을 줄일 수 있다. (크롤링 드라이버가 기록을 저장했을 때 보다, 가벼워 진다.)
- **작업 시작 전 검증(특히 크롤링 등 작업 소요 시간이 오래 걸릴 경우)**
⇒ 단위 테스트를 많이 실행 해봐야 한다.
⇒ 실 사례: 크롤링 전 시크릿 모드 활성화 놓침
⇒ 피해: 웹사이트에 300GB  분량 크롤링한 데이터 기록을 남기다
- [selenium warning undisplay](https://stackoverflow.com/questions/4744968/how-to-suppress-console-error-warning-info-messages-when-executing-selenium-pyth)


### url encoding & decoding
```python
# ======================================================================================================
# from urllib.parse import urlparse
# import urllib
# 'https://ko.wiktionary.org/w/index.php?title=' + urllib.parse.quote("") + '&from=' + urllib.parse.quote('가')
#>>> '%EC%95%88%EB%85%95%ED%95%98%EC%84%B8%EC%9A%94

#urllib.parse.unquote("https://ko.wiktionary.org/w/index.php?title=%EB%B6%84%EB%A5%98:%ED%95%9C%EA%B5%AD%EC%96%B4_%EA%B4%80%ED%98%95%EC%82%AC%ED%98%95(%ED%98%95%EC%9A%A9%EC%82%AC)&from=%EA%B0%80")
#>>> '안녕하세요'
```