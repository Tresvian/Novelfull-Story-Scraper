# Novelfull-Story-Scraper
Downloads and compiles full web novels from Novefull into a local copy for offline and ease of view.

## Requires
* Python3

* Internet access

## Usage
1. Download the git repo, and navigate to the python script.
2. Launch a command line and run the script with a few required arguments
  * *-m* for Maximum amount of chapters to download
  * *-f* for First chapter link
  
 ```python .\download_novelfull.py -m 5 -f https://novelfull.com/reborn-girls-new-life/chapter-527-beg-for-an-amulet.html```
 
  * Multiple stories can be added to download in a queue.
  
  ```python .\download_novelfull.py -m 5 -f https://novelfull.com/reborn-girls-new-life/chapter-527-beg-for-an-amulet.html,https://novelfull.com/the-rise-of-otaku/chapter-271-send-back.html```
  
3. TODO: For now, this just outputs it in the console.
