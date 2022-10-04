from pickle import TRUE
from bot.scraper import Bot

with Bot(teardown=TRUE) as bot:
    # bot.load_all_houses(url='https://www.prd.com.au/oatley/property-search/?listing_type=Sale&property_status=Sold')
    bot.collect_house_info()