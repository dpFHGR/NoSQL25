# Management of Monitoring Templates using a MongoDB and FastAPI in Python
Welcome to this GitHub page on building a Webstack to manage a MongoDB for Monitoring Templates. This is part of the lecture NoSQL of the B.Sc. CDS study course at FHGR.

# Setup
Before you get started, please sign up for MongoDB Atlas as a free user under the following link:
```
https://www.mongodb.com/lp/cloud/atlas/try4-reg?utm_source=google&utm_campaign=search_gs_pl_evergreen_atlas_core-high-int_prosp-brand_gic-null_ww-tier4_ps-all_desktop_eng_lead&utm_term=mongodb%20atlas&utm_medium=cpc_paid_search&utm_ad=e&utm_ad_campaign_id=22031347578&adgroup=173739098633&cq_cmp=22031347578&gad_source=1&gclid=EAIaIQobChMIv526kIy1jAMV8Z2DBx3UPTkXEAAYASAAEgI95vD_BwE
```
## MongoDB Atlas Setup
1. On the left side of the page, under "DEPLOYMENT" click on Database and then click on the "Build a Database" button shown in the centre of the page.
2. Three different configuration options are shown, so we will choose the free plan, i.e. M0: FREE.
3. Three providers are shown, select any provider of your choice-> The code was tested using "aws"
4. Select the closest region.
5. Provide a name for your cluster and click "Create" shown at the botton of the page.
6. After creating, you can now set a username and password and click "Create User".
7. Finally, click on the "Finish and Close" button shown at the bottom of the page, a pop up message will appear, click on "Go to Databases", check for the cluster name you've given earlier and click on "Connect" located next to the cluster name to connect to your cluster.

#### There are 5 files uploaded in this repository: 4 Python files (main.py, routes.py, models.py, db.py) and 1 environment file (.env)
#### Open main.py, db.py, models.py, routes.py and .env in Pycharm or Visual Studio code and open Terminal of the respective IDE.

## Updating .env file
Please update the .env file using your username and password

##  Further Setup & Installation (on Pycharm/ Visual Studio code Terminal)
1. Clone the github link using the following command:
```
git clone https://github.com/dpFHGR/NoSQL25
```
2. Navigate to the NoSQL-Project folder:
```
cd NoSQL-Project
```
3. Create a Virtual Environment:
```
python -m venv venv
```
4. Navigate to the venv file:

On MacOS/Linux:
```
source venv/bin/activate
```
Or on Windows:
```
venv\Scripts\activate # On Windows
```
5. Install Dependencies:
```
pip install -r requirements.txt
```
6. Start the MongoDB Database:

We have to ensure that MongoDB is running locally or via Docker:
```
docker run -d -p 27017:27017 --name mongodb mongo
```
7. Run the FastAPI Application:
```
uvicorn main:app --reload
```
8. Access API Documentation:

Once the app is running, click on the link to the browser from the terminal and add "/docs" to the end of the URL like this: "http://127.0.0.1:8000/docs" and press ENTER
