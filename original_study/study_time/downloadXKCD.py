import requests, os, bs4

url = 'https://xkcd.com/'    # starting the url
os.makedirs('xkcd', exist_ok=True)    # store comics in ./xkcd
while not url.endswith('#'):
    # TODO: Download the page.
    print(f'Download page {url}...')
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # TODO: Find the URL of the comic image.
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        comicUrl = 'https:' + comicElem[0].get('src')

        # TODO: Download the image.
        print(f'Downloading image...{comicUrl}')
        res = requests.get(comicUrl)
        res.raise_for_status()

        # TODO: Save the image to ./xkcd.
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

        # TODO: Get the Prev button's url.
        prevLink = soup.select('a[rel="prev"]')[0]
        url = 'https://xkcd.com/' + prevLink.get('href')

print('Done.')