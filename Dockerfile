#base image
FROM python:3.8 as builder

COPY requirements.txt .

run pip install --upgrade pip

#install all dependencies
RUN pip install --user -r requirements.txt

#second unnamed stage
FROM python:3.8-slim

#copy only the dependency installation from the 1st image
COPY --from=builder /root/.local /root/.local

#set environment var
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#copy whole project to home directory.
COPY ./todo /home 

#update the PATH env variable
ENV PATH=/root/.local:$PATH

#port where django runs
EXPOSE 8000

WORKDIR /home
#start server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
