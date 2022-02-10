import datetime as dt
import time

# print("Hello World!")

print("App started")
run = True
counter = 0
while run == True:
    print("Count: " + str(counter))
    print("System time: " + str(dt.datetime.now()))
    time.sleep(5)
    counter+=1

    # currenttime = dt.datetime.now()
    # if currenttime.second == 0 and currenttime.second % 10 == 0:
    #     print(currenttime)
    #     print("Hello World21!")
