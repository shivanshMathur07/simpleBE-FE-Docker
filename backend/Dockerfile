FROM python:3-alpine
WORKDIR /app
ADD requirements.txt /app/requirements.txt
ADD .env /app/.env
COPY utils /app/utils
ADD app.py /app/app.py
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]