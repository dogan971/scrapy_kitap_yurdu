import scrapy


class KitapYurduSpider(scrapy.Spider):
    name = "kitap_yurdu"     
    start_urls = [
            "https://www.kitapyurdu.com/index.php?route=product/best_sellers&list_id=16&filter_in_stock=1&filter_in_stock=1&limit=100"
        ]
         

    def parse(self, response):
        for data in response.css("div.product-cr"):
            yield{
                "title":data.css("div.ellipsis a span::text").get(),
                "image":data.css("div.image div.cover a.pr-img-link img::attr(src)").get(),
                "author":data.css("div.author.compact a::text").get().lstrip(),
                "price":data.css("div.price span.value::text").get().lstrip()
            }
        
