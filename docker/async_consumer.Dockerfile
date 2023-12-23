FROM dracarys2000/service-manager:v1.1
COPY . /app/docker/
#you need to keep this different from port of application I guess this is port on which docker container is exposed
EXPOSE 8000 
WORKDIR /app/ 
# RUN python -m venv /opt/venv
# ENV PATH="/opt/venv/bin:$PATH"
# ENV ENV="minikube"
# RUN apt-get update
# RUN apt-get install ffmpeg libsm6 libxext6  -y  && pip install --upgrade pip && pip install -r ../requirements.txt
# ENV CELERY_BROKER_URL="redis://test-redis:6379"
# ENV CELERY_RESULT_BACKEND="redis://test-redis:6379"
CMD ["python", "-m", "celery", "-A", "ai_service_manager", "worker"] 


