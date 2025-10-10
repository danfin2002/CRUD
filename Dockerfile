FROM python:3.12.6-bookworm

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

RUN pip install --upgrade pip wheel

COPY requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY . .

RUN sed -i 's/\r$//' prestart.sh && \
    chmod +x prestart.sh

EXPOSE 8000

ENTRYPOINT ["./prestart.sh"]

CMD ["python", "main.py"]