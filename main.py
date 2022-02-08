from libgen_api import LibgenSearch
import urllib.request
import os

book = str(input("Book Name: "))

s = LibgenSearch()
results = s.search_title(book)
print(results)

print("\n\n")
print("Download links:")

item_to_download = results[0]
download_links = s.resolve_download_links(item_to_download)
print(download_links)

url = ""

def main():
    download_file(url)

def download_file(url):
    response = urllib.request.urlopen(url)
    file = open(book + ".pdf", 'wb')
    file.write(response.read())
    file.close()
    print("Completed")

main()