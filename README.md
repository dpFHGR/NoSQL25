# Management of Monitoring Templates using a MongoDB database and FastAPI in Python
Welcome to this GitHub page on building a Webstack to manage Monitoring Templates using MongoDB and FastAPI. This is part of the lecture NoSQL of the B.Sc. CDS study course at FHGR. This project was completed on Windows 11 and all commands were run in Pycharm's terminal or Powershell.

# Use Case: Repository for Monitoring Templates
A Hospital is in the process of setting up and expanding a monitoring solution on various platforms, such as "PRTG" and "Zabbix" (Monitoring tools). Various monitoring points/definitions are being created here and need to be centrally managed. This application serves as a repository to manage the monitoring templates across different tools. It also tracks which servers use which templates, providing better visibility into which monitoring points are active on which systems.

The aim is to ensure that the ICT employees of this hospital have access to this repository so that they can assess the various existing monitoring points for their purposes.

## Contents of this Repository
There are 6 files uploaded in this repository: 3 Python files (main.py, routes.py, models.py), 1 environment file (.env), 1 Dockerfile and 1 docker-compose.yml file.
- main.py: Intitializes the app and loads routers
- routes.py: Defines API endpoints
- models.py: Contains Pydantic models
- .env: Environment variables
- Dockerfile: Builds the FastAPI app image
- docker-compose.yml: Manages MongoDB and FastAPI services
Along with the main branch, 2 side branches were used for development(feat_entities, search_function).

## Setup
Before you get started, please download Docker Desktop on your system:
```
https://www.docker.com/
```
Make sure Docker Desktop is running before proceeding.

##  Further Setup
1. Open a terminal (command prompt/ git bash or any other).
2. Navigate to your desired folder using "cd" (e.g., cd Documents).
3. With "dir" you can check contents of the Directory while navigating.
4. Clone the repository using the following command:
```
git clone https://github.com/dpFHGR/NoSQL25
```
5. Right click the cloned NoSQL25 Folder and select open as Pycharm.
6. Alternatively, open Pycharm and open the NoSQL25 Folder as Project.
7. Go to the terminal of Pycharm
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
Idea: This API helps you to manage monitoring infrastructure by allowing users to register servers, select monitoring tools (Zabbix/PRTG), create templates, and link them together.

1. **Create a User:**
   Navigate to the POST /users endpoint and click on it.
- Click on "Try it out" to open the interactive input form.
- You can modify the default user data or leave it as it is.
- Submit the request by clicking on "Execute" - a new user will be created with a unique ID (automatically generated)
2. **Verify the User:**
  You can use the following endpoints to manage users:
- GET /user/ -> List all users and confirm your new user has been created.
- GET /user/{id} -> Update user data.
- DELETE /user/{id} -> Delete a user.
3. **Choose or Create a Server:**
  Before linking templates, make sure a server exists.
- POST /server/ -> Create a new server.
- GET /server/ -> View all existing servers.
- GET /server/{id} -> Retrieve a specific server by ID.
4. **Choose or Create a Monitoring Tool:**
  The Monitoring tools (e.g., Zabbix, PRTG) are predefined in the system, but you can also add new ones.
- GET /tool/ -> View all available monitoring tools.
- POST /tool/ -> Add a new tool, if needed.
5. **Create or Manage Monitoring Templates:**
  Monitoring templates define what to monitor (e.g., CPU usage, disk space).
- POST /template/ -> Create a new template.
- GET /template/ -> List all templates.
- GET /template/{id} -> Find a specific template by ID.
- PUT /template/{id} -> Update a template.
- DELETE /template/{id} -> Remove a template.
6. **Link Server to Monitoring Template:**
  Once you have a user, tool, and template, link them to a specific server.
- POST /links -> Create a new link between a server and a monitoring template.
  - Required fields: server_id, template_id, tool, and other optional metadata.
- GET /link/server/{server_id} -> View all links associated with a given server.
This effectively connects the server to a monitoring template via the selected tool.

## CURL Commands
After building and running docker compose, instead of accessing the API itself we can run the same test scenario using CURL commands. Since this project was done on Windows and Powershell, Invoke-RestMethod was used instead of CURL. The following is the pipeline:

1. Create a user:
```
$user = Invoke-RestMethod `
  -Uri "http://localhost:8008/user/" `
  -Method Post `
  -ContentType "application/json" `
  -Body (@{
    username   = "Lara"
    email      = "Lara@example.com"
    role       = "Admin"
    created_at = "2025-04-18 10:00:00"
  } | ConvertTo-Json)
```
3. View created user and copy ID
```
$userId = $user._id
Write-Host "User ID is $userId"
```

5. Create Server
```
$server = Invoke-RestMethod `
  -Uri "http://localhost:8008/server/" `
  -Method Post `
  -ContentType "application/json" `
  -Body (@{
    hostname   = "db00"
    ip_address = "0.0.0.0"
    location   = "ICT-A"
    owner_id   = $userId
  } | ConvertTo-Json)
$serverId = $server._id
Write-Host "Server ID is $serverId"
```

7. Create Monitoring tool
```
$tool = Invoke-RestMethod `
  -Uri "http://localhost:8008/tool/" `
  -Method Post `
  -ContentType "application/json" `
  -Body (@{
    name                 = "Zabbix"
    version              = "6.0"
    platform             = "Linux"
    manufacturer         = "Zabbix LLC"
    sys_owner            = "IT Admin"
    serv_name            = "Monitoring-Server-1"
    monitoring_templates = @()
  } | ConvertTo-Json)
$toolId = $tool._id
Write-Host "Tool ID is $toolId"
```

9. Create Monitoring template
```
$template = Invoke-RestMethod `
  -Uri "http://localhost:8008/template/" `
  -Method Post `
  -ContentType "application/json" `
  -Body (@{
    temp_name        = "CPU Load Check"
    description      = "Alert if CPU > 80% for 5 min"
    limit            = 80.0
    unit             = "%"
    time_window      = "5m"
    alerting_method  = "email"
    monitoring_tools = @($toolId)
  } | ConvertTo-Json)
$templateId = $template._id
Write-Host "Template ID is $templateId"
```

10. Create Relationship between template and Server
```
$link = Invoke-RestMethod `
  -Uri "http://localhost:8008/link/" `
  -Method Post `
  -ContentType "application/json" `
  -Body (@{
    server_id   = $serverId
    template_id = $templateId
    tool        = $toolId
    applied_on  = "2025-04-18 12:00:00"
  } | ConvertTo-Json)
Write-Host "Link created."
```

11. Verification listing relationships for the Server
```
Invoke-RestMethod `
  -Uri "http://localhost:8008/link/server/$serverId" `
  -Method Get
```

12. Verification of all entities
```
Invoke-RestMethod -Uri "http://localhost:8008/user/"     -Method Get
Invoke-RestMethod -Uri "http://localhost:8008/server/"   -Method Get
Invoke-RestMethod -Uri "http://localhost:8008/tool/"     -Method Get
Invoke-RestMethod -Uri "http://localhost:8008/template/" -Method Get
```

13. Search function for templates case insensitive
```
Invoke-RestMethod `
  -Uri "http://localhost:8008/template/?q=cPu" `
  -Method Get
```

## Data Dumping
Finally, a data dump was performed to backup and restore the MongoDB database in a Docker container. The following was done:
1. The following command creates the Dump on the container which we cannot see.
```
docker exec -it mongodb mongodump --db monitoring_db --out /data/db/dump
```
3. We can create a new Folder in the NoSQL25 Folder using:
```
mkdir .\mongo_dump
```
5. To copy the Dump locally:
```
docker cp mongodb:/data/db/dump .\mongo_dump
```
## Referrences
1. https://www.youtube.com/watch?app=desktop&v=QkGqjPFIGCA&t=0s
2. https://www.mongodb.com/resources/languages/pymongo-tutorial
3. https://fastapi.tiangolo.com/tutorial/query-params/#multiple-path-and-query-parameters
4. https://medium.com/@mustafaburakaydiin/how-to-backup-and-restore-a-mongodb-database-in-a-docker-container-a7242ba0994f
