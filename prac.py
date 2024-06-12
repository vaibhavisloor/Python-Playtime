# a=['a','b','c']
# # print(int(a))
# a=[1,2,3]
# print(list(reversed(a)))

# b="abcdef"
# print(list(reversed(b)))

# c=''.join('a')
# print(c)

# num='123'

# zeros=5

# final = num + "0" * zeros
# print(final)

# print(reversed('1234'))


# import os

# for i in os.environ.items():
#     print(i)



import http.client

conn = http.client.HTTPSConnection("seeking-alpha.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "cd576afc48msh58f4250c29fc302p1d5e78jsn59447521b8d0",
    'x-rapidapi-host': "seeking-alpha.p.rapidapi.com"
}

conn.request("GET", "/market/get-realtime-quotes?sa_ids=612888%2C16123", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))