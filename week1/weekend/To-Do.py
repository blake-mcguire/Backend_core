task_list = []                                          #defines list variables
completed_tasks = []


def add_task():                              #Adds Task to a task list 
    try:
        task = input("Enter the Task you would like to add!: ")
        due_date = input("Enter The Due Date: ")
        priority = input("What is the priority level? 1-5: 1 is Highest Priority.")
        if priority.isdigit() and int(priority) in range(1,6):
            task_list.append((task, due_date, priority))
            print(f"You added {task} to your task list!")
        else:
            print('Please Enter a number between 1-5 for priority level')
    except Exception as e:
        print(f"An Error Occured: {e}")                               
    
    
    
def view_task():                                          #Shows the view of tasks that are still open
    if task_list:
        sorted_tasks = sorted(task_list, key=lambda x: x[2])   
        for task in sorted_tasks:
            print(f"""-----------------------------------------------------
Task: {task[0]} -- Due: {task[1]} -- Priority: {task[2]}""")
    else:
        print("Your Task List is empty.")
    
        

def complete_task():                                   #Marks a task as complete
    if task_list:
        
        for index, (task, due_date, priority) in enumerate(task_list):
            print(f"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
{index}: {task}; {due_date}; {priority}""")
        
        try:    
            complete = input("""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Enter The Index of The Task You would like to mark complete: """)
            complete_task = task_list.pop(int(complete))
            completed_tasks.append(complete_task)
            print(f"You Completed {complete_task[0]}!")
        
        except ValueError:
            print("please enter the index!")
    
    else:
        print("your task list is empty")
        


def view_completed_tasks():                                 #Shows The list of Tasks That Have Been Completed
    if completed_tasks:   
        for task in completed_tasks:
            print(f"Task: {task[0]} - Status: Complete")
    else:
        print("you have no completed tasks")


def delete_task():                                          #deletes a task from the task list
    if task_list:
        for index, (task, due_date, priority) in enumerate(task_list):
            print(f"{index}: {task}; {due_date}; {priority}")
        
        try:
            del_task = input("Enter the index of the task you would like to delete: ")
            task_list.pop(int(del_task))
        
        except Exception as e:
            print(f"Error Occured: {e}")
    
    else:
        print("Your Task List is empty!")
    


def main():                                                 #Driver function
    while True:
        
        print("""
    Welcome to the To-Do list!
    
    1. Add Task
    2. View Tasks
    3. Mark a task as complete
    4. View Completed Tasks
    5. Delete a task
    6. Quit
                        """)
        
        choice = input("Enter the Corresponding number of the action you would like to execute: ")
        # If Choice == 1,  runs the add task function
        
        if choice == "1":
            add_task()                              
        # choice 2: simply runs the view task function
        
        elif choice == '2':
            view_task()
            
        # choice 3: runs the complete task function 
        elif choice == '3':
            complete_task()
        # choice 4: runs view completed task function
        
        elif choice == '4':
            view_completed_tasks()
            
        # choice 5: runs the delete task func
        
        elif choice == '5':
            delete_task()
        # exits function
        
        elif choice == '6':
            print('Exiting...')
            break
        
        else:
            print('Please Enter a Valid Option.')
        
main()