#!/bin/bash
kubectl apply -f prometheus-operator.yaml
kubectl apply -f example-app-deployment.yaml
kubectl apply -f example-app-service.yaml
kubectl apply -f example-app-service-monitor.yaml
kubectl apply -f prometheus-cluster-role-binding.yaml
kubectl apply -f prometheus-service-monitor.yaml
kubectl apply -f prometheus-service.yaml
