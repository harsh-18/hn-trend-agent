FROM python:3.11-slim
WORKDIR /app
RUN pip install --no-cache-dir google-adk toolbox-core
COPY hn_agent/ ./hn_agent/
EXPOSE 8080
CMD ["adk", "api_server", "--host=0.0.0.0", "--port=8080", "."]
