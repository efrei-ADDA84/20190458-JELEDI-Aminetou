FROM python:3.8-slim

WORKDIR /app

COPY tp1-devops.py .

RUN pip install requests

CMD ["python","tp1-devops.py"]