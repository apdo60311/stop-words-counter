FROM python:latest
ADD stop_words_remover.py .

COPY . .

RUN pip install nltk

CMD ["python", "./stop_words_remover.py"] 
# Or enter the name of your unique directory and parameter set.