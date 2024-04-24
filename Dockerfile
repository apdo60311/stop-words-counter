FROM python:latest

WORKDIR /app

COPY . .

RUN pip install nltk
 

CMD ["python", "./app/stop_words_remover.py"] 
