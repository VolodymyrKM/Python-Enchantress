FROM python:3
EXPOSE 5000
COPY . /opt/service
WORKDIR /opt/service
RUN pip install -r requirements.txt
RUN /usr/local/bin/python -m pip install --upgrade pip

CMD ["python", "app.py"]