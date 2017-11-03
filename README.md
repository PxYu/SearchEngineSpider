# Search Engine Spider

## prerequisite
+ python 2.7
+ scrapy
+ scrapy-fake-useragent (`pip install scrapy-fake-useragent`)

conda install or pip install anything else you are prompted.

## configuration

You can change some of the features in the `settings.py` to suit to your need.

+ database information, obviously. (`database.sql` help you build the database and tables)
+ `TOP_N` is the top number of documents to retrieve from search pages.
+ `DOWNLOAD_DELAY` is the number of seconds between requests.

## usage

In the project folder, run `scrapy crawl keywordSpider -a keyword_file=keywords.txt -a se=google`.
Every keyword takes up a line in `keywords.txt`.
