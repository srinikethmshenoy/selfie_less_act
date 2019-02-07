import os
from flask import Flask,render_template,request
__author__="sriniketh"

app=Flask(__name__)

APP_ROOT=os.path.dirname(os.path.abspath(__file__))
@app.route("/")
def index():
	return render_template("upload.html")
@app.route("/upload", methods=['POST'])
def upload():
	target=os.path.join(APP_ROOT,"images/")
	print(target)  # to verify that the file is getting uploaded correctly

	if not os.path.isdir(target): #if the dir doesnot exist we must make it
		os.mkdir(target)

	for file in request.files.getlist("file"):	   # for the files selected by the user in the frontend
		print(file)
		filename=file.filename  #gives the file name of the file upploaded
		destination="/".join([target,filename])
		print(destination)
		file.save(destination)  # to save to the destination
	return render_template("exit.html")

if(__name__=="__main__"):
	app.run(port=4555,debug=True)	