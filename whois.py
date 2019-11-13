import os
import requests
from xml.dom.minidom import parseString


class Client():
    def __init__(self, api_key=None):
        self.url = 'https://www.whoisxmlapi.com/whoisserver/WhoisService'
        self.api_key = api_key

        if self.api_key is None:
            self.api_key = os.getenv('WHOIS_API_KEY')

    def get(self, domain_name, output_format='JSON'):
        params = dict(
            apiKey=self.api_key,
            domainName=domain_name,
            outputFormat=output_format
        )

        response = requests.get(self.url, params=params)
        if output_format == 'JSON':
            return response.json()

        elif output_format == 'XML':
            return parseString(response.text)

