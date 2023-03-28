<!-- python ray, 병렬처리 라이브러리 -->
https://zzsza.github.io/mlops/2021/01/03/python-ray/


ray

pip install [https://s3-us-west-2.amazonaws.com/ray-wheels/latest/ray-3.0.0.dev0-cp310-cp310-win_amd64.whl](https://s3-us-west-2.amazonaws.com/ray-wheels/latest/ray-3.0.0.dev0-cp310-cp310-win_amd64.whl)
import ray

### Multiprocessing
```python
# python Thread : http://pythonstudy.xyz/python/article/24-%EC%93%B0%EB%A0%88%EB%93%9C-Thread
# ======================================================================================================
# pip install multiprcess
# import multiprocessing

# def square(x):
#   return x*x
  
# if __name__ == '__main__':
#   # Pool 객체 초기화
#   pool = multiprocessing.Pool()
#   #pool = multiporcessing.Pool(processes=4)
  
#   # Pool.map
#   inputs = [0, 1, 2, 3, 4]
#   outputs = pool.map(square, inputs)
  
#   print(outputs)
  
#   # Pool.map_async
#   outputs_async = pool.map_async(square, inputs)
#   outputs = outputs_async.get()
  
#   print(outputs)
  
#   # Pool.apply_async
#   results_async = [pool.apply_async(square, [i]) for i in range(100)]
#   results = [r.get() for r in results_async]
  
#   print(results)

# # multiprocessing error : SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
# # .py file name을 multuprocessing.py 로 지어서 오류났었음.

# import time
# from multiprocessing import Pool
# from tqdm import tqdm

# def func(x):
#     print(x)    
#     return 

# pool = Pool()

# total = 10
# with tqdm(total=total) as pbar:
#     for _ in tqdm(pool.map(func, range(total), pm_pbar=True)): # pm_pbar=True, progress bar
#         print('for complete.')
#         pbar.update()
# pool.close()
# pool.join()

# Pool 객체 초기화
# pool = multiprocessing.Pool(2)
# print('pool is completed.')
# pool = multiporcessing.Pool(processes=4)
# Pool.apply_async
# results_async = [pool.apply_async(to_lonlat, [i]) for i in tqdm(sever_df.address)]
# results = [r.get() for r in results_async]
# print(results)

# http://pythonstudy.xyz/python/article/24-%EC%93%B0%EB%A0%88%EB%93%9C-Thread
```