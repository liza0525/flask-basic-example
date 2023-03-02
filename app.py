# 200 code 관련 된 것만 기본적으로 정리
# 다양한 status code를 통한 통신 예제는 추후 추가

from flask import (
    Flask,
    request,
    render_template
)
from decouple import config

from data.boards import data_dict as board_dict

app = Flask(__name__)
app.config["DEBUG"] = config("DEBUG")

# common
def get_board_data_list():
    return [
        board_info
        for board_info in board_dict.values()
    ]


"""
1. API 정의
- API를 정의 하면, 클라이언트는 서버로부터 원하는 데이터를 받을 수 있습니다.
- sever-side rendering 방식이 아닌 client 프로젝트를 따로 두고 할 경우엔 API endpoint를 정의합니다.
- POST, DELETE 등의 HTML Method를 이용한 예제는 추후에 업데이트 할 예정입니다.
"""
@app.route("/api/boards", methods=["GET"])
def get_board_list():
    # API URL: http://localhost:5000/api/boards
    return {
        "boards": get_board_data_list()
    }, 200


@app.route("/api/boards/<int:board_id>", methods=["GET"])
def get_board_info(board_id):
    # API URL: http://localhost:5000/api/boards/1
    return {
        "board": board_dict[board_id]
    }, 200



"""
2. Page Rendering
- Flask에서는 server-side rendering을 통해 html 페이지를 띄울 수 있습니다.
  - server-side rendering이란: 서버에서 페이지를 그려서 웹으로 보여주는 방식
- 각 html 페이지에 대한 내용은 templates 폴더를 확인하십시오.
- POST, DELETE 등의 HTML Method를 이용한 예제는 추후에 업데이트 할 예정입니다.
"""
@app.route("/page/boards")
def board_list():
    # 페이지 주소: http://localhost:5000/page/boards
    boards =  get_board_data_list()
    return render_template("board/list.html", boards=boards)


@app.route("/page/boards/<int:board_id>")
def board_info(board_id):
    # 페이지 주소: http://localhost:5000/page/boards/1
    board = board_dict[board_id]
    return render_template("board/info.html", board=board)


@app.route("/")
def index():
    # 페이지 주소: http://localhost:5000/
    return render_template("index.html")


# main 함수
if __name__ == "__main__":
    app.run(debug=app.config["DEBUG"])
