from scrapy import Spider, Request
class BooksSpider(Spider):
    name = 'books'
    start_urls = ["http://books.toscrape.com"]
    page = 1
    def parse(self, response):
        books = response.xpath("//li[@class='col-xs-6 col-sm-4 col-md-3 col-lg-3']")  # Ajustado para selecionar o div correto
        for book in books:
            title = book.xpath(".//h3/a/@title").get(),
            price = book.xpath(".//p[@class='price_color']/text()").get(),
            stock = book.xpath(".//p[@class='instock availability']/text()").get().strip(),

            yield {
                "title": title,
                "price": price,
                "stock": stock,
            }
        self.page = self.page + 1
        yield Request(f"http://books.toscrape.com/catalogue/page-{self.page}.html",self.parse)