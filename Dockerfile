# Step 1: Use the official Python image as the base image
FROM python:3.10-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the requirements directly into the container
COPY requirements.txt .

# Step 4: Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the rest of the application code
COPY . .

# Step 6: Expose the port the app runs on
EXPOSE 8000

# Step 7: Command to run the application
CMD ["uvicorn", "fastapi-hello-world:app", "--host", "0.0.0.0", "--port", "8000"]
