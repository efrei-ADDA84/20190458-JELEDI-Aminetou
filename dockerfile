FROM python:3.8-slim

WORKDIR /app

COPY tp1-devops.py .

RUN pip install requests
RUN pip install flask
RUN pip install jsonify

CMD ["python","tp1-devops.py"]