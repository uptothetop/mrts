init:
	eval $(minikube docker-env) && \
	minikube -p minikube docker-env && \
	minikube start && \
	kubectl apply -f deployment.yaml && \
	kubectl apply -f service.yaml && \
	kubectl apply -f mongodb-deployment.yaml && \
	kubectl apply -f mongodb-pv-pvc.yaml && \
	kubectl apply -f mongodb-service.yaml

build:
	docker build -t fastapi-app . && \
	minikube image load fastapi-app

delete:
	minikube delete

dash:
	minikube dashboard

url:
	minikube service fastapi-app --url