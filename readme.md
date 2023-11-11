#### make sure all the commands are being run from main folder level(i.e. sample)

## Create Images

    `docker-compose build`

## Tag images

    `docker tag sample-app decodeit191/sample-app`
    `docker tag sample-api decodeit191/sample-api`

## Login docker hub

    `docker login`

## Push images to docker hub

    `docker push decodeit191/sample-app`
    `docker push decodeit191/sample-api`

## apply yaml manifest using kubectl

    `kubectl apply -f ./charts/back-deploy.yaml`
    `kubectl apply -f ./charts/frontend-deployment.yaml`

Port forward with `kubectl port-forward service/my-service 3001:80`

To run only backend

kubectl apply f ./back-deploy.yaml
kubectl port-forward service/back-service 5000:80

while running docker-compose host in **init**.py and container name in docker-compose should match
