#!/bin/bash

dockerhub_username=vlddm

cd nodes
for dname in */
do
  tag=$dockerhub_username/${dname::-1}:latest 
  docker build --tag ${tag} ./${dname}
  docker push ${tag}
done
cd -
