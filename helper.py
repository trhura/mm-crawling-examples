import codecs
import os

class ItemManager ():
    def __init__ (self, spider_name, maxitem=5000):
        self.spider = spider_name
        self.maxitem = maxitem
        self.file_count = 0
        self.item_count = 0
        self.cfile = None

    def exit (self):
        if self.cfile != None:
            self.cfile.close ()

    def add_item (self, para):
        if self.cfile == None:
            self.open_file ()
            self.item_count = 0
            self.file_count = self.file_count + 1

        self.cfile.write (para + '\n')
        self.item_count = self.item_count + 1

        if self.item_count >= self.maxitem:
            self.cfile.close ()
            self.cfile = None

    def open_file (self):
        cpath = os.path.dirname(os.path.abspath (__file__))
        spider_path = os.path.join (cpath, "data", self.spider)

        if (not os.path.exists (spider_path)):
            os.makedirs (spider_path)

        self.cfile = codecs.open (os.path.join (spider_path,
                                                '%05d.txt' %self.file_count),
                                  'w', encoding='utf-8')

def is_myanmar_char  (character):
    return ord (character) >= 0x1000 and ord (character) <= 0x104F

def is_large_paragraph (paragraph):
    # more than 30 chars
    return len(paragraph) > 30

def is_mainly_myanmar (paragraph):
    # more than half of paragraph is myanmar text
    return len(filter(is_myanmar_char, paragraph)) > (len(paragraph)/2)