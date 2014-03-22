## About

`Scrapy` is open-source web scraping framework for Python. This
repostiroy contains scrapy spiders for some myanmar websites — that I
crawled previously for data collection.

## Usage

* Install `python2.7`, `pip2.7`.
```bash
sudo apt-get install python python-pip
```

* Install scrapy and other necessary python packages
```bash
sudo pip install Scrapy
```

* Install [python-myanmar](https://github.com/trhura/python-myanmar) (needed to convert zg->uni)

* Run the spider using scrapy.
```bash
scrapy runspider ..._spider.py
```
