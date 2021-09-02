#!/bin/bash
curr_dir=$(pwd)
docker build -t abhitrone/django_prometheus:6.0 "$curr_dir"
docker push abhitrone/django_prometheus:6.0  
