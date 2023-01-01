#import required...
#from tkinter import * 
#tkinter is for GUI in python
from pytube import YouTube
from flask import Flask,render_template,redirect,request 
#initialize..
root=Flask(__name__)

#handlers...
@root.route('/')
def dis():
    return render_template('index.html')
#from data..
@root.route('/data',methods=['post'])
def data():
    url=YouTube(request.form['url'].strip())
    '''video=url.streams.first()
    video.download()'''
    url.streams.get_highest_resolution().download()
    #video download....
    return render_template('index.html',m='Downloaded')
# main method...

if __name__=='__main__':
    root.run(debug=True)


