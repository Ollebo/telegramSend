from alpine



#Install python3
RUN apk add python3




# Setup req

COPY req.txt /req.txt
RUN pip3 install -r /req.txt

WORKDIR /code
COPY . /code/

CMD ["python3","-u","getWorks.py"]