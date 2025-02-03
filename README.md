# 🚀 Containerized Flask Application with Kubernetes

A modern Flask application containerized with Docker and deployed on Azure Kubernetes Service (AKS) with MongoDB backend.

## 📹 Demo

Check out our application demo video:

https://github.com/user-attachments/assets/90cb0623-ab32-4bb2-bf8a-66bc402c3bd5




## 🛠️ Tech Stack

### Backend
- 🐍 **Flask** - Python web framework
- 🔄 **PyMongo** - MongoDB Python driver


### Infrastructure
- 🐳 **Docker** - Containerization
- ⚙️ **Kubernetes** - Container orchestration
- ☁️ **Azure Kubernetes Service (AKS)** - Managed Kubernetes
- 📦 **Azure Container Registry (ACR)** - Container registry
- 🔄 **Azure CLI** - Command line interface for Azure

## 🏗️ System Architecture

- **Frontend Layer**: Flask application container
- **Database Layer**: MongoDB instance
- **Network Layer**: 
  - External LoadBalancer for application access
  - Internal ClusterIP for MongoDB communication
  - Network policies for security

## 🚀 Deployment Components

### Kubernetes Resources
- Application & MongoDB Deployment 
- LoadBalancer Service for application
- ClusterIP Service for MongoDB
- ConfigMaps for configuration

### Resource Specifications
- Application Pod:
  - Memory: 256Mi (limit: 512Mi)
  - CPU: 250m (limit: 500m)
- MongoDB Pod:
  - Memory: 256Mi (limit: 512Mi)
  - CPU: 250m (limit: 500m)

## 💻 Prerequisites

- Python 3.8+
- Docker Desktop
- Azure CLI
- kubectl
- MongoDB (for local development)



## 🐳 Docker Build & Push

1. **Build Docker image**
```bash
docker build -t bookstore-app:v1 .
docker tag bookstore-app:v1 your-acr-name.azurecr.io/bookstore-app:v1
```

2. **Test locally**
```bash
docker run -p 50505:50505 bookstore-app:v1
```

## ☁️ Azure Setup & Deployment

### Azure Login & Resource Creation

1. **Login to Azure**
```bash
az login
```

2. **Create Resource Group**
```bash
az group create --name YourResourceGroup --location eastus
```

3. **Create ACR (Azure Container Registry)**
```bash
az acr create --resource-group YourResourceGroup \
    --name YourACRName --sku Basic
```

4. **Create AKS Cluster**
```bash
az aks create --resource-group YourResourceGroup \
    --name YourAKSCluster \
    --node-count 2 \
    --generate-ssh-keys \
    --attach-acr YourACRName
```

### Push to ACR & Deploy

1. **Login to ACR**
```bash
az acr login --name YourACRName
```

2. **Push image to ACR**
```bash
docker push your-acr-name.azurecr.io/your-app-name:v1
```

3. **Get AKS credentials**
```bash
az aks get-credentials --resource-group YourResourceGroup --name YourAKSCluster
```

4. **Deploy to Kubernetes**
```bash
# Deploy MongoDB
kubectl apply -f YAML\ files/mongodb-deployment.yaml
kubectl apply -f YAML\ files/mongodb-service.yaml

# Deploy Application
kubectl apply -f YAML\ files/deployment.yaml
kubectl apply -f YAML\ files/service.yaml
```

5. **Verify deployment**
```bash
kubectl get pods
kubectl get services
```

## 🔍 Monitoring & Maintenance

### View Logs
```bash
# View application logs
kubectl logs -f deployment/your-app-name

# View MongoDB logs
kubectl logs -f deployment/mongodb
```

### Scale Application
```bash
# Scale replicas
kubectl scale deployment your-app-name --replicas=3
```

### Update Application
```bash
# Update image
kubectl set image deployment/your-app-name your-app-name=your-acr-name.azurecr.io/your-app-name:v2
```


## 📝 Note
This project is part of the AIN3003 (Database Systems and Cloud Computing) course assignment. For detailed methodology and findings, please refer to the project report.
