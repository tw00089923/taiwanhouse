
### Start Kubernete 

#### Introduction 
[維基百科]("https://zh.wikipedia.org/wiki/Kubernetes")
跨主機集群的自動部署、擴展以及運行應用程式容器的平台

<img src="https://d33wubrfki0l68.cloudfront.net/1567471e7c58dc9b7d9c65dcd54e60cbf5870daa/da576/_common-resources/images/flower.png" width="300">
Kubernetes is an open-source system for automating deployment, scaling, and management of containerized applications.
#### [Content]("https://kubernetes.io/docs/user-journeys/users/application-developer/foundational/")
1. [install](#1-install)
2. [Deploy an application](#2-deploy-an-application)
3. [Understand basic Kubernetes architecture](#3-understandubasic-kubernetes-architecture)
4. [Additional resources](#4-additional-resources)

#### 1. install 
#### 請確認安裝 virtualbox , Docker
> $ brew cask install minikube
> $ brew install kubectl
> $ minikube start
> $ kubectl config current-context
=> minikube
> $ kubectl config use-context minikube

#### 2. deploy-an-application

The following examples demonstrate the fundamentals of deploying Kubernetes apps:
* Stateless apps: [Deploy a simple nginx server.]("https://kubernetes.io/docs/tasks/run-application/run-stateless-application-deployment/")
* [Stateful apps: Deploy a MySQL database.]("https://kubernetes.io/docs/tasks/run-application/run-single-instance-stateful-application/")

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

* Configuration

To avoid having to unnecessarily rebuild your container images, you should decouple your application’s configuration data from the code required to run it

    * Using a [manifest's container definition]("https://kubernetes.io/docs/tasks/inject-data-application/define-environment-variable-container/") -> Command-line flag 
    * Using [ConfigMaps]("https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/") -> nginx configuration
    * Using [Secrets]("https://kubernetes.io/docs/concepts/configuration/secret/") -> Database credentials

        * If you have any data that you want to keep private, you should be using a Secret. Otherwise there is nothing stopping that data from being exposed to malicious users.



#### 3. Understand basic Kubernetes architecture
As an app developer, you don’t need to know everything about the inner workings of Kubernetes, but you may find it helpful to understand it at a high level.
* What Kubernetes offers
    1. One instance of your app (a complete machine instance or just a container) goes down.
    2. Because your team has monitoring set up, this pages the person on call.
    3. The on-call person has to go in, investigate, and manually spin up a new instance.
    4. Depending how your team handles DNS/networking, the on-call person may also need to also update the service discovery mechanism to point at the IP of the new Rails instance rather than the old.

* Kubernetes API server
    * Your YAML or JSON configuration files declare this desired state in terms of one or more API objects, such as [Deployments]("https://kubernetes.io/docs/concepts/workloads/controllers/deployment/") . To make updates to your cluster’s state, you submit these files to the Kubernetes API  server ([kube-apiserver]("https://kubernetes.io/docs/concepts/overview/kubernetes-api/")).
* Controllers
Once you’ve declared your desired state through the Kubernetes API, the controllers work to make the cluster’s current state match this desired state.
The standard controller processes are kube-controller-manager and cloud-controller-manager, but you can also write your own controllers as well.

#### 4. Additional resources

The Kubernetes documentation is rich in detail. Here’s a curated list of resources to help you start digging deeper.

* Basic concepts
    * [More about the components that run Kubernetes]("https://kubernetes.io/docs/concepts/overview/components/")
    * [Understanding Kubernetes objects]("https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/")
    * [More about Node objects]("https://kubernetes.io/docs/concepts/architecture/nodes/")
    * [More about Pod objects]("https://kubernetes.io/docs/concepts/workloads/pods/pod-overview/")

* Tutorials
    * [Kubernetes Basics]("https://kubernetes.io/docs/tutorials/kubernetes-basics/")
    * [Hello Minikube (Runs on Mac only)]("https://kubernetes.io/docs/tutorials/stateless-application/hello-minikube/")
    * [Kubernetes 101]("https://kubernetes.io/docs/user-guide/walkthrough/")
    * [Kubernetes 201]("https://kubernetes.io/docs/user-guide/walkthrough/k8s201/")
    * [Kubernetes object management]("https://kubernetes.io/docs/tutorials/object-management-kubectl/object-management/")

* What’s next
If you feel fairly comfortable with the topics on this page and want to learn more, check out the following user journeys:

    * [Intermediate App Developer]("https://kubernetes.io/docs/user-journeys/users/application-developer/intermediate/") - Dive deeper, with the next level of this journey.
    * [Foundational Cluster Operator]("https://kubernetes.io/docs/user-journeys/users/cluster-operator/foundational/") - Build breadth, by exploring other journeys.