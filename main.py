import requests
def main():
    url = "https://api.github.com/repos/psf/requests"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"Repository: {data['full_name']}")
        print(f"Description: {data['description']}")
        print(f"Stars: {data['stargazers_count']}")
    else:
        print("Failed to retrieve data from GitHub API.")