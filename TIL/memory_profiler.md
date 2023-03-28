memory 1.5G 가량 차지해서 적어도 300~500까지 낮춰야함.

파이썬 메모리 최적화
memory_profiler로 line by line memory usage 확인 가능.
왜 메모리를 절약해야할까? -> 자원 소모, 빅데이터를 다룰때면 성능이 떨어짐, 캐싱이나 램에 저장이 불가능하기떄문.

from memory_profiler import profile
@profile
def x():

python -m memory_profiler [example.py](http://example.py/)


from memory_profiler import profile
@profile