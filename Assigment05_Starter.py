# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# DZeng, 8.9.2023,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
fileName = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# Note: Assumes that the "ToDoList.txt" file exists in the same directory as script
fileObj = open(fileName, "r")
for line in fileObj:
    lineData = line.split(",")
    dicRow = {"Task":lineData[0].strip(), "Priority": lineData[1].strip()}
    lstTable.append(dicRow)
fileObj.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print("Task|Priority")
        for entry in lstTable:
            print(entry["Task"] + "|" + entry["Priority"])
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        taskInput = input("Enter the task: ").strip()
        priorityInput = input("Enter the priority: ").strip()
        dicRow = {"Task":taskInput, "Priority":priorityInput}
        lstTable.append(dicRow)
        print("New entry added")
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        taskInput = input("Enter the task to be removed: ")
        for entry in lstTable:
            if entry["Task"] == taskInput:
                lstTable.remove(entry)
                print("Entry removed")
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        fileObj = open(fileName, "w")
        for entry in lstTable:
            fileObj.write(entry["Task"] + "," + entry["Priority"] + "\n")
        fileObj.close()
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        break  # and Exit the program
