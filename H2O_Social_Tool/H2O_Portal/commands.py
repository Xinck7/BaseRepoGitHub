import groupy import Client
token=''
client = Client.from_token(token)
groups = client.groups.list()

for group in client.groups.list_all():
    groupnames = []
    groupnames.append(group)
    print(groupnames)
#ask them for the token on manage creds
