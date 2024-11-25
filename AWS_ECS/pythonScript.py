import boto3
import json

# Initialize the ECS client
ecs_client = boto3.client('ecs', region_name='ap-northeast-1')

# Function to create ECS cluster
def create_ecs_cluster(cluster_name):
    try:
        response = ecs_client.create_cluster(
            clusterName=cluster_name
        )
        print(f"Cluster created: {response['cluster']['clusterName']}")
        return response['cluster']['clusterName']
    except Exception as e:
        print(f"Error creating cluster: {e}")
        return None

# Function to create task definition
def create_task_definition():
    task_definition = {
        "family": "my-app-task-python",
        "networkMode": "awsvpc",
        "executionRoleArn": "arn:aws:iam::156041400331:role/ecsTaskExecutionRole",
        "containerDefinitions": [
            {
                "name": "my-app-container-python",
                "image": "156041400331.dkr.ecr.ap-northeast-1.amazonaws.com/flask-app-repo:latest",
                "memory": 512,
                "cpu": 256,
                "essential": True,
                "portMappings": [
                    {
                        "containerPort": 5000,
                        "hostPort": 5000,
                        "protocol": "tcp"
                    }
                ]
            }
        ],
        "requiresCompatibilities": ["FARGATE"],
        "cpu": "256",
        "memory": "512"
    }
    return task_definition

# Function to register the task definition
def register_task_definition(task_definition):
    try:
        response = ecs_client.register_task_definition(
            family=task_definition['family'],
            networkMode=task_definition['networkMode'],
            executionRoleArn=task_definition['executionRoleArn'],
            containerDefinitions=task_definition['containerDefinitions'],
            requiresCompatibilities=task_definition['requiresCompatibilities'],
            cpu=task_definition['cpu'],
            memory=task_definition['memory']
        )
        print(f"Task definition registered: {response['taskDefinition']['taskDefinitionArn']}")
        return response['taskDefinition']['taskDefinitionArn']
    except Exception as e:
        print(f"Error registering task definition: {e}")
        return None

# Function to run ECS service
def run_ecs_service(cluster_name, task_definition_arn):
    try:
        response = ecs_client.create_service(
            cluster=cluster_name,
            serviceName='my-app-service-python',
            taskDefinition=task_definition_arn,
            desiredCount=1,
            launchType='FARGATE',
            networkConfiguration={
                'awsvpcConfiguration': {
                    'subnets': ['subnet-0e81f1c43fd11df94', 'subnet-0545595e819f1212a'],
                    'assignPublicIp': 'ENABLED'
                }
            }
        )
        print(f"ECS Service created: {response['service']['serviceName']}")
    except Exception as e:
        print(f"Error creating ECS service: {e}")

# Main function
def deploy_app():
    cluster_name = "my-app-cluster-python"
    cluster_name = create_ecs_cluster(cluster_name)
    if not cluster_name:
        return

    task_definition = create_task_definition()
    task_definition_arn = register_task_definition(task_definition)
    if not task_definition_arn:
        return

    run_ecs_service(cluster_name, task_definition_arn)

if __name__ == "__main__":
    deploy_app()
