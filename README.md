

# Dockerizing a Flask Application 🚀

Welcome to the guide on Dockerizing a Flask application! This README provides a comprehensive guide on setting up, building, and running a Dockerized Flask app, along with some useful Docker commands.

## 📁 Project Structure

Here is the directory structure of the Flask project:

```
Flask_App/
├── AI_Service/
│   ├── gemini_response_text.py
│   └── gemini_response_image.py
├── Backend/
│   └── app.py
├── Frontend/
│   ├── static/
│   │   ├── Images/
│   │   │   └── icon.jpg
│   │   ├── style.css
│   │   └── script.js
│   └── templates/
│       └── index.html
├── uploads/
├── Dockerfile
├── .env
└── requirements.txt
```

- **`AI_Service/`**: Contains scripts for processing text and image responses.
- **`Backend/`**: Includes the main Flask application file.
- **`Frontend/`**: Holds static files (CSS, JavaScript, images) and HTML templates.
- **`uploads/`**: Directory for storing uploaded files.
- **`Dockerfile`**: Configuration file for building the Docker image.
- **`.env`**: Environment variables.
- **`requirements.txt`**: Python dependencies.

## 🛠️ Getting Started

### 1. Setting Up the Flask Project

Before Dockerizing, ensure your Flask application is set up correctly:

1. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask app locally** to verify everything works:
   ```bash
   python Backend/app.py
   ```

### 2. Building the Docker Image

Build the Docker image for your Flask app using:

```bash
docker build -t flask-app .
```

### 3. Running the Docker Container

Run the Docker container and map the local `uploads` directory to the container’s `uploads` directory:

```bash
docker run -p 3000:3000 -v "$(pwd)/uploads:/app/uploads" flask-app
```

- **`-p 3000:3000`**: Maps port 3000 on your local machine to port 3000 in the container.
- **`-v "$(pwd)/uploads:/app/uploads"`**: Shares the `uploads` directory between your host and the container.

### 4. Accessing the Flask App

Once the container is running, access the Flask application at [http://localhost:3000](http://localhost:3000). 🎉

## 📋 Useful Docker Commands

Here are some essential Docker commands to manage your containers and images:

- **List Docker images**: 
  ```bash
  docker images
  ```

- **List running containers**: 
  ```bash
  docker ps
  ```

- **List all containers (including stopped ones)**: 
  ```bash
  docker ps -a
  ```

- **Remove a Docker image**: 
  ```bash
  docker rmi -f image-name
  ```

- **View logs from a container**: 
  ```bash
  docker logs container-id
  ```

- **Open an interactive terminal session inside a container**: 
  ```bash
  docker exec -it container-id /bin/bash
  ```

## Demo
https://github.com/user-attachments/assets/e67d7f4e-a2c9-4c9a-890a-61e5b3e88168






