
FROM python:3.9.12-slim

WORKDIR /pcbuilder_server


COPY . /pcbuilder_server    
RUN pip install -r requirements.txt
CMD ["flask", "run", "--host=0.0.0.0"]
EXPOSE 5000