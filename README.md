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

7. Port-forwarding:
   kubectl port-forward deployment/practice-deployment 5000:5000

##For Replication Controller
1. Create a recplication_controller-deplymnet file
   kubectl apply -f .\replication-controller_deployment.yaml

2. to check the
   kubectl get rc

   3. port forwarding:
      kubectl port-forward rc/nginx-rc 5003:80
