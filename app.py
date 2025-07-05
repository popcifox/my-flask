from flask import Blueprint, Flask, render_template, request
from routes.board_route import board_bp
from routes.view_route import view_bp
from routes.user_route import user_bp
from routes.ai_route import ai_bp

app = Flask(__name__)

#블루프린트 등록
app.register_blueprint(view_bp,url_prefix='/')
app.register_blueprint(user_bp,url_prefix='/user')
app.register_blueprint(board_bp,url_prefix='/board')
app.register_blueprint(ai_bp,url_prefix='/ai')

@app.route('/')
def index():
    return render_template('index.html')




if __name__ == '__main__':
    app.run(debug=True)
