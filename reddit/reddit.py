# -*- coding: utf-8 -*-
API_KEY = "128657a01b7523fffa14df84ee9bb964_sr98766_ooPq87"


import scrapy

URL = "https://www.reddit.com/r/funny/"

class OurfirstbotSpider(scrapy.Spider):
    name = 'ourfirstbot'
    start_urls = [
    F"http://api.proxiesapi.com/?auth_key={API_KEY}&url={URL}"
    ]

    def parse(self, response):
        titles = response.css("._eYtD2XCVieq6emjKBH3m::text").extract()
        permalink = response.css("._292iotee39Lmt0MkQZ2hPV RichTextJSON-root::text").extract()
        titles = response.css("._2q7IQ0BUOWeEZoeAxN555e _3SUsITjKNQ7Tp0Wi2jGxIM qW0l8Af61EP35WIG6vnGk _3edNsMs0PNfyQYofMNVhsG::text").extract()
        permalink = response.css("._1iKd82bq_nqObFvSH1iC_Q Q0BxYHtCOJ_rNSPJMU2Y7 _2fe-KdD2OM0ciaiux-G1EL _3yQIOwaIuF6gn8db96Gu7y::text").extract()        

        for item in zip(titles, comments):
            all_items = {
                "title": item[0],
                "comment": item[1],
                "ups": item[2],
                "downs": item[3]
            }

            yield all_items
