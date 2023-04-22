FROM python:3.7
COPY ./generator_info/ ./templates/ ./tools/ ./view/ ./manage.py ./requirements.txt /apps/generator_info/
WORKDIR /apps/generator_info
RUN pip install -r requirements.txt
CMD ["python","manage.py","runserver","8000"]