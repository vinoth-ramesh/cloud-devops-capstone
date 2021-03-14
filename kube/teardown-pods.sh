#!/bin/bash

kubectl --kubeconfig=config-aws delete pods,services -l app=std-app

kubectl --kubeconfig=config-aws delete pods,services -l app=mongodb

kubectl --kubeconfig=config-aws delete pods,services -l app=loadbalancer
