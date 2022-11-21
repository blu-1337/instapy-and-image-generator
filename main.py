from imgs import *  # gets all functions and their names
import time
from instagrapi import Client
# from pathlib import Path
from instagrapi.types import StoryMention, StoryMedia, StoryLink, StoryHashtag
import json


def get_random_quote():  # returns quote string
    try:
        quote_len_under_500 = False
        while(not quote_len_under_500):
            ## making the get request
            response = requests.get("https://quote-garden.herokuapp.com/api/v3/quotes/random")
            if response.status_code == 200:
                ## extracting the core data
                json_data = response.json()
                data = json_data['data']

                ## getting the quote from the data
                quote = data[0]['quoteText']
                author = data[0]['quoteAuthor']
                if len(quote) < 501:
                    quote_len_under_500 = True
                    return (quote, author)
                else:
                    print('Quote is too long, fetching another one')
            else:
                print("Error while getting quote")
    except Exception as e:
        print("Something went wrong! Try Again! Exception was: ", e)


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


(message, author) = get_random_quote()

# message2 = "When you say you suffer from a physical illness, you get sympathy. When you say you suffer from depression, you sometimes get blamed. We know it sucks, but at the very least, please take solace in the fact that you are not alone – as evidenced by the fact that 350 million people in the world struggle with depression."
#
# message3 = 'asdf asdf asdf asdf asdf asdf asdf asdf asdf asdf asdf asdf asdf asdf asdf asdf asdf asdf asdf qwe qwer qwer qwer qwer qwer asdf asdf asdf qwer qwef qwef qwef asdf asdf qwef qwefq wef qwef asdf asdf qwef asdf awef awefa wef awef awef asdf asdf asd fasd fasdf asdf asdf '
# message4 = 'Alwaysaa try to end the day with a positiveday with a positiveday with a positive thought. No matter how hard as df'
# message5 = 'giochero per vincere niggas be niggas all the time no cap we strong brosefinos leggo my birtth light'
# message25 = "Lorem ipsum dolor sit ame"
# message50 = "Lorem ipsum dolor sit amet, consectetuer adipiscin"
# message120 = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis nat"  # average quote size
# message220 = 'Lorem ipsum dolor sit amet, consectetueradipiscing welit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies.'
# message260 = 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem.'
# message325 = 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel'
# message500 = 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibu'


# up to 260 incl. fontsize: 72, width 20
# up to 120 incl. fontsize: 72, width 16

#                                                  run program:
with open('status.json', 'r') as openfile:
    # Reading from json file
    status_object = json.load(openfile)

print(status_object)
print(type(status_object))
#                                                login to account
cl = Client()
username = 'motivation_blu'
password = read_password_file('./.pass')[0]

cl.login(username, password)

#                                                 generate story
get_image_from_unsplash()
create_image_with_message(message, 'story')

#                                                   post story
path = ".\\result.jpg"
cl.photo_upload_to_story(path)


#                                             generate and post photo
create_image_with_message(message, 'post')
cl.photo_upload(path, caption=(message + ' -' + author + '\n\n\n #motivational #quoteoftheday #motivationalquotes #motivation #quotes #inspiration #success #mindset #inspirationalquotes #love #positivity'))
