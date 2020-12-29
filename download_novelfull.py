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
from html.parser import HTMLParser


class htmlparser(HTMLParser):
	def __init__(self):
		super().__init__()
		self.tag = 0
		self.next = ''
		self.contents = ''
		
	def handle_starttag(self, tag, attrs):
		# Scrape Next link
		if tag == 'a' and ('id', 'next_chap') in attrs:
			for x in attrs:
				if x[0] == 'href':
					self.next = x[1]
		
		# Scrape contents
		if tag == 'div' and ('id', 'chapter-content') in attrs:
			self.tag = 2
			
		# End marker of contents. Done here to prevent some extra text.
		if self.tag == 2 and tag == 'div' and ('align', 'left') in attrs:
			self.tag = 0

	def handle_endtag(self, tag):
		pass

	def handle_data(self, data):
		if self.tag != 0:
			if self.tag == 2:
				if data != None:
					self.contents += data + '\n'
			else:
				logging.error('HTMLParser did not implement correctly on a handle')

	def returnNext(self):
		value = self.next
		self.next = ''
		return value

	def returnContents(self):
		value = self.contents
		self.contents = ''
		return value


def main(first, max, output, novel_name):
	website = 'http://novelfull.com'
	parser = htmlparser()
	if output == 'text':
		output = text()
		
	for x in range(max):
		getting = requests.get(first)
		if getting == None or not getting.ok:
			logging.error('Could not get good response from Novelfull: ' + first)
			exit()
			
		parser.feed(getting.text)
		next = parser.returnNext()
		if next != '':
			first = website + next
		print(parser.returnContents())
		print('-'*10 + ' DEMARCATION ' + '-'*10 + '\n')
		
		# Here, add the handler for output
		
		if next == '':
			logging.info('Hit stop from unavailable chapter: ' + first)
			break


class output_main:
	pass
	
	
class text(output_main):
	pass
	

if __name__ == '__main__':
	logging.basicConfig(level = logging.INFO, format='[%(levelname)s] %(message)s')
	logging.info('-'*70)
	logging.info('Novelfull Story Downloader - 29Dec2020 Version')
	logging.info('Latest copy https://github.com/Tresvian/Novelfull-Story-Scraper')
	logging.info('Free for distribution, modification, and (reasonable) pull requests')
	logging.info('-'*70)
	parser = argparse.ArgumentParser()
	parser.add_argument('--first_chapter', '-f', help = 'URL of first chapter', required = True)
	parser.add_argument('--max_chapters', '-m', help = 'N amount of chapter DLs', type = int, required = True)
	parser.add_argument('--output_format', '-o', choices = ['text'],
		default = 'text', help = 'File format output')
	args = parser.parse_args()

	if args.max_chapters < 0:
		logging.error('Cannot have negative chapters')
		exit()

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