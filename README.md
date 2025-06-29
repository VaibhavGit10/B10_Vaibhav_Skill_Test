# Kubernetes Microservices Deployment - Skill Test

This project demonstrates the deployment of four containerized Node.js microservices using Kubernetes on Minikube with optional Ingress routing.

## 📦 Microservices Overview

| Service Name     | Port | Description              |
|------------------|------|--------------------------|
| User Service     | 3000 | Manages user operations  |
| Product Service  | 3001 | Handles product data     |
| Order Service    | 3002 | Processes orders         |
| Gateway Service  | 3003 | API Gateway for routing  |

---

## 🧰 Prerequisites

- OS: Ubuntu 22.04
- [Minikube](https://minikube.sigs.k8s.io/docs/start/)
- Docker (Minikube must use Docker driver)
- kubectl (v1.33 or higher)
- Git (to clone this repo)
- curl (for service testing)

---

## 📁 Folder Structure

```bash
submission/
├── deployments/
│   ├── user-service.yaml
│   ├── product-service.yaml
│   ├── order-service.yaml
│   └── gateway-service.yaml
├── services/
│   ├── user-service.yaml
│   ├── product-service.yaml
│   ├── order-service.yaml
│   └── gateway-service.yaml
├── ingress/                         # (Optional) Ingress routing configuration
│   └── ingress.yaml
├── screenshots/
│   ├── pods.png
│   ├── logs.png
│   └── service-test.png
└── README.md
```
---

## 🧰 Minikube Setup

1. Start Minikube with Docker driver:
   ```bash
   minikube start --driver=docker
2. Enable Ingress (for bonus task):
   ```bash
   minikube addons enable ingress
3. Load Docker images into Minikube (optional if not using external registry):
    ```bash
    minikube image load <image-name>
    
---

## 🚀 Deploying Microservices

Step 1: Apply Deployments

```bash
kubectl apply -f deployments/
```

Step 2: Apply Services

```bash
kubectl apply -f services/
```

## 🌐 Ingress (Bonus Task)

Step 3: Apply Ingress (Optional)

```bash
kubectl apply -f services/
```

Step 4: Update your /etc/hosts

```bash
sudo nano /etc/hosts
```

Add this line:
```lua
192.168.49.2 microservices.local
```
---

## 🧪 Testing Services

## View Logs
```bash
kubectl logs deployment/<service-name>
```

## Curl Test via Ingress

```bash
curl http://microservices.local/api/users
curl http://microservices.local/api/products
curl http://microservices.local/api/orders
```

---

## 🛠 Troubleshooting

## • Check pod status:

```bash
kubectl get pods
```

## • Describe a pod for detailed info:

```bash
kubectl describe pod <pod-name>
```

## • Ensure images are accessible to Minikube:

```bash
minikube image load <image-name>
```

---

## 🚀 Deployment Checklist

- 📦 All images loaded into Minikube
- ✅ Services applied successfully
- 🔧 Probes configured
- 📁 Folder structure organized
- 🧪 curl tested with Ingress

---

## ✅ Conclusion

All four microservices have been successfully containerized and deployed on Kubernetes using Minikube. The architecture supports internal service communication through `ClusterIP` services and can be externally accessed using an Ingress controller with clean routing paths.

This project reflects an industry-standard microservices deployment pipeline and demonstrates hands-on proficiency with Kubernetes fundamentals, service networking, and deployment automation.

---

## 🙋‍♂️ Submitted by

**Vaibhav Pawar**  
Junior AI Programmer | DevOps Trainee  
GitHub: [@VaibhavGit10](https://github.com/VaibhavGit10)

---

## 📅 Submission

**Date:** June 29, 2025  
**Project:** Kubernetes Microservices Deployment Assessment  
**Platform:** Ubuntu 22.04 + Minikube + Docker + Kubernetes

---

