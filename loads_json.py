import json
with open("C:/Users/HP/OneDrive/Desktop/Python_Idle/JSON/json_file.json",'r') as fobj:
    content=fobj.read()
    pyobj=json.loads(content)
    print(pyobj)
    
