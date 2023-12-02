from typing import Type, List, Dict, Any
from mongoengine import Document
import requests


def fetch_and_store_data(api_endpoint: str, model_class: Type[Document]) -> None:
    if model_class.objects.count() == 0:
        print(f"Fetching data from {api_endpoint}")
        response = requests.get(api_endpoint)
        data_items: List[Dict[str, Any]] = response.json()

        for item in data_items:
            model_instance = model_class(data=item)
            model_instance.save()
