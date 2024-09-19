# FIRST RUN THIS COMMAND
`python`
This will open windows store and install __PYTHON__

# THEN RUN THIS COMMANDS IN ORDER
mkdir flask_api_project
cd flask_api_project
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install flask requests flask-sqlalchemy
mkdir templates

# RUN THIS TO INITIALIZE THE DATABASE
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
python init_db.py

# RUN THIS TO RUN THE PROJECT
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
python app.py