# Deploying the app on kubernetes (minikube)
### Assumptions
1. It is assumed you have minikube installed.
2. The kubernetes version on minikube is 1.8.x.

## Steps

1. Set your kubectl context
```
kubectl config use-context minikube
```
2. Apply the namespace for the app.

```
kubectl apply -f namespace.yml
```
3. apply the deployment 
```
kubectl apply -f deployment-app.yml
```
4. Check if the pod is up and running
```
kubectl get service -n tan-app
```
5. Create the network policy
```
kubectl apply -f networkpolicy.yml
```
6. Expose the deployment so you can access it from your browser
```
kubectl expose deployment leave-nginx-deployment -n tan-app --type=NodePort
kubectl expose deployment leave-app-deployment -n tan-app --type=NodePort
```
7. Expose the service on minikube
```
minikube service leave-app-service -n tan-app
```
7. Check the service and port mapping
```
kubectl get svc -n tan-app
```
You should see something like this
```
NAME                   CLUSTER-IP   EXTERNAL-IP   PORT(S)          AGE
leave-app-deployment   10.0.0.105   <nodes>       1234:31825/TCP   46m
leave-nginx-deployment   10.0.0.105   <nodes>       1234:31825/TCP   46m
```
Note the port mapping e.g 1234:31825, you will need it

8. Get the IP address of your minikube
```
minikube ip
```
copy this IP address

