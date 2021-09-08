#!/bin/bash
sed "s/tagVersion/$1/g" ansible/imageBuild.yml > ansible/imageBuildDynamicTag.yml
sed "s/tagVersion/$1/g" prometheus-djangoapp/django-all.yml > prometheus-djangoapp/django-all-dynamictag.yml


