# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RotowireItem(scrapy.Item):
	team = scrapy.Field()
	position = scrapy.Field()
	season = scrapy.Field()
	lastFive = scrapy.Field()
	lastTen = scrapy.Field()
	pts = scrapy.Field()
	reb = scrapy.Field()
	stl = scrapy.Field()
	ast = scrapy.Field()
	blk = scrapy.Field()
	threePtFGMade = scrapy.Field()
	fieldGoalPercent = scrapy.Field()
	freeThrowPercent = scrapy.Field()
	turnovers = scrapy.Field()
    pass
