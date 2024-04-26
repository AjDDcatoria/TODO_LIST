from tkinter import*
from tkinter import messagebox
from tkinter.ttk import Combobox
from datetime import datetime
from EntryCompo.EntryComponents import Entries, comboBoxes
from LabelCompo.LabelComponents import Labels
from FramesCompo.FramesComponents import*
from buttonCompo.buttonComponents import*

root = Tk()
Sortedschedule = []
Display_info = []
day_mapping = {
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2,
    "Thursday": 3,
    "Friday": 4,
    "Saturday": 5,
    "Sunday": 6
}
def displayAll():
    last_end_time = 0
    last_option = 0
    
    start = start_box.myEntry.get()
    end = end_box.myEntry.get()
    get_subject = str(subject_box.myEntry.get())
    option = str(days.myComboBox.get())
    start = start_box.myEntry.get()
    end = end_box.myEntry.get()
    index_Day = day_mapping[option]
    
    starting = datetime.strptime(start, "%I:%M %p")
    start_hour = starting.hour
    start_time = starting.strftime("%I:%M %p")
    start_am_pm = starting.strftime("%p")
    
    ending = datetime.strptime(end, "%I:%M %p")
    end_hour = ending.hour
    
    end_time = ending.strftime("%I:%M %p")
    end_am_pm = ending.strftime("%p")

    task = (start_time, end_time, index_Day)
    
    convertedHour = int(end_hour)
    if convertedHour in range(1, 12) and end_am_pm == "PM":
        newHour = int(end_hour)
        newHour +=12

        end_hour = str(newHour)
        end_hour
    else:
        end_hour
        
    for scheduled_task in Sortedschedule:
        location_index = scheduled_task[2]
        if starting < datetime.strptime(scheduled_task[1], "%I:%M %p") and \
           ending > datetime.strptime(scheduled_task[0], "%I:%M %p") and index_Day == location_index:
                messagebox.showerror("ERROR", "Can't Add Schedule")
                return Sortedschedule

    Sortedschedule.append(task)
    last_end_time = end_hour
    last_option = index_Day
    messagebox.showinfo("Successful", "Added Successfully!")
    info = get_subject, option, start_time, end
    Display_info.append(info)
    
    Display_info.sort(key=lambda x: datetime.strptime(x[2], "%I:%M %p"))
    
    sorted_days = sorted(Display_info, key=lambda x: day_mapping.get(x[1], 7))

    display_Info.mylist.delete(0, END)
    
    for entry in sorted_days:
        subject = entry[0]
        days_format = entry[1]
        start_format = entry[2]
        end_format = entry[3]
        
        display_Info.mylist.insert(END, f"{subject}, ({days_format}) {start_format}-{end_format}")

    Sortedschedule.sort(key=lambda x: datetime.strptime(x[0], "%I:%M %p"))
    
    
outerFrame = ExternalFrames(root, frameWidth=815, frameHeight=590, frameRow=0, frameColumn=0, frameBg="#C4D69C")

frame1 = LabelFrame(root, text="Add Schedule", width=350, height=500, bg="#C4D69C")
frame1.place(x=50, y=40)
frame2 = LabelFrame(root, text="List of Subjects", width=350, height=500, bg="#C4D69C")
frame2.place(x=420, y=40)
display_Info = frame2Components(frame2, listWidth=38, listHeight=20, listPadx=0, listPady=0)

subject_Label = Labels(frame1, textLabel="Enter Subject: ", Labelx=50, Labely=45, Labelbg="#C4D69C")
subject_box = Entries(frame1, entryWidth=16, entryx= 180, entryY= 47)

listofDays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

days = comboBoxes(frame1, comboValues=listofDays, comboWidth=14, combox = 176, comboy=151)

days_Label = Labels(frame1, textLabel="Choose Day: ", Labelx=60, Labely=150, Labelbg="#C4D69C")

start_Label = Labels(frame1, textLabel="Choose Start Time: ", Labelx=15, Labely=250, Labelbg="#C4D69C")
start_box = Entries(frame1, entryWidth=16, entryx= 176, entryY= 251)

end_Label = Labels(frame1, textLabel="Choose End Time: ", Labelx=15, Labely=350, Labelbg="#C4D69C")
end_box = Entries(frame1, entryWidth=16, entryx= 176, entryY= 351)

display_Button = Buttons(frame1, ButtonLabel="Add Subject", buttonCommand = displayAll, buttonx=235, buttony=427)


root.mainloop()