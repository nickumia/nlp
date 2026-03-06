FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY data/ ./data/
COPY scripts/ ./scripts/

RUN mkdir -p output

CMD ["python", "scripts/render_graph.py"]
