"""
Configuration information regarding client and envs
"""
import os

from dotenv import load_dotenv
from opensearchpy import OpenSearch

load_dotenv()

INDEX_NAME = "epicurious-recipes"
SERVICE_URI = os.getenv("SERVICE_URI")
if SERVICE_URI == "https://user:pass@hostname:port" or SERVICE_URI is None:
    print(f"Update SERVICE_URI to your cluster uri. Current value for SERVICE_URI={SERVICE_URI}")
    exit(-1)

client = OpenSearch(SERVICE_URI, use_ssl=True)
