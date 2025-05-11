import pickle
d={'name':['ramprasad','sudha'],'age':[44,50]}
with open('pick1.pkl','wb') as fobj:
    content=pickle.dump(d,fobj)
    
