## MADA Server — Flask 애플리케이션

간단한 웹 페이지 뷰, 사용자 회원가입, 게시판 저장, 그리고 붓꽃(iris) 품종 예측 API를 제공하는 Flask 기반 서버입니다. 도커/도커 컴포즈를 통해 손쉽게 실행할 수 있으며, 로컬 개발 환경에서도 바로 구동 가능합니다.

---

## 주요 기능

- **뷰 라우트**: `index`, `iris`, `create-user` 페이지 제공
- **AI 예측**: 사전 학습된 로지스틱 모델로 붓꽃 품종 예측
- **사용자 API**: 사용자 조회/저장
- **게시판 API**: 게시글 저장(샘플)

---

## 프로젝트 구조

```text
my-flask/
  app.py
  db.py
  requirements.txt
  Dockerfile
  docker-compose.yml
  ai-models/
    logistic_model-v1.0.0.pkl
  routes/
    ai_route.py
    board_route.py
    user_route.py
    view_route.py
  templates/
    index.html
    iris.html
    create-user.html
  static/
    css/global.css
    js/index.js
    js/iris.js
    js/create-user.js
```

---

## 사전 요구사항

- 로컬 실행: Python 3.12 권장
- 도커 실행: Docker, Docker Compose

Windows에서 로컬 빌드가 어려울 수 있으므로, 가능하면 Docker 사용을 권장합니다.

---

## 빠른 시작

### 1) 로컬 실행 (Windows PowerShell 기준)

```powershell
cd C:\Users\user\Documents\GitHub\MADA_server\my-flask
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -r requirements.txt
python app.py
```

- 기본 포트: `http://127.0.0.1:5000`
- 헬스 체크: `GET /health`

참고: `app.py`의 실행 포트 인자 오타로 인해 로컬 실행 문제가 있을 수 있습니다. 실행이 되지 않으면 Docker/Compose 사용을 권장합니다.

### 2) Docker

```bash
docker build -t my-flask-app .
docker run --rm -p 5000:5000 my-flask-app
```

### 3) Docker Compose

```bash
docker compose up --build
```

- 접속: `http://127.0.0.1:5000`

---

## 환경 설정 및 의존성

- Python 패키지: `requirements.txt`
- Dockerfile은 빌드 시 필요한 `gcc`를 설치하고, 애플리케이션을 `python app.py`로 실행합니다.
- Flask 환경 변수는 Docker/Docker Compose에서 설정됩니다.

### 데이터베이스 연결

`db.py`에 다음과 같이 하드코딩된 접속 정보가 있습니다. 실제 서비스 시 환경 변수로 분리하세요.

```python
db_config = {
    'host': '43.200.6.22',
    'port': 3306,
    'user': 'user',
    'password': '1234',
    'database': 'my_db',
}
```

---

## 라우트 및 API

### 뷰

- `GET /` → `templates/index.html`
- `GET /iris` → `templates/iris.html` (붓꽃 예측 폼)
- `GET /create-user` → `templates/create-user.html` (회원가입 폼)

### 헬스 체크

- `GET /health`

응답 예시

```json
{
  "success": true,
  "massage": "서버정상작동"
}
```

### AI (Iris 예측)

- `POST /ai/predict-iris`

요청 바디

```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

응답 예시

```json
{
  "success": true,
  "message": "setosa 종류의 붓꽃입니다",
  "result": "setosa"
}
```

간단 테스트 (PowerShell)

```powershell
curl -Method POST "http://127.0.0.1:5000/ai/predict-iris" -ContentType "application/json" -Body '{
  "sepal_length":5.1,
  "sepal_width":3.5,
  "petal_length":1.4,
  "petal_width":0.2
}'
```

### 사용자 API

- `GET /user/list` → 사용자 목록 조회
- `POST /user/save` → 사용자 저장

요청 바디 예시

```json
{
  "id": "test01",
  "pw": "pass1234",
  "nick": "닉네임",
  "addr": "서울시 …"
}
```

응답 예시

```json
{ "success": true, "message": "회원가입 완료" }
```

### 게시판 API (샘플)

Blueprint 프리픽스(`/board`)와 라우트(`/board`)가 중복되어 실제 경로는 다음과 같습니다.

- `POST /board/board`

요청 바디 예시

```json
{ "title": "제목", "content": "내용" }
```

응답: `"board saved"`

---

## 정적 자원 및 프론트 동작

- `static/js/iris.js`: Iris 예측 폼에서 `/ai/predict-iris`로 AJAX 요청
- `static/js/create-user.js`: 회원가입 폼 유효성 검증 및 `/user/save`로 AJAX 요청
- `static/js/index.js`: 데모 알림

---

## 자주 발생하는 이슈

- 로컬에서 C/C++ 빌드 도구가 없어 `scikit-learn` 설치에 실패할 수 있습니다. 이 경우 Docker 사용을 권장합니다.
- `app.py`의 실행 포트 인자 오타로 로컬 실행이 실패할 수 있습니다. 문제가 있을 경우 Docker/Compose 사용 또는 포트 인자 수정이 필요합니다.

---

## 라이선스

프로젝트 내 포함된 모델 및 외부 라이브러리의 라이선스 정책을 준수하세요.


