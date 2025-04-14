# 🐍 Use a clean Python base image
FROM python:3.9-slim

# 📁 Make a folder inside the container
WORKDIR /app

# 🧾 Copy your code and requirements into the container
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# 📢 Expose the port Flask runs on
EXPOSE 5000

# 🚀 Run the Flask app
CMD bash -c "pytest && python -m app.app"
