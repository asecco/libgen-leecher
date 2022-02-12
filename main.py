from libgen_api import LibgenSearch
import urllib.request
import pprint

print("\nWelcome to LibGen Leecher\n")

def main():
    download_file(url)

def download_file(url):
    book_download = book.replace(":","")
    response = urllib.request.urlopen(url)
    file = open(book_download + ".pdf", 'wb')
    file.write(response.read())
    file.close()
    print("\nDownload complete. Enjoy!")

def search():
    try:
        global book
        book = str(input("What is the book title? "))
        s = LibgenSearch()
        title_filters = {"Extension": "pdf"}
        results = s.search_title_filtered(book, title_filters, exact_match=True)
        
        pp = pprint.PrettyPrinter(indent=2, width=150)
        print("\nResults: \n")
        results_items = results[0].items()
        results_filters = list(results_items)[1:8]
        pp.pprint(results_filters)

    except IndexError:
        pass
        print("\nNo results. Try refining your search\n")
        search()
    
    if results:
        item_to_download = results[0]
        download_links = s.resolve_download_links(item_to_download)
        global url
        url = download_links["Cloudflare"]
        
        correct_book = str(input("\nIs this the book you're looking for? [y/n] "))
        if correct_book == "y":
            main()
        elif correct_book == "n":
            print("\nPlease refine your search\n")
            search()
        else:
            print("\nInvalid input. \nExiting.")
            quit()
search()