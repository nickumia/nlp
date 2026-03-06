FROM python:3.11-slim

ARG USER_ID=1000
ARG GROUP_ID=1000

RUN groupadd -g ${GROUP_ID} appuser && \
    useradd -u ${USER_ID} -g ${GROUP_ID} -m appuser

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY data/ ./data/
COPY scripts/ ./scripts/

RUN mkdir -p output && chown -R appuser:appuser /app

USER appuser

CMD ["python", "scripts/render_graph.py"]
