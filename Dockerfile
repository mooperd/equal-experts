FROM python
WORKDIR /hello

COPY . /hello

RUN pip install -r requirements.txt

EXPOSE 8080

CMD python hello.py
