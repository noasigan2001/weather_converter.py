import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url, timeout=10)

assert response.status_code == 200

data = response.json()

assert data ["id"] == 1
assert "title" in data
assert isinstance(data["title"], str)

print(data)
print ("GET test passed")