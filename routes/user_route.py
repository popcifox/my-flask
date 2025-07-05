from flask import Blueprint, jsonify, request

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/user', methods=['GET', 'POST'])
def save_user():
    user_id = request.args.get('id')
    user_pw = request.args.get('pw')

    return jsonify({
        'success' : True,
        'message' : '연결완료',
        'data': {
            'id' : user_id,
            'pw' : user_pw
        }
    })
