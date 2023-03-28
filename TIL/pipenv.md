pipenv install [library]
pipenv uninstall [library] => uninstall 진행해도 pipfile은 변화가 없음, 왜??
그래서 pipfile에서 불필요한 library 직접 제거하고 pipenv --rm 후 다시 pipenv install의 형식으로 진행해야함.
pipenv 가 실행중이면 exit로 종료 가능.
pipenv run python example.py로 가상환경에서 실행가능.

pipenv가 안좋은게 install 시 이름이 다르면 install이 안됨. 위에 같은 경
pipenv 환경변수 지정.
https://hoohaha.tistory.com/92
activate 시 왼쪽에 가상환경 실행됨.