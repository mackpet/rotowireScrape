# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import scrapy

from rotowire.items import RotowireItem

class RotowireSpider(scrapy.Spider):
    name = "rotowire"
    allowed_domains = ["rotowire.com"]

    start_urls = [
    	"http://www.rotowire.com/daily/nba/defense-vspos.htm?site=DraftKings&statview=last10",
    	"http://www.rotowire.com/daily/nba/defense-vspos.htm?site=DraftKings&statview=last10&pos=SG",
    	"http://www.rotowire.com/daily/nba/defense-vspos.htm?site=DraftKings&statview=last10&pos=G",
    	"http://www.rotowire.com/daily/nba/defense-vspos.htm?site=DraftKings&statview=last10&pos=SF",
    	"http://www.rotowire.com/daily/nba/defense-vspos.htm?site=DraftKings&statview=last10&pos=PF",
    	"http://www.rotowire.com/daily/nba/defense-vspos.htm?site=DraftKings&statview=last10&pos=F",
    	"http://www.rotowire.com/daily/nba/defense-vspos.htm?site=DraftKings&statview=last10&pos=C"    
	]

	def parse(self, response):
		
		for 



