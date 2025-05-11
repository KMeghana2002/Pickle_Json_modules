import pickle
with open("C:/Users/HP/OneDrive/Desktop/Python_Idle/PICKLE/pick1.pkl",'rb') as fobj:
    content=fobj.read()
    pyobj=pickle.loads(content)
    print(pyobj)
