import json
d={'name':['raghu','laxmi'],'place':['raichur','gadhwal']}
with open('json1_file.json','w') as fobj:
    json.dump(d,fobj,indent=4)
