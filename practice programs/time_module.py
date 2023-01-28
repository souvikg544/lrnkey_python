import time

start=time.time()
print(int(start))

while(True):
    pt = time.time() # Shortcut for present time
    if((int(pt)-int(start)) == 1):
        print("tick")
        start = pt
