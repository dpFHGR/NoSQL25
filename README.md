# Management of Monitoring Templates using a MongoDB and FastAPI in Python
Welcome to this GitHub page on building a Webstack to manage a MongoDB for Monitoring Templates. This is part of the lecture NoSQL of the B.Sc. CDS study course at FHGR.

# Setup
Before you get started, please sign up for MongoDB Atlas as a free user under the following link:
```
https://www.mongodb.com/lp/cloud/atlas/try4-reg?utm_source=google&utm_campaign=search_gs_pl_evergreen_atlas_core-high-int_prosp-brand_gic-null_ww-tier4_ps-all_desktop_eng_lead&utm_term=mongodb%20atlas&utm_medium=cpc_paid_search&utm_ad=e&utm_ad_campaign_id=22031347578&adgroup=173739098633&cq_cmp=22031347578&gad_source=1&gclid=EAIaIQobChMIv526kIy1jAMV8Z2DBx3UPTkXEAAYASAAEgI95vD_BwE
```
## MongoDB Atlas
1. Create Database
2. Choose free plan
3. Choose any provider -> The code was test using AWS
4. Select the closest region
5. Provide a name for your cluster
6. After creating, you can now set a username and password
7. Finish and connect to your cluster

## Updating .env file
Please update the .env file using your username and password

There are 5 files uploaded in this repository: 4 Python files (main.py, routes.py, models.py, db.py), 1 environment file (.env)

atlas -> cluster -> note password -> connect -> .env -> text.md -> replace password with yours

##  Further Setup & Installation (on Pycharm/ VS code Terminal)
Clone the github link using the following command:
```
git clone https://github.com/dpFHGR/NoSQL25
```
Navigate to the NoSQL-Project folder:
```
cd NoSQL-Project
```
Create a Virtual Environment:
```
python -m venv venv
```
Navigate to the venv file:

On MacOS/Linux:
```
source venv/bin/activate
```
Or on Windows:
```
venv\Scripts\activate # On Windows
```
Install Dependencies:
```
pip install -r requirements.txt
```
Start the MongoDB Database:
We have to ensure that MongoDB is running locally or via Docker:
```
docker run -d -p 27017:27017 --name mongodb mongo
```
Run the FastAPI Application:
```
uvicorn main:app --reload
```
Access API Documentation:
Once the app is running, click on the link to the browser from the terminal and add "/docs" to the end of the URL like this:
"http://127.0.0.1:8000/docs" and press ENTER
