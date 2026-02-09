f1=open("menu.txt","r")
lines=f1.readlines()
Menu=[]
for line in lines:
    cleaned_lines=line
    Menu.append(line.strip())
    
    f1.close()
print(Menu)

def save_menu(Menu):
    f = open("menu.txt", "w")
    for item in Menu:
        f.write(item + "\n")
    f.close()

print("0.add")
print("1.view")
print("2.delete")
print("3.stop")

def Add():
              task=str(input("add a task to menu: "))
              Menu.append(task)
              save_menu(Menu)
              print("task is added")
def view():
           if len(Menu)==0:
             print("no tasks available in Menu")
           else:
             for i in range(len(Menu)):
                 print(i,Menu[i])
def Delete_stop():
             
             if len(Menu)==0:
                 print("no tasks available to Delete")
             else:
                 delete=int(input("which task should be deleted ? "))
                 if delete in range(len(Menu)):
                      Menu.pop(delete)
                      save_menu(Menu)
                      print("task is Deleted")
                      print(Menu)

while True:
    choose=int(input("choose a task :"))
    if choose==0:
        Add()
    elif choose==1:
        view()
    elif choose==2:
        Delete_stop()
    elif choose==3:
        print("Bye")
        break
    else:
        print("invalid number")





    
  
    