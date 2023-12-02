from typing import Type, List, Dict, Any, Callable
import json
from mongoengine import Document
import requests


def fetch_and_store_data(api_endpoint: str, model_class: Type[Document], transformer: Callable[[Any], List[Dict[str, Any]]]) -> None:
    if model_class.objects.count() == 0:
        print(f"Fetching data from {api_endpoint}")
        response = requests.get(api_endpoint)
        if response.status_code == 200:
            try:
                data_items: List[Dict[str, Any]] = transformer(response.json())
                for item in data_items:
                    model_instance = model_class(data=item)
                    model_instance.save()
            except json.JSONDecodeError:
                print(f"Error decoding JSON. Response: {response.text}")
                return
        else:
            print(f"Error fetching data: {response.status_code}, Response: {response.text}")
            return
