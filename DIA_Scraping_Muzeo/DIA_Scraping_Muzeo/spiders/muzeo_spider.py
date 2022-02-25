import scrapy

# Récupère les URL à partir du fichier .txt
def splitURL(txt):
    my_file = open(txt, "r")
    content = my_file.read()
    url = content.splitlines()
    return url

class MuzeoSpider(scrapy.Spider):
    name = "muzeo"

    def start_requests(self):
        start_urls = splitURL("C:/Users/utilisateur/OneDrive - Simplonformations.co/WebScraping/DIA_Scraping_Muzeo/URL_toscrap.txt")
    
    def parse(self, response):
            yield {
                'title': response.css('div.title').get()
            }
