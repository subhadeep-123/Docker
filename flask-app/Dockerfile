ARG BASE_IMG=python:3.11.4-alpine3.17

# Stage 1: Build the application
FROM ${BASE_IMG} AS builder

LABEL maintainer="Subhadeep Banerjee <subhadeep762@gmail.com>"
LABEL description="Flask Rest API"

# Make virtual environment
RUN python -m venv /opt/venv

# Set PATH to virtual environment
ENV PATH="/opt/venv/bin:$PATH"

# Install Python dependencies
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the application code to the container
ADD src/ /app/src

# Set the working directory in the container
WORKDIR /app

# Stage 2: Create the final image running application
FROM ${BASE_IMG} AS run

# Set the working directory in the container
WORKDIR /app

# Set PATH to virtual environment
ENV PATH="/opt/venv/bin:$PATH" \
    # Keeps Python from generating .pyc files in the container
    PYTHONDONTWRITEBYTECODE=1 \
    # Turns off buffering for easier container logging
    PYTHONBUFFERED=1

# Copy installed dependencies from build stage
COPY --from=builder /opt/venv /opt/venv

# Copy the application code to the container
COPY --from=builder /app /app

# Set the command to run your application with Gunicorn using the virtual environment
CMD ["/opt/venv/bin/gunicorn", "--bind", "0.0.0.0:8080", "src.main:app"]