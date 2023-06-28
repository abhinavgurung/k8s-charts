Port forward with `kubectl port-forward service/my-service 3001:80`

To run only backend

kubectl apply f ./back-deploy.yaml
kubectl port-forward service/back-service 5000:80

while running docker-compose host in **init**.py and container name in docker-compose should match
