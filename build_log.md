## 190410
- switches from scrapy image downloader to file downloader. files are now downloading
- some of the links need to be repaired. only full https image links are downloaded but reddit links don't always include domain
- 

## 190409
- back from vacation. need to review project progess and outstanding items
- 19 days of digital ocean credit remaining
- current status: scrapy will pull data from the webpage and store to a json file after a manually typed command
- outstanding: download image, process the color, add the color tag relation to the image, create website
- updated schedule: download image and process color due 4/12; add the color tag relation and fully automate due 4/19; create website due 4/26; server shutdown 4/28
- documention will suffer, folder organization will suffer, automation will suffer, no longer able to include additional websites like instagram
- failed to get scrapy image downloading to work

## VACATION BREAK!!!!!
##
##

## 190308
- setup github repo with plans to self host with gitea in the future
- need to do documentation today. need a readme, change file formats to markdown, need week 1 report
- unrelated to project, i really want to start my dotfiles repo so maybe i'll do that today
- 

## 190307
- scrapy crawl posts -t json -o ./"%(time)s.json"
- success at running python code to scrape the website to a json file with todays date and time
- setup a manage.sh file to organize project commands

## 190306
- add user to docker sudo group
- create bash script to start docker with bash terminal
- first testing with scrapy
- success!!! at getting the image link scraped from console
- response.css("div.top-matter")[2].css("a").attrib['href']
- need to write the python code to automate 

## 190305
- scrapy has dependencies that aren't included in python
- testing docker build with pypy
- success in building and running the docker image
- pypy was required
- need to mount local directory inside the container so rebuilds aren't required every code change
- need to learn how to attach the container and run the code
- sudo docker run -it --rm --mount type=bind,source="$(pwd)",target=/app artisan
- need to make a docker compose
- need to learn how to run and debug

## 190302
- setup docker for python and pip package scrapy
- install docker for debian
- configure to start on boot
- unable to build docker image based on python 

## 190228
- signup for digital ocean trial
- $100 dollars for 2 months digital ocean trial
- setup debian droplet with 8GB RAM, 4 vCPUs, 160GB disk ($40/month)
- debian 9.7 x64
- secured with ssh key
- disabled root login
- disabled password login

