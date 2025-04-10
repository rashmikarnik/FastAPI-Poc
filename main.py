import os
from typing import Union
from dotenv import load_dotenv
from fastapi import FastAPI
from google.oauth2 import service_account
from google.cloud import bigquery


# Load environment variables from .env file
env_file = ".env.dev"
load_dotenv(env_file)

# Get the ENVIRONMENT variable
environment = os.getenv("ENVIRONMENT")
if(environment=="dev"):
    load_dotenv=(".env.dev")
else:
    load_dotenv=(".env.prod")

app = FastAPI()

# Uncomment when running locally
# credentials_path = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
# big_query_client = bigquery.Client.from_service_account_json(credentials_path)
big_query_client = bigquery.Client()


# Uncomment when running locally
# @app.get("/")
# async def root():
#     #get creds
   
#     if(credentials_path):
#         credentials = service_account.Credentials.from_service_account_file(credentials_path)
#         return {"message": "Google creds loaded successfully"}
#     else:
#         return {"message": "Google creds not found"}
    
@app.get("/bigquerydata")
# connect to big query
def bigquery_data():
    query = "SELECT * FROM `inlaid-goods-451523-i3.githubAction_example.test-masking`"
    query_job = big_query_client.query(query)
    results = list(query_job.result())
    return [dict(row) for row in results]
    

@app.get("/test")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)