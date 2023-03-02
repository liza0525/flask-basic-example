# Flask Example
> Flask를 시작하는 사람들을 위한 예제 사이트를 만듭니다.


## 📚directory 구조
```
flask-bagic-example
ㄴ data
    ㄴ boards.py
ㄴ templates
    ㄴ board
        ㄴ info.html
        ㄴ list.html
    ㄴ index.html
ㄴ app.py
ㄴ .env
ㄴ requirements.txt
```
### 설명
- `data`(폴더) : DB를 대체할 데이터를 정의합니다.
    - `boards.py`: 게시판 데이터를 dictionary 형태로 저장했습니다.
- `templates`(폴더): html 페이지를 정의합니다.
    - `board`(폴더)  : 게시판 페이지 관련된 html 파일을 모아두었습니다.
        - `info.html`: 게시판 하나에 대한 페이지입니다.
        - `list.html`: 게시판 리스트에 대한 페이지입니다.
    - `index.html`: 해당 프로젝트의 첫 페이지입니다.
- `app.py`: API와 page rendering url 등을 정의하고, 서버를 실행시키는 코드가 있습니다.
- `.env`: 서버 실행 전에 주요 정보 등을 모아두는 환경설정 파일입니다.
- `requirements.txt`: 서버를 실행하기 전, 필요한 python package를 모아두었습니다.


## 💻실행 방법
0. 해당 레포지토리를 클론합니다.
    ```sh
    git clone [git repository url]
    ```
1. 가상환경을 만듭니다. 가상 환경을 만드는 방법은 여러가지지만 다음을 이용하면 됩니다.
  - pyenv
  - anaconda

2. requirements.txt에 있는 package를 설치합니다
    ```sh
    > pip install -r requirements.txt
    ```

3. 다음 명령어를 통해 `.env.default` 파일을 `.env`로 복사한 후, 환경설정 값을 세팅합니다.
    ```sh
    > cp .env.default .env
    ```

4. 서버를 실행합니다.
    ```shell
    > python app.py
    ```
5. html 페이지로 예제가 돌아가는 모습을 확인하고 싶다면, chrome 등의 브라우저를 통해 다음 주소에 접속합니다.
    ```
    http://127.0.0.1:5000/
    또는
    http://localhost:5000/
    ```

## 📌Version 정보
### ver0.0.1
#### Boards
- DB 없이 예제 데이터로 게시판 페이지를 구현할 수 있도록 합니다.
- GET method와 flask template rendering에 대한 내용을 추가합니다.
