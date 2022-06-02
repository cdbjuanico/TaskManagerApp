import tkinter as tk
from tkinter import ttk
import tkinter
from tkinter import *
from tkinter import font
from turtle import color
from tkcalendar import DateEntry
import mysql.connector as mariadb
import helper
import config

mariadb_connection = mariadb.connect(user = "root", password = config.password, host = "localhost", port = "3306", database = "taskmanager")
cursor = mariadb_connection.cursor(buffered = True)
cursor2 = mariadb_connection.cursor

 
LARGEFONT =("Verdana", 20)

class tkinterApp(tk.Tk):
     
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
         
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
         
        # creating a container
        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        # initializing frames to an empty array
        self.frames = {} 
  
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, Page1, Page2, Page3, Page4, Page5, Page6, Page7, Page8, Page9, Page10, Page11, viewDay, viewMonth, viewYear):
  
            frame = F(container, self)
  
            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(StartPage)
  
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

# first window frame startpage
  
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # label of frame Layout 2
        label = ttk.Label(self, text ="Task Manager", font = LARGEFONT, padding= 10)
         
        # putting the grid in its place by using
        # grid
        label.pack()
  
        addTask = ttk.Button(self, text ="Add a Task",
        command = lambda : [controller.show_frame(Page1)])
     
        # putting the button in its place by
        # using grid
        addTask.pack()
  
        ## button to show frame 2 with text layout2
        editTask = ttk.Button(self, text ="Edit a Task",
        command = lambda : controller.show_frame(Page2))
     
        # putting the button in its place by
        # using grid
        editTask.pack()

                ## button to show frame 2 with text layout2
        deleteTask = ttk.Button(self, text ="Delete a Task",
        command = lambda : controller.show_frame(Page3))
     
        # putting the button in its place by
        # using grid
        deleteTask.pack()

                ## button to show frame 2 with text layout2
        viewAllTask = ttk.Button(self, text ="View all Task",
        command = lambda : controller.show_frame(Page4))
     
        # putting the button in its place by
        # using grid
        viewAllTask.pack()

                ## button to show frame 2 with text layout2
        markTask = ttk.Button(self, text ="Mark Task as Done",
        command = lambda : controller.show_frame(Page5))
     
        # putting the button in its place by
        # using grid
        markTask.pack()

                ## button to show frame 2 with text layout2
        addCategory = ttk.Button(self, text ="Add Category",
        command = lambda : controller.show_frame(Page6))
     
        # putting the button in its place by
        # using grid
        addCategory.pack()

                ## button to show frame 2 with text layout2
        editCategory = ttk.Button(self, text ="Edit Category",
        command = lambda : controller.show_frame(Page7))
     
        # putting the button in its place by
        # using grid
        editCategory.pack()

                ## button to show frame 2 with text layout2
        deleteCategory = ttk.Button(self, text ="Delete Category",
        command = lambda : controller.show_frame(Page8))
     
        # putting the button in its place by
        # using grid
        deleteCategory.pack()

                ## button to show frame 2 with text layout2
        viewCategory = ttk.Button(self, text ="View Category",
        command = lambda : controller.show_frame(Page9))
     
        # putting the button in its place by
        # using grid
        viewCategory.pack()

                ## button to show frame 2 with text layout2
        addTasktoCategory = ttk.Button(self, text ="Add Task to a Category",
        command = lambda : controller.show_frame(Page10))
     
        # putting the button in its place by
        # using grid
        addTasktoCategory.pack()

                ## button to show frame 2 with text layout2
        viewTask = ttk.Button(self, text ="View Task",
        command = lambda : controller.show_frame(Page11))
     
        # putting the button in its place by
        # using grid
        viewTask.pack()
# second window frame ADD TASK PAGE
class Page1(tk.Frame):
        def __init__(self, parent, controller):
                tk.Frame.__init__(self, parent)
                label = ttk.Label(self, text ="ADD A TASK", font= 10)
                title = tkinter.Label(self,text = "Task Name")
                titleEntry = tkinter.Entry(self)
                tododate = tkinter.Label(self,text = "To Do Date")
                tododateEntry = DateEntry(self, selectmode = 'day')
                duedate = tkinter.Label(self,text = "Due Date")
                duedateEntry = DateEntry(self, selectmode = 'day')
                addTaskButton = tkinter.Button(self, text = "Add",width= 10, command = lambda : [helper.functions.addTask(titleEntry,tododateEntry,duedateEntry), controller.show_frame(StartPage)])
                BackButton = tkinter.Button(self, text = "Back",width= 10, command = lambda : [controller.show_frame(StartPage)])
                #LAYOT
                label.pack()
                title.pack()
                titleEntry.pack()
                tododate.pack()
                tododateEntry.pack()
                duedate.pack()
                duedateEntry.pack()
                addTaskButton.pack()
                BackButton.pack()

# third window frame page2
class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        length = 1
        cursor.execute('SELECT * FROM task;')
        label = ttk.Label(self, text ="EDIT A TASK", font = LARGEFONT)
        for a in cursor:
            length += 1
        tasksList = tkinter.Text(self, height=length+1, width=28)
        cursor.execute('SELECT * FROM task;')
        tasksList.insert(INSERT, "======Available Tasks======" + '\n')
        i = 1
        for task in cursor:
            taskDetails = '['+ str(i) +'] ' + task[2]
            tasksList.insert(INSERT, taskDetails + '\n')
            i += 1
        tasksList.insert(INSERT, "===========================" + '\n')
        indexlabel = Label(self, text = "Input Task Index")
        taskIndex = Entry(self)
        newtitle = tkinter.Label(self,text = "New Task Name")
        titleEntry = tkinter.Entry(self)
        tododate = tkinter.Label(self,text = "To Do Date")
        tododateEntry = DateEntry(self, selectmode = 'day')
        duedate = tkinter.Label(self,text = "Due Date")
        duedateEntry = DateEntry(self, selectmode = 'day')
        editTaskButton = tkinter.Button(self, text = "Edit",width= 10, command = lambda : [tasksList.configure(state = 'normal'),helper.functions.editTask(taskIndex, titleEntry, tododateEntry, duedateEntry), helper.functions.update_tasks(tasksList), tasksList.configure(state = 'disabled'), controller.show_frame(StartPage)])
        refreshButton = tkinter.Button(self, text = "Refresh",width= 10, command = lambda : [tasksList.configure(state = 'normal'), helper.functions.update_tasks(tasksList), tasksList.configure(state = 'disabled')])
        BackButton = tkinter.Button(self, text = "Back",width= 10, command = lambda : [controller.show_frame(StartPage)])
        #LAYOUT
        label.pack()
        tasksList.pack()
        indexlabel.pack()
        taskIndex.pack()
        newtitle.pack()
        titleEntry.pack()
        tododate.pack()
        tododateEntry.pack()
        duedate.pack()
        duedateEntry.pack()
        editTaskButton.pack()
        refreshButton.pack()
        BackButton.pack()

class Page3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        length = 1
        cursor.execute('SELECT * FROM task;')
        label = ttk.Label(self, text ="DELETE A TASK", font = LARGEFONT)
        for a in cursor:
            length += 1
        tasksList = tkinter.Text(self, height=length+1, width=28)
        cursor.execute('SELECT * FROM task;')
        tasksList.insert(INSERT, "======Available Tasks======" + '\n')
        i = 1
        for task in cursor:
            taskDetails = '['+ str(i) +'] ' + task[2]
            tasksList.insert(INSERT, taskDetails + '\n')
            i += 1
        tasksList.insert(INSERT, "===========================" + '\n')
        indexlabel = Label(self, text = "Input Task Index")
        taskIndex = Entry(self)
        deleteTaskButton = tkinter.Button(self, text = "Delete", command = lambda : [helper.functions.deleteTask(1,taskIndex), helper.functions.update_tasks(tasksList), controller.show_frame(StartPage)])
        deleteTaskButton2 = tkinter.Button(self, text = "Delete All Finished", command = lambda : [tasksList.configure(state = 'normal'), helper.functions.deleteTask(2,taskIndex), helper.functions.update_tasks(tasksList), tasksList.configure(state = 'disabled'), controller.show_frame(StartPage)])
        refreshButton = tkinter.Button(self, text = "Refresh", command = lambda : [tasksList.configure(state = 'normal'), helper.functions.update_tasks(tasksList), tasksList.configure(state = 'disabled')])
        BackButton = tkinter.Button(self, text = "Back", command = lambda : [controller.show_frame(StartPage)])
        #LAYOUT
        label.pack()
        tasksList.pack()
        indexlabel.pack()
        taskIndex.pack()
        deleteTaskButton.pack()
        deleteTaskButton2.pack()
        refreshButton.pack()
        BackButton.pack()

class Page4(tk.Frame):
        def clearText(tasksList):
                tasksList.delete(1.0, "end")
        def updateList(taskList):
                Page4.clearText(taskList)
                helper.functions.viewAllTask(taskList)
        def __init__(self, parent, controller):
                tk.Frame.__init__(self, parent)
                tasksList = tkinter.Text(self, pady = 10, width = 41)
                cursor.execute('SELECT * FROM task;')
                label = ttk.Label(self, text ="Task List", font = LARGEFONT)
                Page4.updateList(tasksList)
                refreshButton = tkinter.Button(self, text = "Refresh", command = lambda : [tasksList.delete(1.0, "end"),Page4.updateList(tasksList)])
                BackButton = tkinter.Button(self, text = "Back", command = lambda : [Page4.updateList(tasksList), controller.show_frame(StartPage)])
                #LAYOUT
                label.pack()
                tasksList.pack()
                refreshButton.pack()
                BackButton.pack()
class Page5(tk.Frame):
        def clearText(tasksList, taskIndex):
                tasksList.delete(1.0, "end")
                taskIndex.delete(0, "end")
        def updateList(taskList, taskIndex):
                Page5.clearText(taskList, taskIndex)
                helper.functions.viewTaskStatus(taskList)
        def __init__(self, parent, controller):
                tk.Frame.__init__(self, parent)
                label = ttk.Label(self, text ="Task List", font = LARGEFONT)
                tasksList = tkinter.Text(self, width=43)
                indexlabel = tkinter.Label(self, text = "Input Index of Task to changes Status")
                taskIndex = Entry(self)
                BackButton = tkinter.Button(self, text = "Back", command = lambda : [controller.show_frame(StartPage)])
                RefreshButton = tkinter.Button(self, text = "Refresh", command = lambda : [Page5.updateList(tasksList,taskIndex)])
                MarkButton = tkinter.Button(self, text = "Change Status", command = lambda : [helper.functions.markTaskDone(taskIndex.get()), Page5.updateList(tasksList,taskIndex)])
                #LAYOUT
                label.pack()
                tasksList.pack()
                indexlabel.pack()
                taskIndex.pack()
                MarkButton.pack()
                RefreshButton.pack()
                BackButton.pack()
                
                Page5.updateList(tasksList,taskIndex)
#ADD CATEGORY               
class Page6(tk.Frame):
        def __init__(self, parent, controller):
                tk.Frame.__init__(self, parent)
                label = ttk.Label(self, text ="ADD A CATEGORY", font= 10)
                title = tkinter.Label(self,text = "Category Name")
                titleEntry = tkinter.Entry(self)
                addTaskButton = tkinter.Button(self, text = "Add",width= 10, command = lambda : [helper.functions.addCategory(titleEntry.get()), controller.show_frame(StartPage)])
                BackButton = tkinter.Button(self, text = "Back",width= 10, command = lambda : [controller.show_frame(StartPage)])
                #LAYOUT
                label.pack()
                title.pack()
                titleEntry.pack()
                addTaskButton.pack()
                BackButton.pack() 
#EDIT CATEGORY
class Page7(tk.Frame):
        def __init__(self, parent, controller):
                tk.Frame.__init__(self, parent)
                label = ttk.Label(self, text ="EDIT A CATEGORY", font = LARGEFONT)
                tasksList = tkinter.Text(self, width=32)
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
                indexlabel = Label(self, text = "Input Category Index")
                taskIndex = Entry(self)
                newtitle = tkinter.Label(self,text = "New Category Name")
                titleEntry = tkinter.Entry(self)
                editTaskButton = tkinter.Button(self, text = "Edit",width= 10, command = lambda : [tasksList.configure(state = 'normal'),helper.functions.editCategory(taskIndex.get(), titleEntry.get()), helper.functions.update_categs(tasksList), tasksList.configure(state = 'disabled')])
                refreshButton = tkinter.Button(self, text = "Refresh",width= 10, command = lambda : [tasksList.configure(state = 'normal'), helper.functions.update_categs(tasksList), tasksList.configure(state = 'disabled')])
                BackButton = tkinter.Button(self, text = "Back",width= 10, command = lambda : [controller.show_frame(StartPage)])
                #LAYOUT
                label.pack()
                tasksList.pack()
                indexlabel.pack()
                taskIndex.pack()
                newtitle.pack()
                titleEntry.pack()
                editTaskButton.pack()
                refreshButton.pack()
                BackButton.pack()  
#DELETE CATEGORY
class Page8(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        cursor.execute('SELECT * FROM category;')
        label = ttk.Label(self, text ="DELETE A CATEGORY", font = LARGEFONT)
        tasksList = tkinter.Text(self, width=32)
        cursor.execute('SELECT * FROM category;')
        tasksList.insert(INSERT, "======Available Categories======" + '\n')
        i = 1
        for task in cursor:
            taskDetails = '['+ str(i) +'] ' + task[1]
            tasksList.insert(INSERT, taskDetails + '\n')
            i += 1
        tasksList.insert(INSERT, "================================" + '\n')
        indexlabel = Label(self, text = "Input Category Index")
        taskIndex = Entry(self)
        deleteTaskButton = tkinter.Button(self, text = "Delete", command = lambda : [helper.functions.deleteCategory(taskIndex), helper.functions.update_categs(tasksList)])
        refreshButton = tkinter.Button(self, text = "Refresh", command = lambda : [tasksList.configure(state = 'normal'), helper.functions.update_categs(tasksList), tasksList.configure(state = 'disabled')])
        BackButton = tkinter.Button(self, text = "Back", command = lambda : [controller.show_frame(StartPage)])
        #LAYOUT
        label.pack()
        tasksList.pack()
        indexlabel.pack()
        taskIndex.pack()
        deleteTaskButton.pack()
        refreshButton.pack()
        BackButton.pack()  
#VIEW CATEGORY
class Page9(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="LIST OF CATEGORIES", font = LARGEFONT)
        categoryList = tkinter.Text(self, height = 10, width = 31)
        helper.functions.viewCategoryNames(categoryList)
        categoryList.configure(state = 'disabled')
        indexLabel = Label(self, text = "Input Category Index to view Tasks")
        taskIndex = Entry(self)
        taskList = tkinter.Text(self, height = 10, width = 41)
        categoryLabel = Label(self, text = '', font = 20)
        ViewButton = tkinter.Button(self, text = "View", command = lambda : [helper.functions.viewCategoryTasks(taskIndex.get(),taskList,categoryLabel)])
        RefreshButton = tkinter.Button(self, text = "Refresh", command = lambda : [categoryList.configure(state = 'normal'), categoryList.delete(1.0, "end"), helper.functions.viewCategoryNames(categoryList),categoryList.configure(state = 'disabled')])
        BackButton = tkinter.Button(self, text = "Back", command = lambda : [controller.show_frame(StartPage)])
        #LAYOUT
        label.pack()
        categoryList.pack()
        indexLabel.pack()
        taskIndex.pack()  
        categoryLabel.pack()      
        taskList.pack()
        ViewButton.pack()
        RefreshButton.pack()
        BackButton.pack()

#ADD TASK TO CATEGORY
class Page10(tk.Frame):
        def __init__(self, parent, controller):
                tk.Frame.__init__(self, parent)
                cursor.execute('SELECT * FROM task;')
                label = ttk.Label(self, text ="INSERT TASK INTO A CATEGORY", font = LARGEFONT)
                taskListLabel = Label(self, text = "List of Tasks", font = 15)
                tasksList = tkinter.Text(self, height=10, width=41)
                helper.functions.updateTaskList(tasksList)
                categoryListLabel = Label(self, text = "List of Categories", font = 15)
                categoryList = tkinter.Text(self, height=10, width=31)
                helper.functions.viewCategoryNames(categoryList)
                indexlabel = Label(self, text = "Input Task Index")
                taskIndex = Entry(self)
                categorylabel = Label(self, text = "Input Category Index")
                categoryIndex = Entry(self)
                checker = Label(self, text = '', font = 20, fg='red')
                addTaskButton = tkinter.Button(self, text = "Add",width= 10, command = lambda : [Page10.check(taskIndex, categoryIndex, checker)])
                refreshButton = tkinter.Button(self, text = "Refresh",width= 10, command = lambda : [Page10.updatePage(tasksList, categoryList, taskIndex, categoryIndex, checker)])
                BackButton = tkinter.Button(self, text = "Back",width= 10, command = lambda : [controller.show_frame(StartPage)])
                #LAYOUT
                label.pack()
                taskListLabel.pack()
                tasksList.pack()
                categoryListLabel.pack()
                categoryList.pack()
                indexlabel.pack()
                taskIndex.pack()
                categorylabel.pack()
                categoryIndex.pack()
                checker.pack()
                addTaskButton.pack()
                refreshButton.pack()
                BackButton.pack()
                
        def check(taskIndex, categoryIndex, checker):
                tName = helper.functions.getTaskNames(taskIndex.get())
                cName = helper.functions.getCategoryNames2(categoryIndex.get())
                result = helper.functions.addTasktoCategory(taskIndex.get(),categoryIndex.get())
                if(result == 0):
                        string = tName+' has been added to the ' + cName + ' category'
                elif(result == 1):
                        string = tName+' is already in the ' + cName + ' category'
                else:
                        string = 'Invalid Input'
                checker['text'] = string
        
        def updatePage(taskList, categoryList, taskInput, categoryInput, redLabel):
                taskList.delete(1.0, 'end')
                helper.functions.updateTaskList(taskList)
                categoryList.delete(1.0, 'end')
                helper.functions.viewCategoryNames(categoryList)
                taskInput.delete(0, 'end')
                categoryInput.delete(0, 'end')
                redLabel['text'] = ''

class Page11(tk.Frame):
        def __init__(self, parent, controller):
                tk.Frame.__init__(self, parent)
                label = ttk.Label(self, text ="View Task/s", font = LARGEFONT)
                day = tkinter.Button(self, text= "View by Day", width= 15, command = lambda : [controller.show_frame(viewDay)])
                month = tkinter.Button(self, text= "View by Month", width= 15, command = lambda : [controller.show_frame(viewMonth)])
                year = tkinter.Button(self, text= "View by Year", width= 15, command = lambda : [controller.show_frame(viewYear)])
                BackButton = tkinter.Button(self, text = "Back",width= 10, command = lambda : [controller.show_frame(StartPage)])
                #LAYOUT
                label.pack()
                day.pack()
                month.pack()
                year.pack()
                BackButton.pack()
class viewDay(tk.Frame):
        def __init__(self, parent, controller):
                tk.Frame.__init__(self, parent)
                label = ttk.Label(self, text ="View by Day", font = LARGEFONT)
                year = Entry(self)
                month = Entry(self)
                day = Entry(self)
                ylabel = ttk.Label(self, text ="Input Year")
                mlabel = ttk.Label(self, text ="Input Month")
                dlabel = ttk.Label(self, text ="Input Day")
                tasksList = tkinter.Text(self, height=10, width=41)
                ViewButton = tkinter.Button(self, text = "View",width= 10, command = lambda : [helper.functions.viewTask(1, day.get(), month.get(), year.get(), tasksList)])
                BackButton = tkinter.Button(self, text = "Back",width= 10, command = lambda : [tasksList.delete(1.0, 'end'), controller.show_frame(Page11)])
                

                #BUILD LAYOUT
                label.pack()
                ylabel.pack()
                year.pack()
                mlabel.pack()
                month.pack()
                dlabel.pack()
                day.pack()
                ViewButton.pack()
                BackButton.pack()
                tasksList.pack()

class viewMonth(tk.Frame):
        def __init__(self, parent, controller):
                tk.Frame.__init__(self, parent)
                label = ttk.Label(self, text ="View by Month", font = LARGEFONT)
                year = Entry(self)
                month = Entry(self)
                ylabel = ttk.Label(self, text ="Input Year")
                mlabel = ttk.Label(self, text ="Input Month")
                ViewButton = tkinter.Button(self, text = "View",width= 10, command = lambda : [helper.functions.viewTask(2, '', month.get(), year.get(), tasksList)])
                BackButton = tkinter.Button(self, text = "Back",width= 10, command = lambda : [tasksList.delete(1.0, 'end'), controller.show_frame(Page11)])
                tasksList = tkinter.Text(self, height=10, width=41)
                #BUILD LAYOUT
                label.pack()
                ylabel.pack()
                year.pack()
                mlabel.pack()
                month.pack()
                ViewButton.pack()
                BackButton.pack()
                tasksList.pack()

class viewYear(tk.Frame):
        def __init__(self, parent, controller):
                tk.Frame.__init__(self, parent)
                label = ttk.Label(self, text ="View by Year", font = LARGEFONT)
                year = Entry(self)
                ylabel = ttk.Label(self, text ="Input Year")
                ViewButton = tkinter.Button(self, text = "View",width= 10, command = lambda : [helper.functions.viewTask(3, '', '', year.get(), tasksList)])
                BackButton = tkinter.Button(self, text = "Back",width= 10, command = lambda : [tasksList.delete(1.0, 'end'), controller.show_frame(Page11)])
                tasksList = tkinter.Text(self, height=10, width=41)
                #BUILD LAYOUT
                label.pack()
                ylabel.pack()
                year.pack()
                ViewButton.pack()
                BackButton.pack()
                tasksList.pack()
        

# Driver Code
app = tkinterApp()
app.title("TASK MANAGER")
app.geometry("400x800")
app.mainloop()