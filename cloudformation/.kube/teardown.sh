kubectl --kubeconfig=.kube/config-aws delete pods,services -l app=std-app

kubectl --kubeconfig=.kube/config-aws delete pods,services -l app=mongodb

kubectl --kubeconfig=.kube/config-aws delete pods,services -l app=loadbalancer
