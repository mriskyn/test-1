import json, datetime

def toJSON(data):
  return json.loads(json.dumps(data, default=lambda o: o.__dict__, sort_keys=True, indent=4))

def datetimeNowFormatted():
  return datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")