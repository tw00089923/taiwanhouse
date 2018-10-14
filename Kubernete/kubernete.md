
### Start Kubernete 

#### Introduction 
[維基百科]("https://zh.wikipedia.org/wiki/Kubernetes")
跨主機集群的自動部署、擴展以及運行應用程式容器的平台

<img src="https://d33wubrfki0l68.cloudfront.net/1567471e7c58dc9b7d9c65dcd54e60cbf5870daa/da576/_common-resources/images/flower.png" width="300">
Kubernetes is an open-source system for automating deployment, scaling, and management of containerized applications.
#### Content
1. [install](#1-install)
2. [Basic workloads](#2-basic-workloads)
3. [Deploy an application](-#3deploy-an-application)
4. [Understand basic Kubernetes architecture](#4-understandubasic-kubernetes-architecture)
5. [Additional resources](#5-additional-resources)

#### 1. install 
#### 請確認安裝 virtualbox , Docker
> $ brew cask install minikube
> $ brew install kubectl
> $ minikube start
> $ kubectl config current-context
=> minikube
> $ kubectl config use-context minikube

#### 2. Basic workloads

* General concepts
    * Configuration files : write Yaml or Json [Example]("https://kubernetes.io/docs/tasks/run-application/run-stateless-application-deployment/#creating-and-exploring-an-nginx-deployment")
    * Pods : the basic unit for all of the workloads [Example]("https://kubernetes.io/docs/tutorials/kubernetes-basics/explore/explore-intro/")

* Common workload objects
    * Deployment :  The most common way of running X copies (Pods) of your application. Supports rolling updates to your container images
    * Service : a Deployment can’t receive traffic. Setting up a Service is one of the simplest ways to configure a Deployment to receive and loadbalance requests.

* Metadata : specify custom information about your Kubernetes API objects 
    * Labels : Identifying metadata that you can use to sort and select sets of API objects.
    * Annotations : Nonidentifying metadata that you can attach to API objects, usually if you don’t intend to use them for sorting purposes.


* Storage 
storage API objects for different storage needs
    * Volumes : define storage for your cluster.
    * PersistentVolumes and PersistentVolumeClaims  : define storage at the cluster level.


The following examples demonstrate the fundamentals of deploying Kubernetes apps:
* Stateless apps: [Deploy a simple nginx server.]("https://kubernetes.io/docs/tasks/run-application/run-stateless-application-deployment/")
* [Stateful apps: Deploy a MySQL database.]("https://kubernetes.io/docs/tasks/run-application/run-single-instance-stateful-application/")


#### 3. Deploy an application
#### 4. Understand basic Kubernetes architecture
#### 5. Additional resources