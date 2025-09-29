print(7 ==7)
# Branching in Python
floor ="sticky"
walls ="clean"
if floor == "sticky":
    print("clean the floor")
    
val = 3 

if val == 1:
    print("val is one")
elif val == 2:
    print("val is two")
else:
    print("Val is neither one nor two")

while True:
    color = input('Enter "green", "yellow", "red" (or q to quit): ').lower()
    print(f"The user entered {color}")


    if color == "green":
        print("Go")
    elif color == "yellow":
        print("Slow down")
    elif color == "red":
        print("Stop")
    else:
        print("Bogus!")
        break
    
# control flow looping
names = ["Emily", "Jack", "Sophia", "Ethan"];
for name in names:
    print(name)

num = 1

while num >= 10:
    print(num)
    num += 1
  
     
things = ["computer", "colleague", "chair", "spider", "desk"]
for thing in things:
    if thing == "colleague":
        print("Oh, that's just my friend, carry on")
        continue
    elif thing == "spider":
        print("Eek! A spider! Burn it down!")
        break
    print(f"there is a {thing} in my room")

for num in range(5):
    print(num)

for odd in range(3, 12, 2):
    print(odd)