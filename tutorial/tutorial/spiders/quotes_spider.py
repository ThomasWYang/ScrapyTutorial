import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }

        yield from response.follow_all(css='ul.pager a', callback=self.parse)

# region Substitute code for above
        # next_page = response.css('li.next a::attr(href)').get()
        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.parse)
# endregion

# region Generate webpages
        # page = response.url.split("/")[-2]
        # filename = f'quotes-{page}.html'
        # with open(filename,'wb')as f:
        #     f.write(response.body)
        # self.log(f'Saved file {filename}')
# endregion
