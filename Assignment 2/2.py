j1=int(input("Enter the capacity of jug 1: "))
j2=int(input("Enter the capacity of jug 2: "))
j3=int(input("Enter the capacity of jug 3: "))
g=int(input("Enter the final goal amount capacity to be measured: "))

def display():
  print("\nSelect the rule which nedds to be applied");
  print("Rule 1 : Empty jug 1")
  print("Rule 2 : Empty jug 2")
  print("Rule 3 : Empty jug 3")
  print("Rule 4 : Transfer whole content of jug 1 to jug 2")
  print("Rule 5 : Transfer whole content of jug 2 to jug 1")
  print("Rule 6 : Transfer whole content of jug 1 to jug 3")
  print("Rule 7 : Transfer whole content of jug 3 to jug 1")
  print("Rule 8 : Transfer whole content of jug 2 to jug 3")
  print("Rule 9 : Transfer whole content of jug 3 to jug 2")
  print("Rule 10 : Transfer some water from jug 1 to jug 2 until jug 2 is full")
  print("Rule 11 : Transfer some water from jug 2 to jug 1 until jug 1 is full")
  print("Rule 12 : Transfer some water from jug 1 to jug 3 until jug 3 is full")
  print("Rule 13 : Transfer some water from jug 3 to jug 1 until jug 1 is full")
  print("Rule 14 : Transfer some water from jug 2 to jug 3 until jug 3 is full")
  print("Rule 15 : Transfer some water from jug 3 to jug 2 until jug 2 is full")

def apply_rule(ch,x,y,z):
  if (ch==1):
    if(x>0):
      return 0,y,z
    else:
      print("The rule could not be applied")
      return x,y,z
#------------------------------------------------
  elif(ch==2):
    if(y>0):
      return x,0,z
    else:
      print("The rule could not be applied")
      return x,y
#------------------------------------------------
  elif(ch==3):
    if(z>0):
      return x,y,0
    else:
      print("The rule could not be applied")
      return x,y,z
#----------------------------------------------
  elif(ch==4):
    if(x>0 and (x+y)<=j2):
      return 0,x+y,z
    else:
      print("The rule could not be applied")
      return x,y,z
#---------------------------------------------
  elif(ch==5):
    if(y>0 and (x+y)<=j1):
      return x+y,0,z
    else:
      print("The rule could not be applied")
      return x,y,z
#----------------------------------------------
  elif(ch==6):
    if(x>0 and (x+z)<=j3):
      return 0,y,x+z
    else:
      print("The rule could not be applied")
      return x,y,z
#---------------------------------------------
  elif(ch==7):
    if(z>0 and (x+z)<=j1):
      return x+z,y,0
    else:
      print("The rule could not be applied")
      return x,y,z
#----------------------------------------------
  elif(ch==8):
    if(y>0 and (y+z)<=j3):
      return x,0,y+z
    else:
      print("The rule could not be applied")
      return x,y,z
#---------------------------------------------
  elif(ch==9):
    if(z>0 and (y+z)<=j2):
      return x,y+z,0
    else:
      print("The rule could not be applied")
      return x,y,z
#--------------------------------------------1&2
  elif(ch==10):
    if(x>0 and (x+y)>=j2):
      return x-(j2-y),j2,z
    else:
      print("The rule could not be applied")
      return x,y,z
#-------------------------------------------
  elif(ch==11):
    if(y>0 and (x+y)>=j1):
      return x-(j1-x),j1,z
    else:
      print("The rule could not be applied")
      return x,y,z
#--------------------------------------------1&3
  elif(ch==12):
    if(x>0 and (x+z)>=j3):
      return x-(j3-z),y,j3
    else:
      print("The rule could not be applied")
      return x,y,z
#-------------------------------------------
  elif(ch==13):
    if(z>0 and (x+z)>=j1):
      return x-(j1-x),y,j1
    else:
      print("The rule could not be applied")
      return x,y,z
#--------------------------------------------2&3
  elif(ch==14):
    if(y>0 and (y+z)>=j3):
      return x,y-(j3-z),j3
    else:
      print("The rule could not be applied")
      return x,y,z
#-------------------------------------------
  elif(ch==15):
    if(z>0 and (y+z)>=j2):
      return x,y-(j2-y),j2
    else:
      print("The rule could not be applied")
      return x,y,z
#------------------------------------------
  else:
    print("The choice is invalid!!")


x=12
y=z=0 
while(True):
  if(x==g):
    print("GOAL STATE ACHIEVED SUCCESSFULLY!!")
    break
  else:
    display()
    ch=int(input("Enter the rule to be applied from the list : "))
    x,y,z=apply_rule(ch,x,y,z)
    print("\nCurrent Status",end=" ")
    print(x,y,z)