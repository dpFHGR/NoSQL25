# Management of Monitoring Templates using a MongoDB database and FastAPI in Python
Welcome to this GitHub page on building a Webstack to manage Monitoring Templates using MongoDB and FastAPI. This is part of the lecture NoSQL of the B.Sc. CDS study course at FHGR.

# Use Case: Repository for Monitoring Templates
A Hospital is in the process of setting up and expanding a monitoring solution on various platforms, such as "PRTG" and "Zabbix" (Monitoring tools). Various monitoring points/definitions are being created here and need to be centrally managed. This application serves as a repository to manage the monitoring templates across different tools. It also tracks which servers use which templates, providing better visibility into which monitoring points are active on which systems.

The aim is to ensure that the ICT employees of this hospital have access to this repository so that they can assess the various existing monitoring points for their purposes.

## Methodology
There are 6 files uploaded in this repository: 3 Python files (main.py, routes.py, models.py), 1 environment file (.env), 1 Dockerfile and 1 docker-compose.yml file.
-main.py: Intitializes the app and loads routers
-routes.py: Defines API endpoints
-models.py: Contains Pydantic models
-.env: Environment variables
-Dockerfile: Builds the FastAPI app image
-docker-compose.yml: Manages MongoDB and FastAPI services
Along with the main branch, 2 side branches were used for development(feat_entities, search_function).

Data Dumping:
1. With "docker exec -it mongodb mongodump --db monitoring_db --out /data/db/dump", we can create the dump on the container which we cannot see.
2. With "mkdir .\mongo_dump", a new Folder in the NoSQL25 Folder is created.
3. With "docker cp mongodb:/data/db/dump .\mongo_dump", we copy the Dump locally.

## Setup
Before you get started, please download Docker Desktop on your system:
```
https://www.docker.com/
```
Make sure Docker Desktop is running before proceeding.

##  Further Setup
1. Open a terminal (command prompt/ git bash or any other).
2. Navigate to your desired folder using "cd" (eg: cd Documents).
3. With "dir" you can check contents of the Directory while navigating.
4. Clone the repository using the following command:
```
git clone https://github.com/dpFHGR/NoSQL25
```
5. Right click the cloned NoSQL25 Folder and select open as Pycharm / Visual Studio Code.
6. Alternatively, open Pycharm / VS Code and open the NoSQL25 Folder as Project.
7. Go to the terminal of Pycharm / VS Code
8. Run the following command to build the Docker images:
```
docker compose build
```
9. Start the containers in detached mode:
```
docker-compose up -d
```
10. Finally, copy the given URL below, paste it into the address bar, and press ENTER to access the API:
```
http://localhost:8008/docs
```

## How to use this API?

