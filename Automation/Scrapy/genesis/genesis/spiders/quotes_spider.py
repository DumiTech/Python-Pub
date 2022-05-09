import scrapy

from ..items import GenesisItem


class QuoteSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response):

        items = GenesisItem()

        quote_blocks = response.css("div.quote")

        for i in range(0, len(quote_blocks)):
            quote_blocks = response.css("div.quote")[i]
            title = quote_blocks.css("span.text::text").extract()
            author = quote_blocks.css("small.author::text").extract()
            tags = quote_blocks.css("a.tag::text").extract()

            items["title"] = title
            items["author"] = author
            items["tags"] = tags

            print()

            yield items
        
        next_page = response.css("li.next a::attr(href)").get()

        if next_page is not None:
            yield response.follow(next_page, callback = self.parse)

            # yield {
            #     'title': title,
            #     'author': author,
            #     'tags': tags
            # }
