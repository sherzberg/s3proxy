FROM sherzberg/python-all-dev

WORKDIR /app

ADD requirements.txt /app/requirements.txt
RUN python3.4 -m ensurepip
RUN pip3.4 install -r requirements.txt

ADD . /app

ADD .git/refs/heads/master /app/version

EXPOSE 5000

CMD python3.4 app.py
