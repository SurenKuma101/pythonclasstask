RED="red"
BLUE="blue"
YELLOW="yellow"

colour1=(input("enter first colour"))
colour2=(input("enter the second colour"))

if(colour1=="RED" or colour1=="blue" or colour1=="yellow"):
  print("you entered right colour")
else:
  print("Error:invalid colour1")

if(colour2=="RED" or colour2=="blue" or colour2=="yellow"):
 print("you entered right colour")
else:
 print("Error:invalid color2")

    
if(colour1 == colour2): 
     print("Error: the two colours you entered are the same")
else:
 print("the two color are not same")


if(colour1=="red" and colour2=="blue" ):
    print("purple")
 
elif(colour1=="red" and colour2=="yellow" ):
    print("orange")

elif(colour1=="blue" and colour2=="red" ):
    print("purple")

elif(colour1=="blue" and colour2=="yellow" ):
    print("green")
 
elif(colour1=="yellow" and colour2=="red" ):
    print("orange")

elif(colour1=="yellow" and colour2=="blue" ):
    print("green")

