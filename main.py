from libgen_api import LibgenSearch
import urllib.request
import pprint

book = str(input("What is the book title?: "))

s = LibgenSearch()
title_filters = {"Extension": "pdf"}
results = s.search_title_filtered(book, title_filters, exact_match=True)
pp = pprint.PrettyPrinter(indent=2)
pp.pprint(results)

item_to_download = results[0]
download_links = s.resolve_download_links(item_to_download)
url = download_links["Cloudflare"]

def main():
    download_file(url)

def download_file(url):
    response = urllib.request.urlopen(url)
    file = open(book + ".pdf", 'wb')
    file.write(response.read())
    file.close()
    print("Completed")

main()