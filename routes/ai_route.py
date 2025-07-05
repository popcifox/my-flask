import joblib
from flask import Blueprint, jsonify, request

ai_bp = Blueprint('ai', __name__)

model = joblib.load('ai-models/logistic_model-v1.0.0.pkl')

#붓꽃 예측 함수
def predict_iris(sepal_length, sepal_width, petal_length, petal_width):
    y_pred = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
    iris_types = y_pred[0]
    result = ''
    if iris_types == 0:
        result = 'setosa'
    elif iris_types == 1:
        result = 'versicolor'
    else:
        result = 'virginica'
    return result


@ai_bp.route('/predict-iris', methods=['POST'])
def ai_test():
    data = request.get_json()
    #받침 길이
    sepal_length = float(data.get('sepal_length'))
    #받침 너비
    sepal_width = float(data.get('sepal_width'))
    #꽃잎 길이
    petal_length = float(data.get('petal_length'))
    #꽃잎 너비
    petal_width = float(data.get('petal_width'))
    
    iris = predict_iris(sepal_length, sepal_width, petal_length, petal_width)

    return jsonify({
        'success' : True,
        'message' : f'{iris} 종류의 붓꽃입니다',
        'result' : iris
    })
