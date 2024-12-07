FROM python:3.11-alpine

WORKDIR /api

# 이미지 레이오 캐시 떄문에 의존성 설치에 필요한 부분을 먼저 복사한다.
COPY ./api/requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY ./api ./api

EXPOSE 80

CMD ["fastapi", "run", "api/main.py", "--port", "80"]