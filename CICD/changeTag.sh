#!/bin/bash
sed "s/tagVersion/$1/g" playbook-image-build.yaml > playbook-image-build-dynamic-tag.yaml
sed "s/tagVersion/$1/g" django/django-all.yaml > django/django-all-dynamic-tag.yaml
