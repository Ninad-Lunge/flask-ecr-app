# 🚀 Amazon ECS Standard Deployment with CodePipeline

This project demonstrates a simple CI/CD pipeline using **GitHub**, **AWS CodePipeline**, and **ECS Fargate**, based on the [AWS User Guide](https://docs.aws.amazon.com/codepipeline/latest/userguide/ecs-cd-pipeline.html).

## 🛠️ Project Overview

We create a simple Flask application, containerize it using Docker, push it to Amazon Elastic Container Registry (ECR), and deploy it automatically to Amazon ECS using AWS CodePipeline.

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

### 2. **Create an Application Load Balancer:**

* Create an Internet Facing ALB
* Create a Security Group and attach it to ALB, allow inbound traffic from Port `80` (HTTP) and Port `5000` (Custom TCP) from `0.0.0.0/0`

![image](https://github.com/user-attachments/assets/4583f49f-c0d3-41c1-a743-5cd8c383f527)

* Attach a Listener to ALB to listen on Port `80` (HTTP)
* Create a Target Group with Port `5000` to allow inbound traffic from target containers

![Resource Map of ALB](https://github.com/user-attachments/assets/79142249-20c0-4b90-a06a-c66a031ffbc9)

### 3. **Create an ECS Cluster:**

* Use **Fargate** and appropriate VPC/subnets.

### 4. **Create a Service:**

* Choose your task definition.
* Use **Fargate** and the same VPC/subnet.
* Attach the previously created ALB, Listener and Target Group

![image](https://github.com/user-attachments/assets/6ad6a743-aa75-4727-aabb-c9559a6a6651)

### 5. **Create a CodePipeline:**

a. **Create a pipeline in AWS CodePipeline**

   * Source: GitHub or CodeCommit
   * Build: CodeBuild (with `buildspec.yml`)
   * Deploy: ECS (with `imagedefinitions.json`)

b. **Set up CodeBuild Project**

   * Enable Docker
   * Use managed image

c. **Grant ECR Permissions to CodeBuild Role**

   * Attach `AmazonEC2ContainerRegistryPowerUser` policy to the CodeBuild role.

---

## ✅ Testing the Pipeline

1. Make a code change.
2. Commit and push.
3. Watch the pipeline run on the [CodePipeline Console](https://console.aws.amazon.com/codepipeline/).
4. Confirm deployment in your ECS service.

---

![image](https://github.com/user-attachments/assets/d68ee2b6-a2eb-43f7-950f-f10ae8a732e1)

Access the application through DNS name of ALB using `http://<DNS_NAME_OF_ALB>`
![image](https://github.com/user-attachments/assets/a0988d05-9cbd-4e50-8397-fe1935a3f28e)
