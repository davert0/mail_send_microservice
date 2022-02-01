FROM python:3

#environment variable to send application output to terminal without buffering
ENV PYTHONUNBUFFERED 1

#setting working directory and importing source code
RUN mkdir /code
WORKDIR /code
COPY . /code/

#installing requirements
RUN pip install -r requirements.txt