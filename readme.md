# Artisan Keycap Website
This is a website hosting artisan keycap images that can be filtered by color. The web scraper pulls data from the subreddit /r/artisanmacro, processes the images for colors, and applies tags for filtering.

![GIF showing the website in action!]()


## Installation
Debian 9 (stretch):
Install docker, this method is not recommended for production.
```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh
```
Clone this repository using git.
```bash
apt-get install git
git clone https://github.com/jonmurphy1618/artisan.git
cd artisan
```

## Usage
The following command will launch the scraper and host as a docker background process.  
`./manage.sh update`  
The update command will scrape posts from urls provided in `artisan/artisan/spiders/app.py` 
and save the output data to `artisan/output/test.json` & images to `artisan/output/full/`.  

After the webscape is done. The `colorscan.py` script is called which processed the images for colorvalues
and appends the data to `test.json`.  

`./manage.sh webhost`  
The webhost command activates a Caddy local webhost on port 2019.

## Dependencies
- Docker
- PyPy
- Scrapy
- PIL
- Caddy

## License
This project is licensed under the MIT License. All dependencies are forms of open-source licensing.
- Docker is Apache 2.0 [link][1]
- PyPy is MIT [link][2]
- Scrapy is BSD-3-Clause [link][3]
- PIL is MIT-like [link][4]
- Caddy is Apache [link][5]

[1]:https://github.com/moby/moby/blob/master/LICENSE
[2]:https://bitbucket.org/pypy/pypy/src/default/LICENSE
[3]:https://github.com/scrapy/scrapy/blob/master/LICENSE
[4]:http://www.pythonware.com/products/pil/license.htm
[5]:https://github.com/caddyserver/caddy/blob/master/LICENSE.txt
