# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements first
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy remaining files
COPY . .

# Expose port (if it's a web app)
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
