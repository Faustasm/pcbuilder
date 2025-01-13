
FROM python:3.9.12-slim

WORKDIR /pcbuilder_client

RUN apt-get update && apt-get install -y npm
COPY . /pcbuilder_client
RUN npm install
CMD ["npm", "run", "serve"]
EXPOSE 8080