FROM python:3.10

COPY data_client/requirements.txt .
RUN pip3 install -r requirements.txt

COPY data_client/ ./
CMD [ "python3", "client.py" ]