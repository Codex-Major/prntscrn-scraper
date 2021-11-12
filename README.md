# prntscrn-scraper
Due to the fact that prnt.sc openly hosts all of the uploaded photos publicly, we can generate a random string of chars and create a link. If
the link is a valid one, the scraper will automatically scan the webpage for the image and download it. Using `python3 find-text.py`, we
can automatically extract the text from the image files using pytesseract.

## Requirements
Install tesseract:

`sudo apt-get update; sudo apt-get install tesseract-ocr libtesseract-dev`

Git this script:

`git clone https://github.com/Codex-Major/prntscrn-scraper`

Install python3 OpenCV and other requirements

`cd prntscrn-scraper; pip3 install -r requirements.txt`

## scraper.py
This is just a simple scraper to generate random, 6 character, links for https://prnt.sc/ and download an image if there is one at that address.<br />

`python3 scraper.py`

![scraper_image](https://user-images.githubusercontent.com/10734039/137588474-0d5ffefa-165e-474b-a51c-2ef26aaf4d1f.png)


## find_text.py
This script uses pytesseract to find text in images and output it into a txt file in ./image_text/ <br />

`python3 find_text.py`

![findtext_image](https://user-images.githubusercontent.com/10734039/137588566-5379cb0c-e10f-484e-95f2-abba04b6d972.png)

## search_text.py
This script searches each file found by find_text.py for a given 'string', if it contains 'string' the .txt file will be placed into ./searches/'string'/<br />

`python3 search_text.py -s string`


![Screenshot_6](https://user-images.githubusercontent.com/39181001/141450540-0e859b50-e0ae-473f-b9e0-59714e85cf53.png)

