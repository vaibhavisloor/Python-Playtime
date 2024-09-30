import requests

pixela_endpoint = 'https://pixe.la/v1/users'

user_params={
    "token":"ABCdef123!@#",
    "username":"vaibhav-123",
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

# response = requests.post(url=pixela_endpoint,json=user_params)


graph_endpoint = f"{pixela_endpoint}/vaibhav-123/graphs"

graph_params={
"id":"id1",
"name":"Coding Hours",
"unit":"Hours",
"type":"int",
"color":"sora",
"timezone":"Asia/Kolkata",

}

headers={
    "X-USER-TOKEN":"ABCdef123!@#"
}

# response1 = requests.post(url=graph_endpoint,json=graph_params, headers = headers )

# print(response)
# print(response1)

# https://pixe.la/v1/users/vaibhav-123/graphs/id1.html



add_pixel_endpoint = f"{graph_endpoint}/id1"

pixel_params = {
"date":"20240621",
"quantity":"2"
}

response = requests.post(url = add_pixel_endpoint,json=pixel_params,headers=headers)

print(response)