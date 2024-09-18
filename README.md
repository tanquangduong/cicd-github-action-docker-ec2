# cicd-github-action-docker-ec2
Example use case of CI-CD: GitHub Action x Docker x EX2 AWS 

## Create and configure EC2 instance
- Create a pair key
    - For example: ec2-key.pem
    - Save it the your PC and use it to connect with the ec2 instance
    - Save it to AWS_PRIVATE_KEY in Github Action Key and Varibale for CD process
- Set up In-bound security group
    - For example, port 8501 for Streamlit app
- IAM role for EC2
    - SSMFullAccess
    - SSMManagedInstanceCore

## Docker Hub
- Create a Docker Hub repository
- Create a Docker Token for login from Github Action to build and push and EC2 to pull and build

## Set Key and/or variables in Github Action
- DOCKERHUB_USERNAME
- DOCKERHUB_TOKEN
- AWS_EC2_KEY # Put here the values in key.pem file
- AWS_EC2_HOST # like ec2-XX-XXX-XX-XXX.eu-west-3.compute.amazonaws.com
- AWS_EC2_USERNAME # here 'ubuntu'


## Connect EC2 instance from WSL in Window
- Install Ubuntu WSL from Microsoft Store in Window
- Open installed Ubuntu terminal for the first time and configure your username and password
- WSL will then be displayed in the VSCode terminal
- Open WSL terminal and start the connection to EC2 instance using *.pem file
- Change permission
    - chmod 400 ec2-key.pem
    - if we can not change its permission that is because of the .pem file stay in the window system, you should move it into ubuntu root folder
        - mv /mnt/c/Users/YourUsername/path/to/ec2-key.pem ~/ec2-key.pem
        - chmod 400 ec2-key.pem
- Connect to ec2 instance
    - ssh -i "ec2-key.pem" ubuntu@ec2-15-188-52-171.eu-west-3.compute.amazonaws.com

## Install Miniconda in EC2 instance
- Download latest miniconda installer
    - wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
- Verify the installer (optional)
    - sha256sum Miniconda3-latest-Linux-x86_64.sh
- Run installer
    - chmod +x Miniconda3-latest-Linux-x86_64.sh
    - ./Miniconda3-latest-Linux-x86_64.sh
- Initialize Conda for your shell
    - /home/ubuntu/miniconda3/bin/conda init
- Source your shell configuration file to apply the changes
    - source ~/.bashrc
- Verify that Conda is recognized
    - conda --version

- Test app
    - http://XX.XXX.XXX.XXX:8501/

## Install and configure Docker in EC2 instance
- Install Docker
    - sudo apt-get update
    - sudo apt-get install -y docker.io
    - sudo systemctl start docker
    - sudo systemctl enable docker
- Add the User to the Docker Group:
    - sudo usermod -aG docker $USER
- Disconnect and reconnect to your EC2 instance.
    - exit
- Verify Docker Group Membership:
    - groups
    - You should see docker listed among the groups.

## Common command line for Docker, here 'mlops' is, for example, the Docker image repository in Docker hub 
- Pull Docker image
    - docker pull ${{ secrets.DOCKERHUB_USERNAME }}/mlops:latest
- Run Docker container, name it as 'mlops-container'
    - docker run --name mlops-container -d -p 8501:8501 ${{ secrets.DOCKERHUB_USERNAME }}/mlops:latest
    - docker run --name cicd-container -d -p 8501:8501 duongtanquang/cicd_ec2:latest
- Check Docker log
    - docker logs cicd-container
- Stop Docker container
    - docker stop cicd-container || true
- Remove Docker container
    - docker rm cicd-container || true
    -

