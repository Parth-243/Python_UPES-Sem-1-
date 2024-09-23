import requests


def download_file(url, file_name):
    # Send a GET request to the provided URL
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Open a local file in binary write mode and save the content
        with open(file_name, 'wb') as file:
            file.write(response.content)
        print(f"File '{file_name}' downloaded successfully.")
    else:
        print(f"Failed to download file. Status code: {response.status_code}")#Example usage


if __name__ == "__main__":
	url = 'https://morth.nic.in/sites/default/files/dd12-13_0.pdf'
	file_name = 'file.pdf'
	download_file(url, file_name)
