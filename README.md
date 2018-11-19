# 스냅 사진 마켓 서비스  -by lambmukja(a.k.a 사진찍을고양)

## 개발방법

### 1. pyenv 설치 및 python 가상환경 설정
```bash
$ curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash

# 로컬에 설치 후 맨 마지막 세 줄에 있는걸 .bashrc에 추가하고 .bashrc 실행
```
* pyenv 설치가 잘 안된다면 다음을 참고
    * https://github.com/pyenv/pyenv/wiki/Common-build-problems

```bash
$ pyenv install 3.6.5
$ pyenv virtualenv 3.6.5 [자신이 원하는 이름] #ex) 3.6.5-snap
$ pyenv local [자신이 선택한 이름]
```

### 2. requirements.txt 설치
```bash
$ pip install -r requirements.txt
```

### 3. settings.py 받기
* settings.py는 보안상 이슈때문에 github에 올려놓지 않았으니 말해서 받을 것


### 4. git hook 추가
code convention을 맞추기 위해 자신의 git 프로젝트 폴더 안 .git/hooks/pre-commit 파일에 아래 내용을 넣을 것

```sh
#!/bin/sh
FILES=$(git diff --cached --name-only --diff-filter=ACM | grep -e '\.py$')
if [ -n "$FILES" ]; then
    flake8 $FILES
fi
```
