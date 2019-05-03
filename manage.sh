#!/bin/bash

error_report() {
	echo "
	manage.sh commands are:
	bash	starts docker in bash mode
	edit	opens app.py in nano
	help	displays this message
"
}

trap error_report ERR


case "$1" in
	bash)
		docker run -it --rm --mount type=bind,source="$(pwd)",target=/app artisan bash
		;;
	edit)
		nano ./artisan/spiders/app.py
		;;
	scrape_posts)
		docker build --tag=artisan .
		docker run -it --rm --mount type=bind,source="$(pwd)",target=/app artisan scrapy crawl posts -o ./output/test.json
		echo "posts and images data from website saved to ./output/test.json"
		;;
	colorscan)
		#docker run -it --rm --mount type=bind,source="$(pwd)",target=/app artisan python3 colorscan.py
		python3 colorscan.py
		echo "./output/test.json was updated with color tags and saved to ./webhost/www/test.json"
		;;
	webhost)
		docker run -d --mount type=bind,source="$(pwd)"/webhost/www,target=/srv -p 2019:2015 abiosoft/caddy
		echo "website is live" #list ip and port
		;;
	update)
		./manage.sh scrape_posts
		./manage.sh colorscan
		;;
	*)
		error_report
		exit 1
esac


# reference: https://nrempel.com/guides/docker-development-environment/
