import requests  # Popular library for making HTTP requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url  # Initialize an instance variable

    def get_response_body(self):
        response = requests.get(self.url)  # Use the 'requests.get' function to send a GET request to the URL
        return response

    def load_json(self):
        response_body = self.get_response_body()  # calling the previous method
        return response_body.json()  # Convert the response content to JSON
        
        

# if __name__ == "__main__":
url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
requester = GetRequester(url)

response_body = requester.get_response_body()
print(response_body)

json_data = requester.load_json()
print(json_data)