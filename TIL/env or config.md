> .env file
```
DB관련 정보, API_KEY 등 git, 오픈소스에 올리면 안되는 파일 등.

dotenv 패키지 활용

프로젝트의 최상위 루트에 파일을 만듦.

외부 파일에 환경변수를 정의하여 변수로 받아오면 유지보수에 용이
```

config file
```
configuration(환경 설정)을 줄인말

[config.py](http://config.py) 로 활용 가능
```


configure | configure 스크립트는 개발 중인 프로그램을 각기 다른 수많은 컴퓨터들에서 실행하고 도와주도록 설계된 실행 스크립트이다.
소스 코드로부터 컴파일하기 직전에 사용자 컴퓨터의 라이브러리의 존재 여부를 확인하고 연결시킨다

python에서 .env 파일 사용하기 | [https://blog.gilbok.com/how-to-use-dot-env-in-python/](https://blog.gilbok.com/how-to-use-dot-env-in-python/)
.env 파일이란 | [https://velog.io/@hoho_0815/env-파일에-대하여](https://velog.io/@hoho_0815/env-%ED%8C%8C%EC%9D%BC%EC%97%90-%EB%8C%80%ED%95%98%EC%97%AC)
pip install python-dotenv
.env
MySecret = "I am pretty."
.gitignore에 /.env add
example
from dotenv import load_dotenv
import os

```
# load .env
load_dotenv()
mySecret = os.environ.get('MySecret')

```

self.__
python underscore(_) mean | [https://ebbnflow.tistory.com/255](https://ebbnflow.tistory.com/255), [https://mingrammer.com/underscore-in-python/](https://mingrammer.com/underscore-in-python/)




from dotenv import load_dotenv

# pip install python-dotenv



outer.inner_class => init 함수 실행없이 바로 inner_class 실행
outer().inner_class => outer class init 실행 후 inner_class 실행

pipenv 등 가상환경 venv 실행시 powershell에 (venv) 등이 안나오는경우.
또는, F1 - select interprinter 설정시 해당 인터프린터가 안보일경우
=> 경로설정으로 해결가능. 보통 C:/User/user/.virtualenv/file_name/Script/activate or python 선택으로 (venv) powershell을 띄울수있음

shell이란?
interface, 하드웨어 조작까지 가능한.

vcpkg | win linux, maxos에서 C와 C++의 관리를 도와줌([https://vcpkg.io/en/index.html](https://vcpkg.io/en/index.html))
git clone [https://github.com/Microsoft/vcpkg.git](https://github.com/Microsoft/vcpkg.git)
cd vcpkg
해당 파일에서 bootstrap-vcpkg.bat 실행하면 설치된 폴더에 vcpkg.exe파일이 생성되면
해당 파일을 환경변수 path에 등록을하면 vcpkg사용이 가능.
vcpkg integrate install => vcpkg로 설치된 모든 라이브러리를 추가 작업없이 #include로 바로 사용 가능.