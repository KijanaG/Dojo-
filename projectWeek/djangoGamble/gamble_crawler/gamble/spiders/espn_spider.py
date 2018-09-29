import scrapy
from gamble.items import GambleItem
import scrapy

class ESPNSpider(scrapy.Spider):
    name = "espn"
    start_urls = [
        'http://www.espn.com/mlb/schedule'
    ]

    def parse(self, response): 
        for i in range(3):
            table = response.css("tbody")[i]
            yield {
                'team_names': table.css("abbr::attr('title')").extract(),
                'images': table.css("img::attr('src')").extract(),
                'dates': table.css("td::attr('data-date')").extract()
            }

# class Games(scrapy.Item):
#     images = scrapy.Field()
#     team_names = scrapy.Field()
#     dates = scrapy.Field()
#     last_updated = scrapy.Field(serializer=str)

# import scrapy

# class AuthorSpider(scrapy.Spider):
#     name = 'author'

#     start_urls = ['http://quotes.toscrape.com/']

#     def parse(self, response):
#         # follow links to author pages
#         for href in response.css('.author + a::attr(href)'):
#             yield response.follow(href, self.parse_author)

#         # follow pagination links
#         for href in response.css('li.next a::attr(href)'):
#             yield response.follow(href, self.parse)

#     def parse_author(self, response):
#         def extract_with_css(query):
#             return response.css(query).extract_first().strip()

#         yield {
#             'name': extract_with_css('h3.author-title::text'),
#             'birthdate': extract_with_css('.author-born-date::text'),
#             'bio': extract_with_css('.author-description::text'),
#         }
