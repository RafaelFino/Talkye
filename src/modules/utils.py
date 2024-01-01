import ulid
import json

def generateId():
    return ulid.new().str   

def jsonToStr(json):
    return json.dumps(json)

def strToJson(str):
    return json.loads(str)  

def objectToJson(obj):
    return json.dumps(obj.__dict__)