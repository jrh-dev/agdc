FROM python:3.12-slim

WORKDIR /app

copy . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8012

CMD streamlit run Home.py  --server.port 8012