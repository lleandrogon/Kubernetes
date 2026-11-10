# Kubernetes Lab - FastAPI + PostgreSQL + MySQL

Laboratório de estudos de Kubernetes utilizando Kind como cluster local.

## Tecnologias

- FastAPI
- Docker
- Kind
- Kubernetes
- PostgreSQL
- MySQL
- NGINX Ingress Controller

---

# Estrutura do Projeto

```text
.
├── app.py
├── Dockerfile
├── requirements.txt
│
└── k8s/
    ├── namespace.yaml
    │
    ├── app/
    │   ├── deployment.yaml
    │   └── service.yaml
    │
    ├── postgres/
    │   ├── configmap.yaml
    │   ├── secret.yaml
    │   ├── pvc.yaml
    │   ├── deployment.yaml
    │   └── service.yaml
    │
    ├── mysql/
    │   ├── configmap.yaml
    │   ├── secret.yaml
    │   ├── pvc.yaml
    │   ├── deployment.yaml
    │   └── service.yaml
    │
    └── ingress/
        └── ingress.yaml
```

---

# Conceitos Aprendidos

## Namespace

Isola recursos dentro do cluster.

```yaml
kind: Namespace
```

---

## Deployment

Responsável por:

- Criar Pods
- Recriar Pods
- Atualizar versões
- Escalar Pods

---

## ReplicaSet

Mantém a quantidade desejada de Pods.

```text
Deployment
    ↓
ReplicaSet
    ↓
Pods
```

---

## Service

Fornece um endereço estável para acessar Pods.

Exemplos:

```text
minha-api-service
postgres-service
mysql-service
```

---

## ConfigMap

Armazena configurações não sensíveis.

---

## Secret

Armazena credenciais.

---

## PVC (PersistentVolumeClaim)

Reserva armazenamento persistente.

```text
Pod
 ↓
PVC
 ↓
Volume
```

---

## Ingress

Permite expor aplicações HTTP usando hostnames.

```text
Browser
 ↓
Ingress
 ↓
Service
 ↓
Pod
```

---

# Criar Cluster

```powershell
kind create cluster --name estudos
```

Verificar:

```powershell
kubectl get nodes
```

---

# Build da Aplicação

```powershell
docker build -t minha-api:v1 .
```

---

# Carregar Imagem no Kind

```powershell
kind load docker-image minha-api:v1 --name estudos
```

---

# Criar Namespace

```powershell
kubectl apply -f k8s/namespace.yaml
```

Definir namespace padrão:

```powershell
kubectl config set-context --current --namespace=estudos
```

---

# Aplicar Recursos

```powershell
kubectl apply -R -f k8s/
```

---

# Comandos Úteis

Ver tudo:

```powershell
kubectl get all
```

Pods:

```powershell
kubectl get pods
```

Services:

```powershell
kubectl get svc
```

Deployments:

```powershell
kubectl get deployments
```

PVCs:

```powershell
kubectl get pvc
```

Storage Classes:

```powershell
kubectl get storageclass
```

---

# Logs

```powershell
kubectl logs deployment/minha-api
kubectl logs deployment/postgres
kubectl logs deployment/mysql
```

---

# Entrar nos Containers

PostgreSQL:

```powershell
kubectl exec -it deployment/postgres -- bash
```

MySQL:

```powershell
kubectl exec -it deployment/mysql -- bash
```

---

# Port Forward

FastAPI:

```powershell
kubectl port-forward service/minha-api-service 8000:8000
```

PostgreSQL:

```powershell
kubectl port-forward service/postgres-service 5432:5432
```

MySQL:

```powershell
kubectl port-forward service/mysql-service 3306:3306
```

---

# Ingress NGINX

Instalação:

```powershell
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/kind/deploy.yaml
```

Verificar:

```powershell
kubectl get pods -n ingress-nginx
```

Ingress:

```powershell
kubectl get ingress
```

---

# Escalando Aplicação

```powershell
kubectl scale deployment/minha-api --replicas=3
```

---

# Reiniciar Deployment

```powershell
kubectl rollout restart deployment/minha-api
```

---

# Teste de Persistência

Apagar Pod:

```powershell
kubectl delete pod -l app=postgres
```

O Deployment recriará o Pod.

Os dados permanecem porque estão armazenados no PVC.

---

# Próximos Estudos

- Resource Requests e Limits
- StatefulSet
- Horizontal Pod Autoscaler (HPA)
- Helm
- Multi-node Cluster
- CI/CD

---

# Fluxo Mental Kubernetes

```text
Dockerfile
    ↓
docker build
    ↓
Imagem
    ↓
kind load docker-image
    ↓
Deployment
    ↓
ReplicaSet
    ↓
Pod
    ↓
Service
    ↓
Ingress
    ↓
Usuário
```
