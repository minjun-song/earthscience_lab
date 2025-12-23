# 별의 일주운동 시뮬레이터

## 프로젝트 목적
- 중학생 및 영재학생을 위한 별의 일주운동 시뮬레이터로, 지구 자전과 천구 회전, 관측자 시점을 직관적으로 이해하도록 돕습니다.

## 사용 기술
- Three.js, HTML, Streamlit

## 실행 방법
1) `pip install -r requirements.txt`
2) `streamlit run app.py`

## GitHub 저장소 구조
- `simulator/index.html`: Three.js로 구현된 별의 일주운동 시뮬레이션 단일 HTML 파일
- `app.py`: Streamlit 앱 진입점. `simulator/index.html`을 읽어 iframe 형태로 렌더링하여 Streamlit Cloud에서도 실행 가능
- `requirements.txt`: Streamlit 실행에 필요한 기본 패키지 목록
- `README.md`: 프로젝트 개요와 실행 방법 안내
