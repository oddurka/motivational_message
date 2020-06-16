
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

# Gets the quote and author of the day from www.brainyquote.com, and returns them as a tuple
def get_quote():
    import requests
    from bs4 import BeautifulSoup

    URL = 'https://www.brainyquote.com/quote_of_the_day'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    results = soup.find("div", {"class": 'qll-bg'}).findAll("a")
    quote = results[0].get_text()
    author = results[1].get_text()

    return (quote, author)

print(get_quote())

