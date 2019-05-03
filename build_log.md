## 190503
- add try/except to colorscan so all images get values
- fixed colorscan.py to add 0 color values for failed images
- scrapy json append is a new set instead of expanding the previous, need to revise the colorscan.py to accomodate
- failed to get json with multiline to import correctly. maybe try jsonlines format, open file and then import each fileline as json,

## 190502
- success button filters are now working with json data added with jquery, the filter had to run after the jquery loaded data to the page
- removed all the debug prints, removed excess comments, removed temp images used for testing
- todo finalize the colortag script to add default 0 values if image can't be scanned
- todo finalize the scrapper to pull more images
- todo finalize the css so the page looks nice

## 190501
- new server up and running!!
- using AWS EC2 with the free credit time. it's not clear how much the free portion covers
- setting up webserver after moving was super easy. just needed to get ssh keys setup for git and server, and install docker
- success jquery and javascript are outputting the correct html
- failed filtering doesn't see jquery applied attributes for colors
- might have something to do with active and static lists

## 190426
- server is out of time
- moving the webserver and html/css/js to the github folder

## 190425
- testing phone remote setup while at work meetings
- meh, not much time for working. maybe if i find somewhere closer to eat
- need to install mosh, setup keyboard shortcuts 

## 190424
- attempting to filter today
- also need to format the data into something usable today instead of just <p>
- success at filtering!! got filtering to work with static HTML code. 
- todo queryselect based on color values
- todo fix the colorscanner script to add zero values if the image fails
- https://stackoverflow.com/questions/2613648/jquery-selecting-all-elements-where-attribute-is-greater-than-a-value

## 190423
- success at full json import into html
- success at formatting the code into something readable
- jquery could use clone() but is not implemeneted at this time
- todo color processing script needs to add zero values if the image fails
- failed at filtering so far, seems like a few options and it's possible
- http://fofwebdesign.co.uk/template/_testing/filter/filter-multi-js.htm
- https://codepen.io/kvana/pen/LLJmZb

## 190419
- docker run -d --mount type=bind,source="$(pwd)"/www,target=/srv -p 2019:2015 abiosoft/caddy
- above command allows for editing the index and viewing changes immediately
- json is loaded into javascript using ajax
- images and titles are displayed from the json file
- the code is very messy....
- need to find a cleaner approach and tag the images with their color values
- the javascript to select images based on color tag info can be done later

## 190418
- after reading about a bunch of frontend frameworks and software, a basic javascript, css, html page should suffice but i'm not sure
- considered MEAN, react, bootstrap. they all seem like overkill for a single dynamic page that pulls info from a json
- setup the docker for Caddy webhosting
- docker run -d -v $(pwd)/www:/srv -p 2019:2015 abiosoft/caddy
- the defaults ports 80 and 2015 don't work with docker -p 2015:2015 but changing to above command works
- need to update github and start working on the html css javascript
- https://www.w3schools.com/howto/howto_js_portfolio_filter.asp
- https://github.com/abiosoft/caddy-docker/blob/master/Dockerfile

## 190416
- color filtering for images is much more comlicated than assumed
- best approach seems to be k-means clustering similar to this: http://charlesleifer.com/blog/using-python-and-k-means-to-find-the-dominant-colors-in-images/
- my approach for simplicity sake is using HSL color values and counting each pixel
- the website filter can then select between about a dozen colors and the 'strength' of the color
- HSL color filter example: https://stackoverflow.com/questions/25943927/search-images-by-color-in-python
- success!!! python script for scanning the image and saving color values to the json file

## 190410
- switches from scrapy image downloader to file downloader. files are now downloading
- some of the links need to be repaired. only full https image links are downloaded but reddit links don't always include domain

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

