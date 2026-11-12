import random
import time
timer = 0
y = "#"
WhileCheck = True
while WhileCheck: 
    timer = timer + 1
    time.sleep(0.1)
    x = random.randint(0,100)
    if x <= 80:
        print(y*x)
    else:
        print(y*x,"движение")
    
    if timer == 100:
        WhileCheck = False

    
    



    


    