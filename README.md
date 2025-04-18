# Management of Monitoring Templates using a MongoDB database and FastAPI in Python
Welcome to this GitHub page on building a Webstack to manage Monitoring Templates using MongoDB and FastAPI. This is part of the lecture NoSQL of the B.Sc. CDS study course at FHGR.

# Use Case: Repository for Monitoring Templates
A Hospital is in the process of setting up and expanding a monitoring solution on various platforms, such as "PRTG" and "Zabbix" (Monitoring tools). Various monitoring points/definitions are being created here and need to be centrally managed. This application serves as a repository to manage the monitoring templates across different tools. It also tracks which servers use which templates, providing better visibility into wwhich monitoring points are active on which systems.

The aim is to ensure that the ICT employees of this hospital have access to this repository so that they can assess the various existing monitoring points for their purposes.

## Setup
Before you get started, please download Docker Desktop on your system:
```
https://www.docker.com/
```
Keep the Docker Desktop open for the upcoming docker-compose functions to access the API.

##  Further Setup (on Pycharm/ Visual Studio code Terminal)
There are 6 files uploaded in this repository: 3 Python files (main.py, routes.py, models.py), 1 environment file (.env), 1 Dockerfile and 1 docker-compose.yml file.
- Open main.py, models.py, routes.py, .env, Dockerfile and docker-compose.yml files in Pycharm or Visual Studio code.
- Open the terminal in your chosen IDE and you are ready to start.

1. Clone the github link using the following command:
```
git clone https://github.com/dpFHGR/NoSQL25
```
2. Navigate to the NoSQL-Project folder:
```
cd NoSQL25
```
3. Build the Docker images:
```
docker compose build
```
4. Start the containers in detached mode:
```
docker-compose up -d
```
5. Finally, copy the given URL below, paste it into the address bar, and press ENTER to access the API:
```
http://localhost:8008/docs
```

## How to use this API?
