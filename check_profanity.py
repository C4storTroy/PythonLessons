import urllib

def read_text():
    quotes = open("/home/castor/Documents/Nanodegree/FullStack/Python/movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    conn = urllib.urlopen("http://www.wdyl.com/profanity?q="+text_to_check)
    output = conn.read()
    print(output)
    conn.close()
    if "true" in output:
        print("Profanity Alert!!")
    elif "false" in output:
        print ("This document has no curse words")
    else:
        print("Could not scan the document properly")


read_text()
