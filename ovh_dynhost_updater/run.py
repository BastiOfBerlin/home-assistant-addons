#!/usr/bin/env python3
#https://www.ovh.com/auth/api/createToken?GET=/domain/zone/*&PUT=/domain/zone/*&POST=/domain/zone/*
import ovh
import json
import requests

with open('/data/options.json', 'r') as f:
  config = json.load(f)

application_key=config['applicationKey']
application_secret=config['applicationSecret']
consumer_key=config['consumerKey']

zoneName=config['zoneName']
subDomain=config['subDomain']
endpoint=config['endpoint']
ip4=config['ip4']
ip6=config['ip6']

client = ovh.Client(
  endpoint=endpoint,
  application_key=application_key,
  application_secret=application_secret,
  consumer_key=consumer_key,
)

if ip4:
  newIP4=requests.get("https://api4.ipify.org").content.decode()
  print(f'IPv4: {newIP4}\n')
  result = client.get(f'/domain/zone/{zoneName}/record', fieldType='A',subDomain=subDomain)
  recordID=result[0]
  client.put(f'/domain/zone/{zoneName}/record/{recordID}',subDomain=subDomain,target=newIP4,ttl=0)

if ip6:
  newIP6=requests.get("https://api6.ipify.org").content.decode()
  print(f'IPv6: {newIP6}\n')
  result = client.get(f'/domain/zone/{zoneName}/record', fieldType='AAAA',subDomain=subDomain)
  recordID=result[0]
  client.put(f'/domain/zone/{zoneName}/record/{recordID}',subDomain=subDomain,target=newIP6,ttl=0)

client.post(f'/domain/zone/{zoneName}/refresh')
