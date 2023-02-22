# instapy-and-image-generator
This is an instagram bot that takes a random image from unsplash, puts a motivational text quote on it and posts it as a normal post or as a story on an Instagram account. 

This project has forthcoming implementations for Like, Comment and Follow features. These are not yet implemented.



# Installation

1. Clone the repository
2. use `pip install -r requirements.txt` command to install all of the Python modules and packages listed in thre requirements.txt file
3. Create a file called `.pass` in the main folder (instapy-and-image-generator).
4. inside the `.pass` file write your YouTube account password one the first line.
5. Open up in your text editor `main.py` and change the username (search for it) variable to whatever your Instagram account username is.
6. Open CMD and navigate inside the main folder and write `python main.py post`. This is done like this because it is expecting an argument. With `post` the app makes a normal post but also a story with that post.


# Opening with jupyter notebook
To better test this program and to add new funtionalities, you can use the Jupyter Notebook. This allows you to add snippets of code without having to restart the whole application. To launch the jupyter notebook:

1. navigate to the main folder in CMD
2. launch the virtual environment by writing in CMD:
```
py -m venv instaenv
cd instaenv\Scripts\
activate
```

To disable your new virtual env write in CMD `deactivate`

3. in the virtual environment write 
`jupyter notebook`
4. click on the `notebook.ipynb` notebook

I recommend copying snippets of code from `main.py` to `notebook.ipnyb` to test them out and improve them. Then copy them back to `main.py` file.



# Contents
In this section various contents of the app will be described. They are in alphabetical order.

## blue-heart.png
This is a small png image used as logo on all images.

## imgs.py
Here is where the image generation computation takes place. It looks at various resolutions and adapts the text.

## launch_main_python_file.bat
This is useful when you want to automate this script with Windows Task Scheduler. You can make it such that this script gets run for example three times a day. Make sure to edit the path according to your system.

## main.py 
The main Python file.

## notebook.ipnyb
This is the Jupyter notebook to be opened for application testing and development.

## posted_quotes.txt
In this file are stored quotes that have already been posted on the instagram page.

## quotes.txt
This is the main quotes file. This is a large collection of quotes with the following format
`quote -Author`
The minus sign is mandatory as it is searched for in the application.

This file gets smaller with time as the quotes get moved line by line to the `posted_quotes.txt` file.
## quotes Copy.txt
This is just a copy of the original quotes file

# Troubleshooting
This section is to help you go through a password change and things similar to this which require that you edit program files.

## Instagram Password Change
If you change your account password, you need to update the `.pass` file and delete the `session.json` file as this keeps in memory your old session with your old password and the login will fail.
