# AWS_Certified_Developer_Associate
This repo is for aws certified developer associate exam preparation

We are going to use AWS CLI tool as well to work with AWS Services


1:AWS Cli setup link

https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html

Also create a user through aws managment console with the appropriate policy

----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------

1.1 Docker image setup by using flask app

    1.Create Your Flask App
    2.Create a Dockerfile
    3.Build and Test the Docker Image Locally

For more detailed look into the docker directory



2:Amazon Elastic Container Registry (ECR)
 is a fully managed container image registry provided by AWS. It allows you to securely store, manage, and deploy container images (such as Docker images). ECR integrates seamlessly with AWS container services like Amazon ECS, EKS, and AWS Fargate, as well as with CI/CD tools for streamlined workflows.

        
    1.Create an ECR Repository
    2.Authenticate Docker with ECR
    3.Tag the Docker Image
    4.Push the Image to ECR

Go to AWS ECR folder for more details

Docker image creation from root folder
docker build -t flask-app -f Docker/Dockerfile .

----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------


3:Amazon ECS (Elastic Container Service) --with Fargate or EC2 instances using the AWS CLI

Prerequisites
    your AWS user has the permissions specified in the AdministratorAccess IAM polic
    Your user has the IAM permissions to create a service role.
    A user with administrator access has manually created the task execution role so that it is available on the account to be used.

    1. ECR Permissions
        AmazonEC2ContainerRegistryFullAccess — Provides full access to ECR repositories, including pushing and pulling images.
    2. ECS Permissions
        AmazonECS_FullAccess — Provides full access to ECS, including managing clusters, task definitions, and services.
        AmazonECSTaskExecutionRolePolicy
    3. IAM Permissions for ECS Execution Role
        IAMReadOnlyAccess — Grants read-only access to IAM resources (for viewing roles and policies).
        IAMFullAccess — Grants full access to IAM resources (for creating and assigning roles, which might be necessary for task execution roles).
    4. VPC and Networking Permissions
        AmazonVPCFullAccess — Provides full access to VPC resources, including subnets, security groups, and network interfaces.
    5. CloudWatch Logs Permissions
        CloudWatchLogsFullAccess — Provides full access to CloudWatch Logs, allowing tasks to write logs.
    6. S3 Permissions (Optional, if interacting with S3)
        AmazonS3FullAccess — Grants full access to S3, if your application requires interacting with S3.
    7. EC2 Permissions (If using EC2 Launch Type)
        AmazonEC2FullAccess — Provides full access to EC2, if you are using EC2 instances for your ECS tasks.



    These policies should provide all the permissions needed for typical ECS tasks involving ECR, ECS, IAM, VPC, CloudWatch, and EC2/S3 (if applicable).

 --we will use our previous tasks like docker images and AWS ECR in this AWS ECS

    Create the cluster
    Create a task definition
    Create the service
    View your service
    Clean up

--For further details see AWS_ECS directory



----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------


4. Amazon Elastic Kubernetes Service (Amazon EKS)

    What is AWS EKS?
    AWS Elastic Kubernetes Service (EKS) is a managed Kubernetes service that makes it easy to run Kubernetes on AWS without needing to install, operate, and maintain Kubernetes control planes or nodes.


Prerequisites
    AWS CLI installed and configured.
    kubectl installed.
    AWS IAM role with required EKS permissions.
    AWS EKS CLI (eksctl) installed.
    Docker installed for containerizing your app.

You will need several AWS and Kubernetes tools to manage EKS:
    AWS CLI: The AWS Command Line Interface (CLI) lets you interact with AWS services, including EKS.
    kubectl: Kubernetes CLI for interacting with the Kubernetes API server.
    eksctl: A simple CLI tool to create and manage EKS clusters.


Roadmap for Application Developers
To deploy your Flask app as a Docker image in AWS Elastic Kubernetes Service (EKS), you need to follow these detailed steps:
    Step1: Prepare Your Flask Application
        use the existing flask app that we created in first session

    Step 2: Push the Docker Image to Amazon Elastic Container Registry (ECR)
        We already have an docker image so we will use this
        
    Step 3: Set Up AWS EKS
        1.Create an EKS Cluster
        2.Update kubeconfig
        3.Verify the Cluster


    Step 4: Deploy Flask App to EKS
        1.Create a Kubernetes Deployment Manifest
        2.Create a Kubernetes Service Manifest
        3.Apply the Manifests
        4.Verify the Deployment


    Step 5: Access the Application
        1.Get the External IP
        2.Access the Flask App


    Step 6: (Optional) Monitor and Optimize
        1.Monitor Using CloudWatch
        2.Autoscale the Application

    See AWS_EKS directory for detailed 

Which API Should You Use?

    Use the Kubernetes API (via kubectl) for interacting with and managing your containerized applications, deployments, and resources.
    Use the AWS EKS API (via the AWS CLI or SDK) for managing EKS-specific resources, including clusters, networking, and IAM roles.


----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------


5.Getting started with Elastic Beanstalk

    Prerequisites
        AWS CLI
        Elastic Beanstalk CLI (EB CLI)
        Make sure your AWS IAM user has the necessary permissions to work with Elastic Beanstalk, EC2, and other AWS resources (like S3, RDS, etc.).
        Application Code:
            Prepare the application code you want to deploy (e.g., a simple Python Flask app, Django app, Node.js, etc.).


    Initialize the project: eb init
    Create environment: eb create my-env
    Deploy the app: eb deploy
    Open the app: eb open
    Check status: eb status
    View logs: eb logs
    Terminate environment: eb terminate







----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------


6.AWS Lambda

We are using this as a web application developer

Deploying a Serverless Web Application (End-to-End)
    Frontend: Build a web or mobile frontend using HTML, CSS, JavaScript, React, etc.
    Backend: Use Lambda functions behind an API Gateway to serve as the backend.
    Authentication: Integrate Amazon Cognito for user authentication and authorization.
    Database: Use DynamoDB as a serverless NoSQL database to store user data or application data.
    Hosting: Host the frontend using Amazon S3 (static website hosting) or Amazon CloudFront.


Prerequisites
    Before you can create the example app, make sure you have the required command line tools installed.
    AWS CLI
        You can manually deploy the resources for your app using either the AWS Management Console or the AWS CLI. 
    AWS SAM CLI
        If you want to deploy the example app using AWS SAM, you need to install both the AWS CLI and the AWS SAM CLI.


1.Create IAM Role for Lambda using the AWS CLI.
2.Write the Lambda function in Python and create a deployment package.
3.Create an API Gateway REST API, resource, and method.
4.Integrate API Gateway with Lambda.
5.Deploy the API and generate an Invoke URL.
6.Grant API Gateway permissions to invoke the Lambda function.
7.Test the API by making a GET request.
8.Monitor Lambda logs using CloudWatch.

6.1 SAM (Serverless )

Building a serverless application using AWS Lambda, API Gateway, DynamoDB, and EventBridge, with an example application for managing "Tasks" (Create, List, Delete).

Overview of the Application
1.Lambda Functions: Backend logic for the application.
    1.1.CreateTaskFunction: Adds tasks to a DynamoDB table.
    1.2.ListTasksFunction: Retrieves tasks from the table.
    1.3.DeleteTaskFunction: Deletes a task.
    1.4.EventBridgeFunction: Triggers when a task is deleted.
2.API Gateway: HTTP interface for invoking the Lambda functions.
3.DynamoDB: Stores tasks with taskId as the primary key.
4.EventBridge: Listens for events when a task is deleted.



Full Command Sequence
Here’s the summarized sequence:

    # Initialize the project
    sam init

    # Edit the template.yaml
    nano template.yaml

    # Write the application code
    mkdir src
    nano src/create_task.py
    nano src/list_tasks.py
    nano src/delete_task.py
    nano src/event_bridge.py

    # Build and deploy the application
    sam build
    sam deploy --guided

    # Test the application
    curl -X POST https://<API_ID>.execute-api.<region>.amazonaws.com/Prod/tasks -H "Content-Type: application/json" -d '{"name": "Learn SAM"}'
    curl https://<API_ID>.execute-api.<region>.amazonaws.com/Prod/tasks
    curl -X DELETE https://<API_ID>.execute-api.<region>.amazonaws.com/Prod/tasks/<taskId>

    # Monitor logs
    aws logs describe-log-groups
    aws logs get-log-events --log-group-name "/aws/lambda/CreateTaskFunction" --log-stream-name <stream-name>

    # Clean up resources
    aws cloudformation delete-stack --stack-name TaskManagerStack