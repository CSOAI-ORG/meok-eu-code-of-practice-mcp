FROM meok/mcp-base:latest
COPY . /app
WORKDIR /app
RUN pip install --no-cache-dir fda-samd-mcp==1.0.0
EXPOSE 8081
HEALTHCHECK --interval=30s --timeout=5s --retries=3 \
  CMD curl -fsS http://localhost:8081/healthz || exit 1
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8081"]
