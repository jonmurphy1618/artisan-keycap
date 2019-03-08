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
