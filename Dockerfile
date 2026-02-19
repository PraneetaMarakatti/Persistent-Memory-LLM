# -----------------------------
# Base Image
# -----------------------------
FROM python:3.11-slim

# -----------------------------
# Working Directory
# -----------------------------
WORKDIR /app

# -----------------------------
# Install system dependencies
# -----------------------------
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    && rm -rf /var/lib/apt/lists/*

# -----------------------------
# Copy Requirements First
# (Better caching)
# -----------------------------
COPY requirements.txt .

# -----------------------------
# Install Python Packages
# -----------------------------
RUN pip install --no-cache-dir -r requirements.txt

# -----------------------------
# Copy Entire Project
# -----------------------------
COPY . .

# -----------------------------
# Expose Ports
# -----------------------------
EXPOSE 8000
EXPOSE 8501

# -----------------------------
# Start BOTH Backend + UI
# -----------------------------
CMD bash -c "uvicorn backend.api:app --host 0.0.0.0 --port 8000 & streamlit run ui/streamlit_app.py --server.port 8501 --server.address 0.0.0.0"
