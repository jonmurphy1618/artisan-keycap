<!---
Reference:
https://www.openproject.org/
https://www.projectmanagementdocs.com/
--->

# Artisan Keycap Website
## Scope
The subreddit /r/aritsanmacro (2.5k users) exists for user to share photos of their artisan keycaps. Artisan keycaps are keyboard keys made similar to art sculptures, to add flair for a users custom keyboard (see /r/MechanicalKeyboards with 350k users). The problem is that custom keyboards typically have a color theme but there isn't a color sorting option when searching for artisan keycaps. 

The goal of this project is to create a website with color sorting options to browse artisan keycap photos. The site will scrape images linked by the /r/artisanmacro subreddit, process the image colors, and save the color tags with associated links. The website will have a UI to select color sorting options and display a continuously scrollable page of photos.

The second goal is to use this project as part of my protfolio which will require additional documentation on the planning, design, and execution of the project. The additional documentation will also need to be provided with website hosting.

This project does not include programming a web scraper, image processing, or a tagging storage system which are all assumed to be existing open source tools. The webhosting will be selfhosted on existing hardware or a self managed cloud server.

## Schedule
The high level milestone schedule is:
- 190301 - WBS & planning complete. Ready to start building!
- 191308 - Web scrapper downloads daily reddit post links to a database
- Delay due to vacation 190313 - 190327
- 190329 - Images are processed for colors
- 190405 - Image color tags are saved to the database in relation to the image link
- 190412 - Dynamic website created with color sorting UI

## Budget
The budget for the project is $0. It is to be funded through the FYxx My Empty Wallet Foundation. If the assumed existing software is open source, the only costs would be website hosting. My existing home server is capable of webhosting. Alternatively, Digital Ocean (cloud server services) has $100 credit for 6 months which would be able to host the webserver.

## WBS
The Work Breakdown Structure presented here represents all the work required to complete this project.

#### Outline View
<!--- follow the 8-80 rule for breaking out each task --->
	1. Web scrapper
		1.1 Setup docker enviroment on dev server
		1.1 Install python and pip package scrapy
		1.2 Save and setup git repo
		1.3 Filter subreddit posts for the day and save each posts link
		1.4 Find the image link in the post and save the link
		1.5 Download the image linked
	2. Database
		2.1 Setup docker compose yaml
		2.2 MySQL (assumed for now)
		2.3 Test data persistance through docker rebuild
		2.4 Save web scrape data to database
	3. Image Processing
		3.1 setup Python, from PIL import Image
		3.2 Limit to 16-Bit Color
		3.3 Loop over the histogram and average the pixel color by pixel count
		3.4 Save color data to database
		3.4 Save thumbnail to database
	4. Website
		4.1 Setup foundation including DNS, firewall, reverse proxy, LAMP
		4.2 Simple UI design for color selection (slider, color wheel, checkbox, ect)
		4.3 Change background color to color selected
		4.4 Color selection at top of page
		4.5 Page is 1-6 columns of pictures that load as the page is scrolled


## Contacts
Project team directory for all communications is:

|Name	|Title	|Email	|Other	|
|---|---|---|---|
|Jon Murphy	|Project Owner	|me@jonmurphy.info	|git: jonmurphy1618	|


## Quality
The quality standards that will be followed:
- [Python PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/)
- [MySQL Style Guide](https://www.sqlstyle.guide/)
- [Docker Guide](https://docs.docker.com/get-started/)

The quality metrics the project will need to meet:
- Hourly subreddit scrapping for new posts
- Minimum maintence requirements. No manual cache cleaning, docker building, or webscrapping.
- Less than 3 second website load time
- Color filtering done without website reloading and within 3 seconds

## Risks
All risks, their causes, and the impacts.

- Webserver cannot handle DDOS or heavy traffic because it's selfhosted and could require a server restart.
- Image background will affect color tags. Image processing could focus on center of image and ignore edges.
- Web scrapper will pull each image with no regard for content. The scrapper could be time delayed to allow for subreddit admin to monitor content. Also, downvoted posts could be ignored.
- Images will be links which could have 404 issues. The thumbnail will be available without a highres version.
- Website is dynamic and stack is currenly unknown. This will delay the website development stage.
- Color blind options are not currently included. Text or sybmols could be included for filters.
- Schedule conflict with homelab server upgrade to UnRaid. Unable to use homelab for webhost or development. 
