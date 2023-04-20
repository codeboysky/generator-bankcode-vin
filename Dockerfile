FROM python:3.7
COPY ./generator_info /apps
RUN pip install -r requirements.txt
WORKDIR /apps/generator_info
CMD ["python","manage.py","runserver","8000"]