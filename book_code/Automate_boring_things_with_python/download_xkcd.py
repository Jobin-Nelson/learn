'''
Downloads every single xkcd comics
'''
import os
from requests_html import HTMLSession

def main():
    s = HTMLSession()
    url = 'https://xkcd.com'
    os.makedirs('xkcd', exist_ok=True)

    while not url.endswith('#'):
        print(f'Downloading page {url}')
        r = s.get(url)
        r.raise_for_status()

        comic = r.html.find('#comic img', first=True)
        if not comic:
            print('Could not find comic image')
        else:
            comic_url = 'https:' + comic.attrs['src']
            print(f'Downloading image {comic_url}')
            res = s.get(comic_url)
            res.raise_for_status()

            file_path = os.path.join('xkcd', os.path.basename(comic_url))
            with open(file_path, 'wb') as f:
                f.write(res.content)
        prev_link = r.html.find('a[rel="prev"]',first=True).attrs['href']
        url = 'https://xkcd.com' + prev_link
    print('Done')


if __name__ == '__main__':
    main()
