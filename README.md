There are 5 files uploaded in this repository: 4 Python files (main.py, routes.py, models.py, db.py), 1 environment file (.env)

Setup & Installation (on Pycharm/VS code Terminal)
git clone https://github.com/dpFHGR/NoSQL25
cd NoSQL-Project

Create a Virtual Environment (on Pycharm/VS code Terminal)
python -m venv venv
source venv/bin/activate # On macOS/Linux
venv\Scripts\activate # On Windows

Install Dependencies (on Pycharm/VS code Terminal)
pip install -r requirements.txt

Start the MongoDB Database (on Pycharm/VS code Terminal)
We have to ensure that MongoDB is running locally or via Docker:
docker run -d -p 27017:27017 --name mongodb mongo

Run the FastAPI Application (on Pycharm/VS code Terminal)
uvicorn main:app --reload

Access API Documentation
Once the app is running, click on the link to the browser from the terminal and add "/docs" to the end of the URL like this:
http://127.0.0.1:8000/docs and press ENTER
