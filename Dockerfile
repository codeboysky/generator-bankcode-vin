FROM python:3.7
COPY ./generator_info /apps/generator_info/
WORKDIR /apps/generator_info
RUN pip install -r requirements.txt
CMD ["python","manage.py","runserver","0.0.0.0:8000"]