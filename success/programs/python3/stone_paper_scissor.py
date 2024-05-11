# stone paper scissor game between 2 players
print("'stone' 'paper' 'scissor'")
a = input("Ram enter your value : ")
b = input("Shyam enter your value : ")

if a == 'stone':
    while b == 'stone':
        print("Match ties")
        break
    while b == 'paper':
        print("Shyam wins")
        break
    while b =='scissor' :
        print("Ram wins")
        break


if a == 'paper':
    while b == 'stone':
        print("Ram wins")
        break
    while b == 'paper':
        print("Match ties")
        break
    while b =='scissor' :
        print("Shyam wins")
        break
  
        
if a == 'scissor':
    while b == 'stone':
        print("Shyam wins")
        break
    while b == 'paper':
        print("Ram wins")
        break
    while b =='scissor' :
        print("Match ties")
        break
     