################################################
# Free to use, modify, and distribute.
#
# Connects to novelfull.com with web requests,
# downloads, and compiles into a single document.
#
# Works with website schema as of 25Dec2020
################################################

import requests
import argparse
import logging
import re
from html.parser import HTMLParser

class htmlparser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []
        self.next = ''
    def handle_starttag(self, tag, attrs):
        #[('class', 'btn btn-success'), ('href', '/beware-mr-officer-tread-carefully/chapter-4.html'), ('title', 'Chapter 4'), ('id', 'next_chap')]
        if tag == 'span' and attrs != [] and attrs[0] == ('class', 'btn btn-success') and attrs[3][1] == 'next_chap':
            self.tags.append(0)
    def handle_endtag(self, tag):
        pass
    def handle_data(self, data):
        if self.tags.count != 0:
            tag = self.tags.pop()
            if tag == 0:
                self.next = data
            else:
                logging.error('HTMLParser did not implement correctly on a handle')

def main(first, max, output, novel_name):
    for x in range(max):

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--first_chapter', '-f', help = 'URL of first chapter')
    parser.add_argument('--max_chapters', '-m', help = 'N amount of chapter DLs')
    parser.add_argument('--output_format', '-o', choices = ['text'],
        default = 'text' ,help = 'File format output')
    args = parser.parse_args()

    if type(args.first_chapter) is list:
        logging.info("Detected multiple requests")
        for x in args.first:
            name = re.search(r'https?:\/\/novelfull\.com\/(.+)\/',x.lower())
            novel_name = name[1]
            if name == None:
                logging.error('Could not parse ' + x + ', skipping')
                continue
            logging.info("Pulling " + novel_name)
            main(x, args.max_chapters, args.output_format, novel_name)
    else:
        name = re.search(r'https?:\/\/novelfull\.com\/(.+)\/',args.first_chapter.lower())
        novel_name = name[1]
        if name == None:
            logging.error('Could not parse ' + args.first_chapter + ', quitting')
            exit()
        logging.info("Pulling " + novel_name)
        main(args.first_chapter, args.max_chapters, args.output_format, novel_name)