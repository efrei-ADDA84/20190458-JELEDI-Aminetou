FROM python:3.8-slim

WORKDIR /app

COPY tp2-devops.py .

RUN pip install requests
RUN pip install flask
RUN pip install jsonify

CMD ["python","tp2-devops.py"]