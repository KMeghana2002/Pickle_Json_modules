import pickle
d={'name':['poornima'],'age':[12]}
with open('pick.pkl','wb') as fobj:
    content=pickle.dumps(d)
    fobj.write(content)
