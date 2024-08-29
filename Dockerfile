FROM python:3.12-alpine

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY Backend /app/Backend
COPY Frontend /app/Frontend
COPY AI_Service /app/AI_Service
COPY .env /app/.env

# Create uploads directory
RUN mkdir -p /app/uploads

# Expose the port
EXPOSE 3000

# Set working directory for running the app
WORKDIR /app/Backend

# Command to run the application
CMD ["python", "app.py"]
