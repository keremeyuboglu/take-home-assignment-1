from dotenv import dotenv_values,load_dotenv 
import json
import os

load_dotenv()
config = dotenv_values(".env")  # config = {"USER": "foo", "EMAIL": "foo@example.org"}
print(json.dumps(config, indent=4))
print(os.environ)
