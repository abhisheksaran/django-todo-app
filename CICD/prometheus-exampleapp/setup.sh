#!/bin/bash
k apply -f example-app-deployment.yaml
k apply -f example-app-service.yaml
k apply -f example-app-service-monitor.yaml
k apply -f prometheus-cluster-role-binding.yaml
k apply -f prometheus-service-monitor.yaml
k apply -f prometheus-service.yaml
