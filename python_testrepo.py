print("Hello world")
print("This is a test repository in Python helping snail reach top of the well!!!")
import random
distance = int(input("Enter the distance to the Top:"))
trial = int(input("Enter Number of Trials:"))
up = [2,3,4,5]
down = [-1,-2,-3]
climb_up = 0
climb_down = 0
current_time = 0
current_distance = 0
final = 0
print(current_time, climb_up,climb_down,current_distance)
for i in range(1,trial + 1):
    while (current_distance<distance):
    
        current_time+=1
        climb_up = random.choice(up)
        climb_down = random.choice(down)
        current_distance = current_distance + climb_up + climb_down
        print(current_time, climb_up,climb_down,current_distance)
        
    
    final = final + current_time
    print("Travel time for Trial",i, "is:", current_time, "minutes")   
    current_distance = 0
    current_time = 0
    
    
    
print("The average travel time for", trial, "trials is",final/trial, "minutes")