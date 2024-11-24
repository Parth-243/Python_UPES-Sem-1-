import pickle

list1=['P','A',"Parth",1,2,3,4]
with open("data.pickle", "wb") as file:
    # Pickle the Python object and save it to file
    pickle.dump(list1, file)