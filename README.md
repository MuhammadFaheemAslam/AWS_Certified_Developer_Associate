# AWS_Certified_Developer_Associate
This repo is for aws certified developer associate exam preparation

We are going to use AWS CLI tool as well to work with AWS Services


1:AWS Cli setup link

https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html

also create a user through aws managment console with the appropriate policy


2:Amazon Elastic Container Registry (ECR)
 is a fully managed container image registry provided by AWS. It allows you to securely store, manage, and deploy container images (such as Docker images). ECR integrates seamlessly with AWS container services like Amazon ECS, EKS, and AWS Fargate, as well as with CI/CD tools for streamlined workflows.

Go to AWS ECR folder for more details

Docker image creation from root folder
docker build -t flask-app -f Docker/Dockerfile .

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

