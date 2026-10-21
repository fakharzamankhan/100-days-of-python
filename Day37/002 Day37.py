import requests
from datetime import datetime
pixela_endpoint="https://pixe.la/v1/users"
USER_NAME="fakhar"
TOKEN="asjjsdbdjwkdjkad"
GRAPH_ID="graph1"

user_params={
    "token":TOKEN,
    "username":USER_NAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"

}


# response=requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

graph_endpoint=f"{pixela_endpoint}/{USER_NAME}/graph"

graph_configuration={
    "id":GRAPH_ID,
    "name": "Cycling_graph",
    "unit":"Km",
    "type": "float",
    "color":"ajisai",

}

headers = {
    "X-USER-TOKEN":TOKEN
}
# response=requests.post(url=graph_endpoint,json=graph_configuration,headers=headers)
# print(response.text)

pixel_creation_endpoint=f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"

today = datetime.now()
# today=datetime(year=2026,month=9,day=13)

pixel_data={
    "date":today.strftime("%Y%m%d"),
    "quantity": input("how many kilometers did you cycle today?"),
}

# response=requests.post(url=pixel_creation_endpoint,json=pixel_data,headers=headers)
# print(response.text)

update_endpoint=f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data={
    "quantity": "4.5",

}

# response=requests.put(url=update_endpoint,json=new_pixel_data,headers=headers)
# print(response.text)

delete_endpoint=f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
response=requests.delete(url=delete_endpoint,headers=headers)
print(response.text)

