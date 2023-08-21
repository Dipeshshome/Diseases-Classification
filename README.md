# Diseases-Classification

## Workflows maintained

1.Update config.yaml<br>
2.Update secrets.yaml [Optional] for database and other crededentials. <br>
3.Update params.yaml <br>
4.Update the entity <br>
5.Update the configuration manager in src config <br>
6.Update the components for data ingestion, model preparation, callbacks, evaluation etc. <br>
7.Update the pipeline <br>
8.Update the main.py <br>
9.Update the dvc.yaml for tracking mlops pipeline.<br>



## Pipeline

1. Stage 1: Data Ingestion stage.<br>
2. Stage 2: Prepare Base Model stage<br>
3. Stage 3: Training<br>
4. Stage 4: Evaluation stage<br>
5. Stage 5: Prediction stage<br>


## DVC Command

1. dvc init.<br>
2. dvc repro.<br>
3. dvc dag.<br>

## Requirements Installation
pip install -r requirements.txt<br>

## Application running
1. python app.py<br>
2. UI training: http://127.0.0.1:8080/train<br>


## About the deployment

1. Build docker image of the source code<br>

2. Push your docker image to ECR<br>

3. Launch Your EC2 <br>

4. Pull Your image from ECR in EC2<br>

5. Lauch your docker image in EC2<br>

#Policy:<br>

1. AmazonEC2ContainerRegistryFullAccess<br>

2. AmazonEC2FullAccess<br>

## Create ECR repo to store/save docker image

Save the URI<br>

## Create ECR repo to store/save docker image
Save the URI

## Create EC2 machine (Ubuntu)

## Open EC2 and Install docker in EC2 Machine:

#optinal<br>

1. sudo apt-get update -y<br>

2. sudo apt-get upgrade<br>

#required<br>

1. curl -fsSL https://get.docker.com -o get-docker.sh<br>

2. sudo sh get-docker.sh<br>

3. sudo usermod -aG docker ubuntu<br>

4. newgrp docker<br>

## Configure EC2 as self-hosted runner:

setting>actions>runner>new self hosted runner> choose os> then run command one by one<br>

## Setup github secrets and variables:

AWS_ACCESS_KEY_ID= <br>

AWS_SECRET_ACCESS_KEY= <br>

AWS_REGION = us-east-1 <br>

AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com <br>

ECR_REPOSITORY_NAME = simple-app <br>






