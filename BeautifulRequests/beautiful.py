import requests
import bs4

def get_text(page):
    title = []
    data = []
    try:
        r = requests.get(page)
    except:
        return -99, 'ERROR: Page doesnt exist', ''   
    
    if r.status_code != 200:
            return r.status_code, title, data

    soup = bs4.BeautifulSoup(r.text, "lxml")

    title = soup.title.text

    for pelem in soup.find_all('p'):
        data.append(pelem.get_text())
    data = ",".join(data)

    return r.status_code, title, data


def get_image(page):
    images = []
    r = requests.get(page)
    if r.status_code != 200:
        return r.status_code, images

    soup = bs4.BeautifulSoup(r.text, "lxml")
    for link in soup.find_all('img'):

        images.append(link.get("src"))

    return r.status_code, images

def get_link(page):
    link = []
    r = requests.get(page)
    if r.status_code != 200:
        return r.status_code, link

    soup = bs4.BeautifulSoup(r.text, "lxml")
    for pelem in soup.find_all('a'):
        link.append(pelem.get('href'))

    return r.status_code, link

if __name__ == '__main__':
        page = "http://pythonforengineers.com"    
        print(get_text(page))
        print("\n\n")
        print(get_image(page))
        print("\n\n")
        print(get_link(page))