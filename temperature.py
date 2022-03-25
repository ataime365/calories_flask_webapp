from selectorlib import Extractor
import requests


class Temperature:
    """
    Represents a temperature value extracted from the timeanddate.com/weather webpage
    """
    # class variable
    headers = {
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }
    base_url = 'https://www.timeanddate.com/weather/'
    yml_file_path = 'temperature.yaml'

    def __init__(self, country, city):
        self.country = country.replace(" ", "-")  # Instance variable
        self.city = city.replace(" ", "-")

    def _complete_url(self):
        """"Completes the self.base_url by adding country and city"""
        url = f'{self.base_url}{self.country}/{self.city}'
        return url

    def _scrape(self):
        """Extracts the value as instructed by the yml file and returns a dictionary"""
        url = self._complete_url()
        response = requests.get(url, headers=self.headers)
        full_content = response.text
        extractor = Extractor.from_yaml_file(self.yml_file_path)
        raw_value = extractor.extract(full_content)  # extract from an html
        return raw_value

    def get(self):
        """Cleans the output from _scrape method"""
        value = self._scrape()
        cleaned_value = value.get('temp').replace('°C', '').strip()
        cleaned_value = int(cleaned_value)
        return cleaned_value


if __name__ == "__main__":
    temperature = Temperature('italy', 'rome')
    print(temperature.get())
