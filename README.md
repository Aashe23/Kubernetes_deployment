# Kubernetes_deployment
#The command which are used:
1. Create cluster:
kind create cluster --config config.yaml

2. delete a cluster:
kind delete cluster --name kind

3. Build an image:
   docker build -t practice-image:1.0 .
  
4. Image taging:
   docker tag practice-image:1.0 aashe1623/practice-image:1.0

5. Image push :
   docker push aashe1623/practice-image:1.0

6. Deployment created:
   kubectl apply -f deployment.yaml
