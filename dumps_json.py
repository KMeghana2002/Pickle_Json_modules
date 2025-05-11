import json
d={'name':['megha','varsha','vamshi'],'age':[23,20,15]}
with open('json_file.json','w') as fobj:
    content=json.dumps(d,indent=4)
    fobj.write(content)
