FROM python:3.12-slim

RUN useradd --create-home --uid 10001 appuser
WORKDIR /app

COPY app ./app
COPY requirements.txt .

USER 10001
EXPOSE 8080
ENV PORT=8080
CMD ["python", "-m", "app.server"]