FROM python:3.10-slim
WORKDIR /usr/app
COPY . . 
RUN pip install -r requirements.txt
ENV FLASK_APP /usr/app/server.py
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]