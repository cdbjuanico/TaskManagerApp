from tkinter import *
import mysql.connector as mariadb
import config

mariadb_connection = mariadb.connect(user = "root", password = config.password, host = "localhost", port = "3306", database = "taskmanager")
cursor = mariadb_connection.cursor()
desc = ["ID", "To do Date", "Task Name", "Due Date", "Status"]
descViewAll = ["ID", "Task Name", "To do Date", "Due Date", "Status","Category"]
categoryDesc = ["ID", "Category Name"]

class functions():
        
    def update_tasks(tasksList):
        functions.clearText(tasksList)
        cursor.execute('SELECT * FROM task;')
        tasksList.insert(INSERT, "======Available Tasks======" + '\n')
        i = 1
        for task in cursor:
            taskDetails = '['+ str(i) +'] ' + task[2]
            tasksList.insert(INSERT, taskDetails + '\n')
            i += 1
        tasksList.insert(INSERT, "===========================" + '\n')

    def update_categs(tasksList):
        functions.clearText(tasksList)
        tasksList.configure(state = "normal")
        tasksList.delete(1.0, "end")
        i = 1
        tasksList.insert(INSERT, "======Available Categories======" + '\n')
        cursor.execute('SELECT * FROM category;')
        for categs in cursor:
            categDetails = '['+ str(i) +'] ' + categs[1]
            tasksList.insert(INSERT, categDetails + '\n')
            i += 1
        tasksList.insert(INSERT, "================================" + '\n')

    def clearText(tasksList):
        tasksList.delete(1.0, "end")

    def addTask(titleEntry,todo,due):
        taskname = titleEntry.get()
        tasktodo = todo.get_date()
        taskdue = due.get_date()
        
        if taskname != "":
            statement = 'INSERT INTO task (tododate, taskname, duedate) VALUES (%s, %s, %s);'
            values = (tasktodo,taskname,taskdue)
            cursor.execute(statement, values)
            mariadb_connection.commit();
            print("\nNew Task has been created")
        else:
            print("Please input Task Title")
        titleEntry.delete(0, 'end')
        todo.delete(0, 'end')
        due.delete(0, 'end')

    def editTask(taskIndex, newtaskname, newtododate, newduedate):
        index = taskIndex.get()
        newname = newtaskname.get()
        todo = newtododate.get_date()
        due = newduedate.get_date()
        try:
            #functions.viewTaskNames()
            taskname = functions.getTaskNames(int(index))

            if(newtododate != ''):
                statement = 'UPDATE task SET tododate = %s WHERE taskname = %s;'
                values = (todo, taskname)
                cursor.execute(statement, values)
                mariadb_connection.commit();
                print("To do changed")

            if(newduedate != ''):
                statement = 'UPDATE task SET duedate = %s WHERE taskname = %s;'
                values = (due, taskname)
                cursor.execute(statement, values)
                mariadb_connection.commit();
                print("Due changed")

            if(newtaskname != ''):
                statement = 'UPDATE task SET taskname = %s WHERE taskname = %s;'
                values = (newname, taskname)
                cursor.execute(statement, values)
                mariadb_connection.commit();
                print("Task name changed")
                
            
        except:
            print("Invalid input.")

    def deleteTask(choice,index):
        taskIndex = index.get()
        deleteChoice = choice
        if deleteChoice == 1:
            taskname = functions.getTaskNames(int(taskIndex))
            statement = 'DELETE FROM task WHERE taskname = %s;'
            values = [taskname]
            cursor.execute(statement, values)
            mariadb_connection.commit();
            print('\nSuccessfully deleted a task')

        elif deleteChoice == 2:
            statement = 'DELETE FROM task WHERE status = %s;'
            values = ['FINISHED']
            cursor.execute(statement, values)
            mariadb_connection.commit();
            print('\nSuccessfully deleted all finished task/s')     
            
        else:
            print("Invalid input..")


    def viewAllTask(taskList):

        tasks_dict = {}
        
        cursor.execute('SELECT * FROM task;') 
        no_categ = cursor.fetchall()

        view ='SELECT taskid, tododate,taskname,duedate,status,categoryname FROM task NATURAL JOIN belongs_to NATURAL JOIN category;'
        cursor.execute(view)
        tasks = cursor.fetchall()
        for category in tasks:
            if category[0] in tasks_dict:
                tasks_dict[category[0]].append(category[5])
            else:
                tasks_dict[category[0]] = [category[5]]

        for tasks in no_categ:
            i = 0
            taskList.insert(INSERT, "===================TASK==================" + '\n')
            for columns in tasks: 
                taskList.insert(INSERT, desc[i] + ": " + str(columns) + '\n')
                i += 1
            if tasks[0] in tasks_dict:
                    categ_list = tasks_dict[tasks[0]]
                    categ_list_join = ', '.join(categ_list)
                    taskList.insert(INSERT, f'Category : {categ_list_join}' + '\n')
            else:
                taskList.insert(INSERT, f'Category : Null' + '\n')
            taskList.insert(INSERT, "=========================================" + '\n')

    def viewTaskNames(List):
        List.insert(INSERT, "=========Available Tasks=========" + '\n')
        i = 1
        cursor.execute('SELECT * FROM task;') 
        for task in cursor:
            List.insert(INSERT, '['+ str(i) +'] ' + task[2] + '\n')
            i += 1
        List.insert(INSERT, "=================================" + '\n')
    
    def viewTaskStatus(List):
        List.insert(INSERT, "==============Available Tasks==============" + '\n')
        i = 1
        cursor.execute('SELECT * FROM task;') 
        for task in cursor:
            List.insert(INSERT, '['+ str(i) +'] ' + task[2] + ' - ' + task[4] + '\n')
            i += 1
        List.insert(INSERT, "===========================================" + '\n')

    def viewCategoryNames(categoryList):
        cursor.execute('SELECT * FROM category;')
        i = 1
        categoryList.insert(INSERT, "======AvailableCategories======" + '\n')
        for categs in cursor:
                categDetails = '['+ str(i) +'] ' + categs[1]
                categoryList.insert(INSERT, categDetails + '\n')
                i += 1
        categoryList.insert(INSERT, "==============END==============" + '\n')


    def updateTaskList(tasksList):
        cursor.execute('SELECT * FROM task;')
        tasksList.insert(INSERT, "=============Available Tasks=============" + '\n')
        i = 1
        for task in cursor:
                taskDetails = '['+ str(i) +'] ' + task[2]
                tasksList.insert(INSERT, taskDetails + '\n')
                i += 1
        tasksList.insert(INSERT, "=========================================" + '\n')
    def getTaskNames(index): 
        cursor.execute('SELECT * FROM task;')
        tasks = cursor.fetchall()
        return tasks[int(index)-1][2]

    def getCategoryNames(categindex,taskIndex):
        tasks_dict = {}
        cursor.execute('SELECT * FROM category;')
        categs = cursor.fetchall()

        view ='SELECT taskid, tododate,taskname,duedate,status,categoryname FROM task NATURAL JOIN belongs_to NATURAL JOIN category;'
        cursor.execute(view)
        tasks = cursor.fetchall()
        for category in tasks:
            if category[0] in tasks_dict:
                tasks_dict[category[0]].append(category[5])
            else:
                tasks_dict[category[0]] = [category[5]]
        
        categ_sel = categs[categindex-1][1]

        if taskIndex in tasks_dict:
            if categ_sel in tasks_dict[taskIndex]:
                return False

        return categ_sel

    def getCategoryNames2(index): 
        try:
            i = 1
            cursor.execute('SELECT * FROM category;')
            for var in cursor:
                if i == int(index):
                    name = var[1]
                i += 1
            return(name)  
        except:
            status = 404
            return(status)
        
    def markTaskDone(index):
        try:
            taskIndex = index
            taskname = functions.getTaskNames(taskIndex)
            statement = 'SELECT status FROM task WHERE taskname = %s;'
            values = [taskname]
            cursor.execute(statement, values)
            for i in cursor:
                if(str(i[0]) == 'FINISHED'):
                    statement = 'UPDATE task SET status = "UNFINISHED" WHERE taskname = %s;'
                else:
                    statement = 'UPDATE task SET status = "FINISHED" WHERE taskname = %s;'
           
            cursor.execute(statement, values)
            mariadb_connection.commit();
            print('\n' + taskname + " marked as done!")
        except:
            print("Invalid input?.")

    def addCategory(name):
        category = name
        statement = 'INSERT INTO category (categoryname) VALUES (%s);'
        values = [category]
        cursor.execute(statement, values)
        mariadb_connection.commit();

    def editCategory(index, name):
        try:
            categoryName = functions.getCategoryNames2(index)
            newCategory = name
            statement = 'UPDATE category SET categoryname = %s WHERE categoryname = %s;'
            values = (newCategory, categoryName)
            cursor.execute(statement, values)
            mariadb_connection.commit();
            print("\nSuccessfully renamed category")
        except:
            print("Unable to Edit Category Name, please try again")

    def deleteCategory(index):
        categoryIndex = index.get()
        categoryname = functions.getCategoryNames2(categoryIndex)
        statement = 'DELETE FROM category WHERE categoryname = %s;'
        values = [categoryname]
        cursor.execute(statement, values)
        mariadb_connection.commit();


    def viewCategoryTasks(index, list,label):
        functions.clearText(list)
        newview = 'SELECT taskid, taskname, tododate, duedate, status, categoryname FROM category NATURAL JOIN belongs_to NATURAL JOIN task WHERE categoryname = %s;'
        categoryIndex = int(index)
        cursor.execute('SELECT * FROM category;')
        i = 1
        for var in cursor:
            if(i == categoryIndex):
                name = var[1]
            i += 1
        value = [name]
        label['text'] = name
        cursor.execute(newview,value)
        for tasks in cursor:
            i = 0
            list.insert(INSERT, "===================TASK==================" + '\n')
            for columns in tasks:
                list.insert(INSERT, descViewAll[i] + ": " + str(columns) + '\n')
                i += 1
            list.insert(INSERT, "=========================================" + '\n')


    def addTasktoCategory(taskIndex, categoryIndex):
        taskname = functions.getTaskNames(taskIndex)
        categoryname = functions.getCategoryNames2(categoryIndex)
        if(categoryname == 404):
            return(404)
        try:
            statement = 'INSERT INTO belongs_to VALUES ((SELECT categoryid FROM category WHERE categoryname = %s),(SELECT taskid FROM task WHERE taskname = %s));'
            values = (categoryname,taskname)
            cursor.execute(statement, values)
            mariadb_connection.commit();
            print(taskname + '  added to ' + categoryname + ' category')
            return(0)
        except: 
            return(1)

    def viewTask(choice, day, month, year, list):
        list.delete(1.0, 'end')
        if choice == 1:
            if (len(day) == 1):
                day = str('0' + day)
            if (len(month) == 1):
                month = str('0' + month)
            date = year + '-' + month + '-' + day
            
        if choice == 2:
            if (len(month) == 1):
                month = str('0' + month)
            date = year + '-' + month + '-__'

        if choice == 3:
            date = year + '-__' + '-__'

        query = ('SELECT taskid, tododate, taskname, duedate, status FROM task WHERE tododate LIKE %s;')
        var = [date]
        cursor.execute(query,var)

        for tasks in cursor:
            i = 0
            list.insert(INSERT, "===================TASK==================\n")
            for columns in tasks:
                list.insert(INSERT, desc[i] + ": " + str(columns) + '\n')
                i += 1
            list.insert(INSERT, "=========================================\n")
