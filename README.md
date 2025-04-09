# FastAPI-Poc

1. activate virual env
   1. if python is setup python -m venv .venv - creates .venv folder
   2. add this folder to gitignore
   3. activate virtual environemnt .venv\Scripts\Activate.sh or bash .venv/Scripts/activate for command prompt .venv\Scripts\activate.bat
   4. run this command to check if activated -- which python
1. install fast api -- if installed check version -- pip show fastapi
1. write main.py
1. run code with command -- python -m fastapi dev main.py

# setup debugger for python to run fastAPI

1. get python debugger extension
2. after that select interpreter : from commad palatete python venv
3. set launch.json
4. run -- pip install -r requirements.txt to add all dependencies

5. create requirements.txt --- add fastapi
pip freeze > requirements.txt -- freeze all depencencies
   uvicorn

# without virtual environment

install all the depencencied where python exe is present
c:\\Users\\raskarnik\\AppData\\Local\\Programs\\Python\\Python313\\python.exe -m pip install uvicorn -- install uvicorn
c:\\Users\\raskarnik\\AppData\\Local\\Programs\\Python\\Python313\\python.exe -m pip install fastapi --- fastapi

# Run with debugger
1.select fastAPI python debugger
2. launch.json :
 {
      "name": "Rashmi: FastAPI",
      "type": "debugpy",
      "request": "launch",
      "python": "c:\\Users\\raskarnik\\AppData\\Local\\Programs\\Python\\Python313\\python.exe",
      "module": "uvicorn",
      // "python": "${workspaceFolder}/.venv/Scripts/python.exe",
      "args": ["main:app", "--reload"],
      "jinja": true
    }
3. run by clicking run and debug


# setting up code
1. Run : pip install python-dotenv -- to create env file
2. google auth set up : pip install google-auth google-auth-oauthlib
3. big query : pip install google-cloud-bigquery
4. run service: python -m fastapi dev main.py or through debugger

# create docker image
1. Build the Image: docker build -t your-image-name .. 