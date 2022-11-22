


# read quote file from quotes.txt
# with open('quotes.txt', 'r+', encoding="utf8") as f: # open file in read / write mode
#         firstLine = f.readline() # read the first line and throw it out
#         data = f.read() # read the rest
#         f.seek(0) # set the cursor to the top of the file
#         f.write(data) # write the data back
#         f.truncate() # set the file size to the current size



with open('quotes.txt', 'r+', encoding="utf8") as f: # open file in read / write mode
        firstLine = f.readline() # read the first line and throw it out
        quote = firstLine.split('-')[0]
        author = firstLine.split('-')[1]
        data = f.read() # read the rest
        f.seek(0) # set the cursor to the top of the file
        f.write(data) # write the data back
        f.truncate() # set the file size to the current size
        with open('posted_quotes.txt', 'a') as g:
            g.write(firstLine)
