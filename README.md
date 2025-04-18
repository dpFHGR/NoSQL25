# Management of Monitoring Templates using a MongoDB and FastAPI in Python
Welcome to this GitHub page on building a Webstack to manage Monitoring Templates using MongoDB and FastAPI. This is part of the lecture NoSQL of the B.Sc. CDS study course at FHGR.

## Use Case: Repository for Monitoring Templates
The KSGR (Kantonsspital Graubünden) is in the process of setting up and expanding a monitoring solution on various platforms like "PRTG" and "Zabbix" (Monitoring tools). Various monitoring points/definitions are being created here and need to be centrally managed. This application serves as a repository to manage the monitoring templates across different tools. It also tracks which servers use which templates, allowing better visibility into wwhich monitoring points are active on which systems.

The aim is to ensure that KSGR ICT employees have access to this repository so that they can assess the various possibilities of the existing monitoring points for their purposes.

## Docker Desktop Setup
Before you get started, please download Docker Desktop on your system:
```
https://www.docker.com/
```
Keep the Docker Desktop open for the upcoming docker-compose function to access the API.

##  Further Setup (on Pycharm/ Visual Studio code Terminal)
There are 6 files uploaded in this repository: 3 Python files (main.py, routes.py, models.py), 1 environment file (.env), 1 Dockerfile and 1 docker-compose.yml file.
- Open main.py, models.py, routes.py, .env, Dockerfile and docker-compose.yml files in Pycharm or Visual Studio code.
- Open the terminal in your chosen IDE and you are ready to begin with the commands.

1. Clone the github link using the following command:
```
git clone https://github.com/dpFHGR/NoSQL25
```
2. Navigate to the NoSQL-Project folder:
```
cd NoSQL25
```
3. Create a Virtual Environment:
```
python -m venv venv
```
4. Activate the virtual environment you created:

  On MacOS/Linux:
```
source venv/bin/activate
```
  Or on Windows:
```
venv\Scripts\activate
```
5. Install Dependencies:
```
pip install -r requirements.txt
```
6. Start the MongoDB Database:
   
First, make sure you've got Docker installed on your system.

Then check whether MongoDB is running locally or via Docker:
```
docker run -d -p 27017:27017 --name mongodb mongo
```
7. Run the FastAPI Application:
```
uvicorn main:app --reload
```
8. Access API Documentation:

Once the app is running, click on the link to the browser from the terminal and add "/docs" to the end of the URL like this: "http://127.0.0.1:8000/docs" and press ENTER
