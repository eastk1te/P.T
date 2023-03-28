```python
from flask import Flask, jsonify, current_app

# https://flask-docs-kr.readthedocs.io/ko/latest/patterns/fileuploads.html
def run_app(data):
    app = Flask(__name__)
    # route는 url 방문할때 준비된 함수가 트리거 되도록 바인딩하기 위한 데코레이터
    # 즉 해당 url 방문시 upload json 함수 실행
    @app.route("/")
    def upload_json():
        app = Flask(__name__)
        app.config['JSON_AS_ASCII'] = False

        with app.app_context():
            print(app.app_context)

        return jsonify(data) # data to json file 
        
    # https://growingsaja.tistory.com/299
    # if use korean lang, json.dumps use
    with app.app_context():
        print(current_app.name) 

    # default encoding is ascii but use this code make utf-8 encoding
    app.config['JSON_AS_ASCII'] = False # jsonify can korean use
    app.run()


if __name__ == "__main__":
    run_app({'a':1})
```

### ready to flask
 - Flask : micro web framework(micro : 한개의 .py로 작성 가능), 간결하게 유지 및 확장 가능
 - Django는 덩치가 큰 프레임 워크, 그에 반해 flask는 가벼워 확장 모듈을 활용해 개발

```python
# Python tutorial Flask : https://pythonbasics.org/what-is-flask-python/
# Flask ORM : https://daimhada.tistory.com/134
# flask, request 통신
# https://mooneegee.blogspot.com/2017/10/python-flask-http-get-post.html
# https://justkode.tistory.com/9
# https://sagittariusof85s.tistory.com/266


# in terminal
#curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
# python3 get-pip.py

#pip install flask

from flask import Flask
app= Flask(__name__)

@app.route('/')
def hello():
    return 'Hello'

if __name__ == '__main__':
    app.run()

# https://wikidocs.net/81510 : wikidocs flask
# c:\venvs dir env 생성
cd \ 
mkdir venvs
cd venvs

# python 가상환경 실행
python -m venv myproject
virualenv myproject
# -m venv(python module venv use), myproject(dir name)

# pip cmd, terminal 환경에서 사용이 안될 떄
pip 환경 변수 설정
pip install --upgrade pip


# 가상환경 진입 및 flask install
cd C:\venv\myproject\Scripts activate
deactivate
pip install flask

# pip 최신 버전
python -m pip install --upgrade pip

#  .cmd file 로 설정하면 매번 입력할 필요 없음
.cmd 확장자(배치 파일)
pip install pybo

@echo off
cd c:/projects/myproject
set FLASK_APP=pybo
set FLASK_ENV=development
c:/venvs/myproject/scripts/activate

## 기초 공사
├── pybo/
│      ├─ __init__.py
│      ├─ models.py         # 데이터 베이스 처리
│      ├─ forms.py          # 서버로 전송된 폼을 처리
│      ├─ views/            # 화면 구성 디렉터리
│      │   └─ main_views.py 
│      ├─ static/           #CSS, JavaScript, image file 저장 static dir
│      │   └─ style.css
│      └─ templates/        # HTML 파일 
│            └─ index.html
└── config.py               # pybo project 환경 설정 

from flask import Flask
from flask import Blueprint
bp = Blueprint('main', __name__, url_prefix='/')
@bp.route('/')



def create_app():           # 애플리케이션 팩토리
    # 전역으로 사용시 순환참조(circular import) 오류가 대표적
    app = Flask(__name__)       # 그래서 application factory 사용으로 예방
    # pybo.py file -> /pybo/__init__.py file open then def create_app make (create_app = aplication factory, 내부 정의 함수명)

    
    @app.route('/') # 애너테이션 url mapping func
    # if use bluepring, can manage route func effiecally and manage url and func mapping tool(class) in flask
    from .views import main_views
    app.register_blueprint(main_views.bp)

    def hello_pybo():
        return 'Hello, Pybo!'
    
    return app

# if main.py file을 server에서 실행시켜 놓으면 계속 업데이트가 됨.
from flask import Flask, jsonify, current_app

# https://flask-docs-kr.readthedocs.io/ko/latest/patterns/fileuploads.html
def run_app(data):
    app = Flask(__name__)
    # route는 url 방문할때 준비된 함수가 트리거 되도록 바인딩하기 위한 데코레이터
    # 즉 해당 url 방문시 upload json 함수 실행
    @app.route("/")
    def upload_json():
        app = Flask(__name__)
        app.config['JSON_AS_ASCII'] = False

        with app.app_context():
            print(app.app_context)

        return jsonify(data) # data to json file 
        
    # https://growingsaja.tistory.com/299
    # if use korean lang, json.dumps use
    with app.app_context():
        print(current_app.name) 

    # default encoding is ascii but use this code make utf-8 encoding
    app.config['JSON_AS_ASCII'] = False # jsonify can korean use
    app.run()
```