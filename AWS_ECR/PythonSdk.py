import boto3
from botocore.exceptions import ClientError

# Create an ECR client
ecr_client = boto3.client('ecr', region_name='ap-northeast-1')  # Replace with your region

def create_ecr_repository(repository_name):
    try:
        # Create a repository
        response = ecr_client.create_repository(
            repositoryName=repository_name,
            imageScanningConfiguration={
                'scanOnPush': True  # Enable image scanning on push
            },
            imageTagMutability='IMMUTABLE'  # Make the image tags immutable
        )
        print(f"Repository '{repository_name}' created successfully!")
        print(response)  # Optional: print the response for details

    except ClientError as e:
        print(f"Error creating repository: {e}")

# Replace 'flask-app-repo' with your repository name
repository_name = 'flask-app-repo-sdk'
create_ecr_repository(repository_name)
