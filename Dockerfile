FROM python:3.8-slim


# Install system dependencies
RUN apt-get update && apt-get install -y \
    libsqlite3-dev

# Install Streamlit
RUN pip install --no-cache-dir streamlit==1.34.0

# Set the working directory
WORKDIR /app

# Copy the Streamlit app file into the container
COPY app.py /app

# Expose port 8501 for Streamlit
EXPOSE 8501

# Run Streamlit app
CMD ["streamlit", "run", "--server.port", "8501", "app.py"]
