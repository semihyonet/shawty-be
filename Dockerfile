# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any necessary dependencies
RUN pip install poetry

# Install the dependencies
RUN poetry install --no-dev

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV PYTHONUNBUFFERED=1

# Run uvicorn server with the FastAPI app
CMD ["poetry", "run","uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
