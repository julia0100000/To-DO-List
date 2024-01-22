#Julia Riesman and Faith Sanders
#1/10/24
#To-Do List


#Init


list = []




#Functions


def add():
       add = input("Add a task: ")
       list.extend(add)
def view():
        print(list)
def complete():
        complete = input("What task would you like to mark as completed?")
        x = int(complete)
        list.insert(x, complete)
def remove():
        remove = input("What would you like to remove?")
        x = int(remove)
        list.pop(x)
def exit():
        quit()


def removeAll():
        list.clear()

def alphabet():
        sorted(list)


def count():
        list.count(list)




def grocery():
        print("Welcome to Your Grocery List")
        print("Please choose an operation: (Type a number between 1-5)")
        print("1. Add a task \n2. View current list \n3. Mark task completed \n4. Remove ONE task  \n5. Remove ALL tasks \n6. Sort the list alphabetically \n7. Print number of items in list \n8.Exit")
        option = int(input("Operation"))
        if option == 1:
                add()
                cont = input("would you like to continue?")
                if cont=="yes":
                    grocery()
                if cont == "no":
                    quit()
        elif option == 2:
                view()
                cont = input("would you like to continue?")
                if cont=="yes":
                    grocery()
                if cont == "no":
                    quit()
        elif option == 3:
                complete()
                cont = input("would you like to continue?")
                if cont=="yes":
                    grocery()
                if cont == "no":
                    quit()
        elif option == 4:
                remove()
                cont = input("would you like to continue?")
                if cont=="yes":
                    grocery()
                if cont == "no":
                    quit()
        elif option == 5:
              removeAll()
              cont = input("would you like to continue?")
              if cont=="yes":
                    grocery()
              if cont == "no":
                    quit()
        elif option == 6:
              alphabet()
              cont = input("would you like to continue?")
              if cont=="yes":
                    grocery()
              if cont == "no":
                    quit()
        elif option == 7:
              count()
              cont = input("would you like to continue?")
              if cont=="yes":
                    grocery()
              if cont == "no":
                    quit()
        elif option == 8:
                exit()




#Main
grocery()  
