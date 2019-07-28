#!/bin/bash

usage() {
	cat << EndOfUsage
Run or deploy willcarh.art

Usage:
  deploy.sh MODE

Required arguments:
  MODE       - the deploy mode, can be one of {local, dev, prod}
               'local' will run the app locally
               'dev' will publish the app to the staging space: https://willcarhart-dev.herokuapp.com/
               'prod' will publish the app to production: http://willcarh.art
               (default: local)

Optional arguments:
  -h, --help - show this help menu and exit

EndOfUsage
}

update_vars() {
	if [[ "$1" != "willcarhart-dev" && "$1" != "willcarhart-prod" ]] ; then
		echo "deploy.sh: warning: no such environment '$1'"
		echo "  Did not update environment variables."
		return 1
	fi
	APP="$1"
	if [[ ! -f willcarhart_admin.lcksmth.gpg ]] ; then
		echo "deploy.sh: warning: no such file willcarhart_admin.lcksmth.gpg"
		echo "  Did not update environment variables."
		return 1
	fi
	VARS=( `gpg -d willcarhart_admin.lcksmth.gpg` )
	if [[ $? -ne 0 ]] ; then
		echo "deploy.sh: warning: incorrect credentials for locksmith file"
		echo "  Did not update environment variables."
		return 1
	fi
	for VAR in "${VARS[@]}" ; do
		heroku config:set --app "$APP" "$VAR"
	done
}

if [[ "$1" == "-h" || "$1" == "--help" ]] ; then
	usage
	exit 0
fi

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
	dev|devo|development)
		echo "Deploying willcarh.art to dev staging space: https://willcarhart-dev.herokuapp.com/"
		update_vars willcarhart-dev
		heroku run --app willcarhart-dev python manage.py migrate
		heroku run --app willcarhart-dev python maid.py -u
		git push heroku-willcarhart-dev `git branch | grep \* | cut -d ' ' -f2`
		echo
		echo "Deploy attempt complete [dev]"
		echo "Heroku statistics:"
		heroku ps --app willcarhart-dev
		;;
	prod|production)
		read -p "Are you *absolutely* sure you want to push to production? " CONFIRM
		if [[ $CONFIRM == [yY] || $CONFIRM == [yY][eE][sS] ]] ; then
			echo "Deploying willcarh.art to production: http://willcarh.art"
			update_vars willcarhart-prod
			heroku run --app willcarhart-prod python manage.py migrate
			heroku run --app willcarhart-prod python maid.py -u
			git push heroku master
			echo
			echo "Deploy attempt complete [prod]"
			echo "Heroku statistics:"
			heroku ps --app willcarhart-prod
		else
			echo "Did not deploy to production."
		fi
		;;
	*)
		echo "deploy.sh: err: unknown mode '$MODE'"
		exit 1
		;;
esac
