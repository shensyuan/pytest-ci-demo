# import requests
import json

class DataService:
    def __init__(self, api_url="https://api.example.com"):
        self.api_url = api_url
        self.cache = {}
    
    def get_data(self, key):
        """get data from API or cache"""
        if key in self.cache:
            return self.cache[key]
        
        # 模擬 API 呼叫
        response = requests.get(f"{self.api_url}/data/{key}")
        if response.status_code == 200:
            data = response.json()
            self.cache[key] = data
            return data
        raise Exception(f"Failed to get data for key: {key}")
    
    def save_data(self, key, value):
        """save data to API"""
        response = requests.post(
            f"{self.api_url}/data",
            json={key: value}
        )
        if response.status_code == 201:
            return True
        return False
    
    def get_external_config(self):
        """outside device"""
        response = requests.get(f"{self.api_url}/config")
        return response.json() if response.status_code == 200 else {}