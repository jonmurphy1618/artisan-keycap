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
	*)
		error_report
		exit 1
esac


# reference: https://nrempel.com/guides/docker-development-environment/
