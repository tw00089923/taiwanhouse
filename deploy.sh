#!/bin/bash

echo "Creating the volume..."

kubectl apply -f ./kubernetes/persistent-volume.yml
kubectl apply -f ./kubernetes/persistent-volume-claim.yml

echo "Creating the database credentials..."

kubectl apply -f ./kubernetes/secret.yml


echo "Creating the mysql deployment and service..."

kubectl create -f ./kubernetes/mysql-deployment.yml
kubectl create -f ./kubernetes/mysql-service.yml



echo "Creating the flask deployment and service..."

kubectl create -f ./kubernetes/flask-deployment.yml
kubectl create -f ./kubernetes/flask-service.yml



echo "Creating the vue deployment and service..."

kubectl create -f ./kubernetes/vue-deployment.yml
kubectl create -f ./kubernetes/vue-service.yml