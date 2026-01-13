# Base image
FROM mcr.microsoft.com/devcontainers/python:3.13-bookworm

# Install system dependencies needed by Chromium
RUN apt-get update && apt-get install -y \
    libnss3 \
    libatk-bridge2.0-0 \
    libx11-xcb1 \
    libxcomposite1 \
    libxcursor1 \
    libxdamage1 \
    libxrandr2 \
    libgbm1 \
    libasound2 \
    libpangocairo-1.0-0 \
    libcups2 \
    libxss1 \
    libgtk-3-0 \
    libdbus-1-3 \
    curl \
    wget \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /workspaces/property-scraper

RUN echo "PWD inside build is:" && pwd
RUN echo "Files at build context root:" && ls -la /
RUN echo "Files in current workdir:" && ls -la .
RUN echo "Searching for requirements.txt..." && find / -maxdepth 3 -name requirements.txt 2>/dev/null || true

# Copy requirements
COPY requirements.txt requirements.txt

# Install Python dependencies
RUN pip install --upgrade pip \
    && pip install -r requirements.txt \
    && pip install --upgrade playwright \
    && playwright install chromium

# Default command
CMD [ "bash" ]
