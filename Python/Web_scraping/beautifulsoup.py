from bs4 import BeautifulSoup
import requests

# scraping newegg site for graphics card price
url = "https://www.newegg.com/gigabyte-radeon-rx-6700-xt-gv-r67xtgaming-oc-12gd/p/N82E16814932416?Description=graphics&cm_re=graphics-_-14-932-416-_-Product"

result = requests.get(url)
doc = BeautifulSoup(result.text,"html.parser")
prices = doc.find_all(text="$")
parent = prices[0].parent
strong = parent.find("strong")
print(strong.string)