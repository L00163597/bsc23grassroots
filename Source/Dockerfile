# Use the official Python image as the base image
# Must update this value to be latest version of Python: 3.12
FROM python:3.9

# Set environment variables to non-interactive mode and unbuffered Python output
ENV PYTHONUNBUFFERED 1
ENV DEBIAN_FRONTEND noninteractive

# Set the working directory in the container
WORKDIR /app

# Copy the project's requirements.txt and install dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copy the Django project source code to the container
COPY . /app/

# Expose the port that the Django development server will run on
EXPOSE 8000

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
