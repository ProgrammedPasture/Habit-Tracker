import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"

token_id = "abcdefghi123"
pixela_username = "brandonlee"
Graph_id = "graph1"

user_params = {
    "token": token_id,
    "username": pixela_username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(url=pixela_endpoint, json=user_params)
#print(response.text)


graphics_endpoint = f"{pixela_endpoint}/{pixela_username}/graphs"

graphics_params = {
    "id": Graph_id,
    "name": "Reading Graph",
    "unit": "words",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": token_id,
}


#graph_request = requests.post(url=graphics_endpoint, json=graphics_params, headers=headers)
# print(graph_request.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{pixela_username}/graphs/{Graph_id}"

today = datetime.today().strftime("%Y-%m-%d")

pixel_data = {
    "date": today,
    "quantity": "15"
}

# request_pixel = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(request_pixel.text)

update_endpoint = f"{pixela_endpoint}/{pixela_username}/graphs/{Graph_id}/{today}"

new_pixel_data = {
    "quantity": "13",
}

# request_put = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(request_put.text)

delete_endpoint = f"{pixela_endpoint}/{pixela_username}/graphs/{Graph_id}/{today}"

requests_delete = requests.delete(url=update_endpoint, headers=headers)
print(requests_delete.text)