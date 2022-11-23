from imgs import *  # gets all functions and their names
import time
from instagrapi import Client
# from pathlib import Path
from instagrapi.types import StoryMention, StoryMedia, StoryLink, StoryHashtag
import json
import os
from random import randint
from time import sleep




def get_quote_from_quotes_txt_for_instapost():
    with open('quotes.txt', 'r+', encoding="utf8") as f: # open file in read / write mode
        firstLine = f.readline() # read the first line and throw it out
        quote = firstLine.split('-')[0]
        author = firstLine.split('-')[1]
        # check if quote already quoted
        with open('posted_quotes.txt', 'r+') as g:
            if quote in g.read():
                print("Quote found in posted_quotes, fetching another one...")
                print(quote)
                print('fuckthisloop')
                data = f.read() # read the rest
                f.seek(0) # set the cursor to the top of the file
                f.truncate() # set the file size to the current size
                f.write(data + "\n") # write the data back
                return get_quote_from_quotes_txt_for_instapost()
            else:
                if len(quote) < 3:
                    print('Quote is too short, fetching another one...')
                    data = f.read() # read the rest
                    f.seek(0) # set the cursor to the top of the file
                    f.truncate() # set the file size to the current size
                    f.write(data + "\n") # write the data back
                    return get_quote_from_quotes_txt_for_instapost()
                if len(quote) < 501:
                    quote_len_under_500 = True
                    data = f.read() # read the rest
                    f.seek(0) # set the cursor to the top of the file
                    f.truncate() # set the file size to the current size
                    f.write(data + "\n") # write the data back
                    g.write(firstLine)
                    return (quote, author)
                else:
                    print('Quote is too long, fetching another one...')
                    data = f.read() # read the rest
                    f.seek(0) # set the cursor to the top of the file
                    f.truncate() # set the file size to the current size
                    f.write(data + "\n") # write the data back
                    return get_quote_from_quotes_txt_for_instapost()




def read_password_file(filepath):
    """
    Read and return the user/password file.
    """
    try:
        with open(filepath, 'r') as fd:
            lines = fd.readlines()
            fd.close()
            return lines
    except IOError:
        raise ValueError("Can't open password file for reading.")


(message, author) = get_quote_from_quotes_txt_for_instapost()


# up to 260 incl. fontsize: 72, width 20
# up to 120 incl. fontsize: 72, width 16

#                                                  run program:
with open('status.json', 'r') as openfile:
    # Reading from json file
    status_object = json.load(openfile)

print(status_object)
print(type(status_object))
#                                                login to account
if 'session.json' in os.listdir():
    with open('session.json', 'r') as f:
        cl_session = json.load(f)
else:
    cl_session =  {}


cl = Client(cl_session)
username = 'moneyfest001@outlook.com'
password = read_password_file('./.pass')[0]

cl.login(username, password)

with open('session.json', 'w') as f:
    json.dump(cl.get_settings(), f)

#                                                 generate story
get_image_from_unsplash()
create_image_with_message(message, 'story')

#                                                   post story
path = ".\\result.jpg"
cl.photo_upload_to_story(path)


#                                             generate and post photo
create_image_with_message(message, 'post')
cl.photo_upload(path, caption=(message + ' -' + author + '\n\n\n #motivational #quoteoftheday #motivationalquotes #motivation #quotes #inspiration #success #mindset #inspirationalquotes #love #positivity'))
