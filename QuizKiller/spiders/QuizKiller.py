"""
Created on Thu Apr  6 17:13:20 2017

@author: dt

To run this spider:
    scrapy crawl quizkiller
    or run.sh in root folder
"""


from scrapy.spider import Spider #scrapy.spiders in python 3
from scrapy.selector import Selector
#from QuizKiller.items import QuizkillerItem
from QuizKiller.settings import *
from scrapy.http import FormRequest
import os
import sys
import pandas as pd
import scrapy
from datetime import datetime
from scrapy.mail import MailSender
from send_mail import *
import time
from scrapy.exceptions import CloseSpider

regression_url = "https://chalk.uchicago.edu/webapps/blackboard/content/listContent.jsp?course_id=_168537_1&content_id=_3485492_1"
email_receiver = [""]

class QuizKillerSpider(Spider):
    name = 'quizkiller'
    # start_urls = [regression_url]
    def start_requests(self):            
        yield scrapy.Request(regression_url, callback = self.parse, dont_filter=True, headers=DEFAULT_REQUEST_HEADERS)  

    def parse(self, response):       
        message = response.xpath("//div[@class='main-message']/text()").extract()
        print(message)
        #message = None
        if not message or message == "" or message[0].strip()!='There is no content to display.':
            send(content='Regression quiz!', To=email_receiver)
            print('QUIZ!!! Email notification sent!')
            raise CloseSpider(reason='Quiz found')
            
        else:
            print('No quiz')
            if datetime.now().strftime('%H:%M:%S')<="22:00:00":
                yield scrapy.Request(regression_url, callback = self.parse, dont_filter=True, headers=DEFAULT_REQUEST_HEADERS)

            return {'quiz': 0}
        
        
