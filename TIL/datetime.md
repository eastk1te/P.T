### Datetime

```python

# ======================================================================================================
# datetime striptime 표현식 : https://docs.python.org/ko/3/library/datetime.html#strftime-and-strptime-format-codes
# import datetime

# KST = datetime.timezone(datetime.timedelta(hours=9))

# today = datetime.datetime.now(tz=KST)
# from1 = datetime.datetime(today.year, today.month, today.day, today.hour, today.minute, today.second, tzinfo=KST)
# print(today.day)

# from2 = datetime.datetime.strftime(today, '%m%d_%H')
# print(from2)

# 시간 관련 작업을 하신다면 아래 사항을 꼭 기억해주세요.
# 시간대를 명시합시다.
# 시각을 애플리케이션 로직이나 데이터베이스에서 저장할 때는 UTC로 사용하고, 유저에게 표시할 때만 유저의 시간대로 변환하여 보여주도록 합시다.    
# 백엔드 서버끼리 통신할 때도 항상 UTC를 사용한다는 가정을 하면, 시간대가 없더라도 robust하게 처리할 수 있습니다.
# (robustness is the ability of a computer system to cope(대처,대응하다) with errors during execution(실행))
```