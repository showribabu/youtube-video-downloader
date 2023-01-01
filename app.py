# tkinter no need to install separately....
# here we are using 'tkinter and pytube'
from tkinter import *
from pytube import YouTube

# initialixation of tkinter...

app=Tk()
# gui requirements..
app.geometry('500x500')
app.resizable(0,0)
app.title('Youtube Down loader')
Label(app,text='Youtube video downloader',font='arial 15 bold')

# for field for enter link..
link=StringVar()
Label(app,text='enter link',font='arial 10 bold',background='red').place(x=180,y=60)
#..field for entry the link..
link_e=Entry(app,width=70,textvariable=link).place(x=35,y=90)

# function for handiliing..download button...

def Download():
    url=YouTube(str(link.get()))
    video=url.streams.first()
    video.download()
    #the video..download..
    #After download it show downloaded..
    Label(app,text='Downloaded',font='arial 20 bold',bg='pink').place(x=180,y=210)

# Button for download ..click...
Button(app,text='click',font='arial 20 ',bg='violet red',command=Download).place(x=250,y=250)

#command call corresponding function..

if __name__=='__main__':
    app.mainloop()

