#!/bin/bash

usage() {
	cat << EndOfUsage
Run or deploy willcarh.art

Usage:
  ./run.sh MODE

Required arguments:
  MODE - the run mode, can be one of {local, dev, or prod}
         'local' will run the app locally
         'dev' will publish the app to the staging space: https://willcarhart-dev.herokuapp.com/
         'prod' will publish the app to production: http://willcarh.art
EndOfUsage
}

if [[ $# -eq 0 ]] ; then
	MODE="local"
else
	MODE="$1"
fi

MODE=`echo "$MODE" | tr '[:upper:]' '[:lower:]'`
case $MODE in
	local)
		echo "Running willcarh.art locally..."
		python manage.py runserver
		;;
	dev)
		echo "Deploying willcarh.art to dev staging space: https://willcarhart-dev.herokuapp.com/"
		git push heroku-willcarhart-dev `git branch | grep \* | cut -d ' ' -f2`
		;;
	prod)
		read -p "Are you *absolutely* sure you want to push to production? " CONFIRM
		if [[ $CONFIRM == [yY] || $CONFIRM == [yY][eE][sS] ]] ; then
			echo "Deploying willcarh.art to production: http://willcarh.art"
			git push heroku master
		else
			echo "Did not deploy to production."
		fi
		;;
	*)
		echo "run.sh: err: unknown mode '$MODE'"
		exit 1
		;;
esac
