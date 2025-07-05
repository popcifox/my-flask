from flask import Blueprint, request

board_bp = Blueprint('board_bp', __name__ )
#게시글 저장
@board_bp.route('/board', methods=['POST'])
def save_board():
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')
    print(title)
    print(content)

    return "board saved"