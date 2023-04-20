FROM python:3.7
RUN /apps
COPY ./generator_info /apps
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple some-package
WORKDIR /apps/generator_info
CMD ["python","manage.py","runserver","8000"]