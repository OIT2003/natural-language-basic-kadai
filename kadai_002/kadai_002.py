import re
import MeCab
from bs4 import BeautifulSoup
from urllib import request

main_url = "https://www.aozora.gr.jp/cards/000148/files/2371_13943.html"
stop_url = "http://svn.sourceforge.jp/svnroot/slothlib/CSharp/Version1/SlothLib/NLP/Filter/StopWord/word/Japanese.txt"

main_response = request.urlopen(main_url)
main_soup = BeautifulSoup(main_response)

stop_response = request.urlopen(stop_url)
stop_soup = BeautifulSoup(stop_response)

main_response.close()
stop_response.close()

main_text = main_soup.find("div", class_ = "main_text")
main_tags_delete = main_text.find_all(["rp", "rt"])

for tag in main_tags_delete:
    tag.decompose()

main_text = main_text.get_text()
main_text = re.sub(r"[\u3000 \n \r]", "", main_text)

stop_text = stop_soup.text
stoptext_list = stop_text.split("\r\n")
stoptext_list = [word for word in stoptext_list if word]

mecab_tagger = MeCab.Tagger("-Owakati")
main_text = mecab_tagger.parse(main_text)

main_text_list = main_text.split(" ")
result_text_list = list()

for split_text in main_text_list:
    if split_text not in stoptext_list:
        result_text_list.append(split_text)

print(result_text_list)
