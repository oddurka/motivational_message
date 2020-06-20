
# Checks what OS the script is running on
def check_os():
    from sys import platform
    if platform == "linux" or platform == "linux2":
        # linux
        return "Linux"
    elif platform == "darwin":
        # OS X
        return "OS X"
    elif platform == "win32":
        # Windows...
        return "Windows"

# Gets the quote and author of the day from www.brainyquote.com, and returns them as a dict
def get_quote():
    import requests
    from bs4 import BeautifulSoup

    URL = 'https://www.brainyquote.com/quote_of_the_day'
    # Gets the html code for the given url
    page = requests.get(URL)

    # Makes the data easier to interact with
    soup = BeautifulSoup(page.content, 'html.parser')

    results = soup.find("div", {"class": 'qll-bg'}).findAll("a")

    res = {
        "quote": results[0].get_text(),
        "author": results[1].get_text()
    }

    return res

#print(get_quote())


# start a terminal window and displays the quote of the day
def start_terminal_windows():
    import os
    quote = get_quote()

    # Saves the quote to a txt file for easier display options
    quoteFile = open('quoteFile.txt', 'w+')
    quoteFile.write("### QUOTE OF THE DAY ###\n" + quote.get("quote") + '\n  -' + quote.get("author") + "\n #######################")
    quoteFile.close()

    # The CMD command
    os.system("start type quoteFile.txt")

start_terminal_windows()


