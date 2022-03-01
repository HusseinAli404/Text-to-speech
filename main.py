from tkinter import*
from gtts import gTTS
from playsound import playsound


root = Tk()
root.geometry('1024x768')
root.title('TEXT TO SPEECH')
root.configure(bg='gray')

play_image  = PhotoImage(file='images/play.png')
reset_image = PhotoImage(file='images/reset.png')
exit_image  = PhotoImage(file='images/exit.png')

label1=Label(root, text = 'TEXT_TO_SPEECH', font = ('arial',20), bg ='white smoke')
label2=Label(root, text = 'www.github.com/HusseinAli404/text-to-speech', font = ('arial',20), bg ='white smoke')

text = StringVar()
text_box = Entry(root,textvariable=text,font=('arial',20))

def text_to_speech():
	message = text_box.get()
	speech  = gTTS(text=message)
	speech.save('file.mp3')
	playsound('file.mp3')

def reset():
	text.set('')
def exit():
	root.destroy()


button_1 = Button(root,image=reset_image ,command=reset)
button_2 = Button(root,image=play_image  ,command=text_to_speech)
button_3 = Button(root,image=exit_image  ,command=exit)


button_1.grid(row=5,column=1,sticky='nsew')
button_2.grid(row=5,column=2,sticky='nsew')
button_3.grid(row=5,column=3,sticky='nsew')

text_box.grid(row=3,column=2,sticky='nsew')
label1.grid(row=1,  column=2,sticky='nsew')
label2.grid(row=8, column=2,sticky='nsew')

List1 = [1,2,3,4,5,6,7,8,9,10]
List2 = [1,2,3,4,5]

row_number    = 0
column_number = 0

for i in List1:
	Grid.rowconfigure(root,row_number,weight=1)
	row_number+=1

for i in List2:	
	Grid.columnconfigure(root,column_number,weight=1)
	column_number+=1




root.mainloop()