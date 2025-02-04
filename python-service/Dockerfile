# Use official Python image
FROM python:3.9

# Set working directory inside the container
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the files
COPY . .

# Expose port 7000
EXPOSE 7000

# Run the application
CMD ["python", "app.py"]

