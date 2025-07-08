import tkinter as tk
#tkinter library to create window and write on the window

from tkinter.filedialog import askopenfilename , asksaveasfilename
#to open and save the file

def saving_file():
    file_location = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text files","*.txt"),["All files","*.*"]])
    if not file_location:
        return#if no file then return
    with open(file_location,"w") as file_output:#this is called with block this concept comes in file handling in python
        #open means open if location find in written format as o/p
        text = text_edit.get(1.0,tk.END)#here we are editing
        file_output.write(text)#then the o/p
    root.title(f"notepad_clone -{file_location}")#with the help of f the location can be displayed if not that then the file location

#this is the function for saving the file with the function asksaveasfilename () now defaultextention is the parameter
#which will have deafault extension as .txt like notepad saves default way
#filetypes will show the files in the written manner here basically saving wala work is done
#*.* means any type of file rather than txt

def opening_file():
    file_location = askopenfilename(
        filetypes=[("text files","*.txt"),(" All files","*.*")] )
    if not file_location:
        return
    text_edit.delete(1.0,tk.END)#for deleting also
    with open(file_location,"r") as file_input:
        text = file_input.read()#here just reading the file
        text_edit.insert(tk.END,text)#here of editing and ending
    root.title(f"note_clone-{file_location}")

#this function is for opening and displaying the file with the function askopenfile name()


root=tk.Tk()
#create Tkinter window with Tk()
root.title("MY OWN NOTEPAD")
#title for the notepad
root.rowconfigure(0,minsize=1500)
#row for the notepad
root.columnconfigure(1,minsize=1500)
#column for the notepad

text_edit = tk.Text(root)
text_edit.grid(row=0,column=1,sticky="nsew")
#Text is the function of tkinter text will be edited or written all that will be written on tkinter window
#sticky="nsew" making long or proper  window

frame_button = tk.Frame(root, relief=tk.RAISED,bd=3)
#here Frame is a function in my root or window well Frame() will help in desinging the button of open & save
#now relief=RAISED here means the buttons will be little popped i.e relief helps in giving effects to the button bd is border
frame_button.grid(row=0,column=0,sticky="ns")
#sticky="ns" is a parameter for aligning thing together

button_open=tk.Button(frame_button,text="OPEN",command=opening_file)#open button
button_open.grid(row=0,column=0,padx=5, pady=5)
#grid is a function helps as for giving dimension like place where the button will be in trems of row & column
#command is for giving command which is in the opening_file () have

button_save=tk.Button(frame_button,text="SAVE AS",command=saving_file)#save as button
button_save.grid(row=1,column=0,padx=5)



root.mainloop()
#compulsory end line if tkinter library is used


