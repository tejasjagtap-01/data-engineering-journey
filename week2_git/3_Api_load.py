import requests
import logging

class APILoader:

    def __init__(self, url):
        self.url = url
        self.data = None

    def fetch(self):
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                self.data = response.json()
                logging.info(f'Fetched {self.url} successfully')
            else:
                logging.error(f'Failed with status code {response.status_code}')
        except requests.exceptions.RequestException as e:
            logging.error(f'Request Failed : {e}')
        return self.data

api = APILoader("https://api.jolpi.ca/ergast/f1/2023/results.json")
api.fetch()
# print(api.data['MRData'])
print(api.data['MRData']['RaceTable']['Races'][0]['Results'][0]['Driver']['familyName'])
print(api.data['MRData']['RaceTable']['Races'][0]['Results'][0]['Constructor']['name'])