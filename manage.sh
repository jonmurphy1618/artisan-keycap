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
	# processes the scraped information and applies the color tags to each item
		# input file: ./output/test.json
		# output: updated ./output/test.json
	colorscan)
		python3 colorscan.py
		echo "./output/test.json was updated"
		;;
	webhost)
		docker run -d --mount type=bind,source="$(pwd)"/webhost/www,target=/srv -p 2019:2015 abiosoft/caddy
		echo "website is live" #list ip and port
		;;
	*)
		error_report
		exit 1
esac


# reference: https://nrempel.com/guides/docker-development-environment/
