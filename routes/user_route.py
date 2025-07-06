from flask import Blueprint, request,jsonify
from db import get_connection

user_bp = Blueprint('user', __name__)

#라우트 /user

#회원 조회
@user_bp.route('/list',methods=['GET'])
def get_user_list():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        sql = "SELECT * FROM user"
        cursor.execute(sql)
        users = cursor.fetchall()
        print(users)
        return jsonify({
            'success':True,
            'message':'회원 조회 완료',
            'data':users
        })
    except Exception as e:
        print(e)
        return jsonify({
            'success':False,
            'message':'회원 조회 실패'
        })
    finally:
        conn.close()



#회원 저장
@user_bp.route('/save',methods=['POST'])
def save_user():
    data = request.get_json()
    id = data.get('id')
    pw = data.get('pw')
    nick = data.get('nick')
    addr = data.get('addr')

    try:
        conn = get_connection()
        cursor = conn.cursor()
        sql = "INSERT INTO user (id,pw,nick,address,created_at) VALUES (%s,%s,%s,%s,sysdate())"
        cursor.execute(sql,(id,pw,nick,addr))
        conn.commit()
        return jsonify({
            'success':True,
            'message':'회원가입 완료'
        })
    except Exception as e:
        print(e)
        return jsonify({
            'success':False,
            'message':'회원가입 실패'
        })
    finally:
        conn.close()