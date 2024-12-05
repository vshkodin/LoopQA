# Use an official Python base image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PIP_NO_CACHE_DIR=1

# Install required system packages
RUN apt-get update && apt-get install -y \
    curl \
    gnupg \
    git \
    unzip \
    libnss3 \
    libatk1.0-0 \
    libx11-xcb1 \
    libxcomposite1 \
    libxcursor1 \
    libxdamage1 \
    libxrandr2 \
    libasound2 \
    libpangocairo-1.0-0 \
    libgtk-3-0 \
    libgbm1 \
    libpangoft2-1.0-0 \
    libharfbuzz-icu0 \
    libgl1 \
    fonts-liberation \
    && rm -rf /var/lib/apt/lists/*

# Install Playwright and its browsers
RUN pip install --upgrade pip
RUN pip install playwright
RUN playwright install --with-deps

# Install Allure
RUN curl -o allure.zip -L https://github.com/allure-framework/allure2/releases/download/2.21.0/allure-2.21.0.zip && \
    unzip allure.zip -d /opt/allure && \
    rm allure.zip && \
    ln -s /opt/allure/bin/allure /usr/local/bin/allure

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port for running tests or serving Allure reports if needed
EXPOSE 8080

# Define the default command
CMD ["pytest", "tests/test_ui.py", "--alluredir=allure-results"]
