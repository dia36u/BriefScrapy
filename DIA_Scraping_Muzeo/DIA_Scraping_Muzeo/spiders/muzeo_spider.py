import scrapy

# Récupère les URL à partir du fichier .txt
def splitURL(txt):
    my_file = open(txt, "r")
    content = my_file.read()
    url = content.splitlines()
    return url
 
class MuzeoSpider(scrapy.Spider):
    name = "muzeo"
    start_urls = splitURL(r"URL_toscrap.txt")

    def parse(self, response):
         for oeuvre in response.css('div.oeuvre_container'):
       
       #Recupère le titre, l'auteur, l'url de l'image et le prix sur la liste d'URL 
            yield {
                'title': oeuvre.css("h3 a::attr(title)").get(),
                'author': oeuvre.css("div.oeuvre_container h3 a span::text").get(),
                'urlImage': oeuvre.css("h3 a::attr(href)").get(),
                'price' : oeuvre.css("div.oeuvre_container div::text").get()
            }