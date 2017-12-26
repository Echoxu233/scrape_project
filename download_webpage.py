from urllib.request import urlopen

url  = "https://search.azlyrics.com/search.php?q=the+chainsmokers&w=songs&p=1"

def get_webpage(url):

    print("Getting Request Object")
    request = urlopen(url)
    print("Reading Request Object")
    data = request.read()
    text = data.decode("utf-8")

    print("Web Page Downloaded")
    return text

text = get_webpage(url)

with open('html_text.txt', 'w') as f:
    f.write(text)
