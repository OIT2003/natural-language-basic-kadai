import re
from bs4 import BeautifulSoup
from urllib import request

url = "https://www.aozora.gr.jp/cards/000148/files/2371_13943.html"

response = request.urlopen(url)
soup = BeautifulSoup(response)

response.close()

main_text = soup.find("div", class_ = "main_text")
tags_to_delete = main_text.find_all(["rp", "rt"])

for tag in tags_to_delete:
    tag.decompose()

main_text = main_text.get_text()
main_text = re.sub(r"[\u3000 \n \r]", "", main_text)

print(main_text)
