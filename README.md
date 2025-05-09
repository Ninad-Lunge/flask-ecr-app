Here's a polished and well-formatted version for your GitHub README:

---

# 🚀 Amazon ECS Standard Deployment with CodePipeline

This project demonstrates a simple CI/CD pipeline using **GitHub**, **AWS CodePipeline**, and **ECS Fargate**, based on the [AWS User Guide](https://docs.aws.amazon.com/codepipeline/latest/userguide/ecs-cd-pipeline.html).

## 🛠️ Project Overview

We create a simple Flask application, containerize it using Docker, push it to Amazon Elastic Container Registry (ECR), and deploy it automatically to Amazon ECS using AWS CodePipeline.

---

## 📦 Flask App Setup

### `app.py`

```python
from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def hello():
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Deployment Status</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(to right, #00b09b, #96c93d);
                color: white;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                margin: 0;
            }
            .message-box {
                background: rgba(0, 0, 0, 0.3);
                padding: 50px;
                border-radius: 12px;
                text-align: center;
                box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
            }
            h1 {
                font-size: 2.5rem;
                margin-bottom: 0.5em;
            }
            p {
                font-size: 1.3rem;
            }
        </style>
    </head>
    <body>
        <div class="message-box">
            <h1>🚀 Success!</h1>
            <p>CICD Pipeline with GitHub + AWS CodePipeline + ECS Fargate!!</p>
        </div>
    </body>
    </html>
    """
    return render_template_string(html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

---

## 🐳 Dockerfile

```dockerfile
# Base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy app code
COPY app.py .

# Expose port
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
```

---

## 🔨 Build Docker Image

Run the following command to build the Docker image:

```bash
docker build -t flask-app:latest .
```


## 🧪 Requirements

Create a `requirements.txt` file:

```
Flask==2.2.2
```

---

## 🔨 Build Docker Image

```bash
docker build -t flask-app:latest .
```

---

## 🐋 Push Docker Image to Amazon ECR

1. **Authenticate Docker with ECR:**

```bash
aws ecr get-login-password --region <your-region> | docker login --username AWS --password-stdin <your-account-id>.dkr.ecr.<your-region>.amazonaws.com
```

2. **Create an ECR Repository:**

```bash
aws ecr create-repository --repository-name flask-app
```

3. **Tag your image:**

```bash
docker tag flask-app:latest <your-account-id>.dkr.ecr.<your-region>.amazonaws.com/flask-app:latest
```

4. **Push the image:**

```bash
docker push <your-account-id>.dkr.ecr.<your-region>.amazonaws.com/flask-app:latest
```

---

## ⚙️ Set Up AWS CodePipeline for ECS

### 1. **Create a Task Definition in ECS:**

* Use the pushed ECR image.
* Choose **Fargate** launch type.
* Assign CPU and memory.
* Set container port to `5000`.

### 2. **Create an ECS Cluster:**

* Use **Fargate** and appropriate VPC/subnets.

### 3. **Create a Service:**

* Choose your task definition.
* Use **Fargate** and the same VPC/subnet.

### 4. **Create a CodePipeline:**

Go to **AWS CodePipeline** and:

* **Source stage**: Choose GitHub as your source, connect your repo.
* **Build stage**: (Optional) Use AWS CodeBuild to run your `docker build` and `docker push` commands.
* **Deploy stage**: Choose **Amazon ECS (Blue/Green)** or standard ECS deployment, and specify:

  * ECS Cluster
  * ECS Service
  * Image definition file (usually `imagedefinitions.json`)

---

## 📁 Sample `imagedefinitions.json`

Used by CodePipeline to update ECS with the new image:

```json
[
  {
    "name": "flask-app",
    "imageUri": "<your-account-id>.dkr.ecr.<your-region>.amazonaws.com/flask-app:latest"
  }
]
```

Generate this in your build step or store it in your repo.

---

![image](https://github.com/user-attachments/assets/4b9f7967-838b-40af-8b87-5ccd3a88903a)
![image](https://github.com/user-attachments/assets/8298cd33-714b-4847-bff0-866aff305093)
![image](https://github.com/user-attachments/assets/d68ee2b6-a2eb-43f7-950f-f10ae8a732e1)
