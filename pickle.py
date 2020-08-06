import pickle

numba = 49

msg = pickle.dumps(numba)

print(msg)

message = pickle.loads(msg)

print(message)
