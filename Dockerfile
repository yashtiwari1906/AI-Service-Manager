FROM python:3.9
COPY . /app/ 
#you need to keep this different from port of application I guess this is port on which docker container is exposed
EXPOSE 8000 
WORKDIR /app/ 
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
ENV ENV="production"
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y  && pip install --upgrade pip && pip install -r requirements.txt
CMD ["python",  "manage.py", "runserver", "0.0.0.0:5050"] 