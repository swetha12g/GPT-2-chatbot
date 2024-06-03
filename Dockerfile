# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Download the model and tokenizer files during build time to avoid downloading during runtime
RUN python -c "\
import transformers; \
model_name = 'gpt2'; \
tokenizer = transformers.GPT2Tokenizer.from_pretrained(model_name); \
model = transformers.GPT2LMHeadModel.from_pretrained(model_name);"

# Run the application
CMD ["python", "llama_chatbot.py"]

