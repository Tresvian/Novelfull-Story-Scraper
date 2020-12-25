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

def main(first, max, output):
    pass

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
            name = re.search(r'http[s]?:\/\/novelfull\.com\/(.+)\/',x.lower())
            if name == None:
                logging.error('Could not parse ' + x + ', skipping')
                continue
            logging.info("Pulling " + name[1])
            main(x, args.max_chapters, args.output_format)
    else:
        name = re.search(r'http[s]?:\/\/novelfull\.com\/(.+)\/',args.first_chapter.lower())
        if name == None:
            logging.error('Could not parse ' + args.first_chapter + ', quitting')
            exit()
        logging.info("Pulling " + name[1])
        main(args.first_chapter, args.max_chapters, args.output_format)