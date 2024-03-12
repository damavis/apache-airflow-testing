import requests
from airflow.models.baseoperator import BaseOperator


class CustomOperator(BaseOperator):
    def __init__(self, name: str, **kwargs) -> None:
        super().__init__(**kwargs)
        self.name = name

    def execute(self, context):
        response = requests.get("localhost:8080/test")
        print(response)
        pass
