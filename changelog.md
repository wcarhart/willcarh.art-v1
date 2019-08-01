# Changelog
This is a history of the development to [willcarh.art](https://www.willcarh.art). Changes can happen in one of the following categories:
 - `FUNCTIONALITY [ADDED, UPDATED, DEPRECATED]`
 - `CONTENT [ADDED, UPDATED, REMOVED]`
 - `DEPLOYMENT`
 - `BUGFIX`

Version numbers follow the format _[major.minor.commit]_. See [`chronicler.py`](https://github.com/wcarhart/willcarh.art/blob/master/chronicler.py) for more details.

## Unreleased
There is currently no unreleased content. Track active development progress [here](https://trello.com/b/glDTHpCJ/willcarhart).

## [0.1.158] 2019-07-31 (PR #11)
### Functionality ADDED
 - introduced the changelog

### Functionality UPDATED
 - improved the Chronicler implementation

### Content UPDATED
 - fixed various typos in blog posts
 - highlighted GitHub links in blog posts

### Bugfix
 - fixed broken links in the `README.md`

## [0.1.155] 2019-07-29 (PR #10)
### Functionality ADDED
 - added alt tags for more images

### Functionality UPDATED
 - updated `notes.txt`

### Content ADDED
 - added third blog post

### Content UPDATED
 - fixed the Herald usage in the `README.md`
 - fixed typo in lurker demo section

### Bugfix
 - fixed media content overflow issue on blog posts

## [0.1.130] 2019-07-29 (PR #9)
### Functionality UPDATED
 - migrated the Herald to the official Gmail API
 - moved large visual media to third party hosting solution
 - updated `requirements.txt`

### Functionality DEPRECATED
 - removed admin features on publicly deployed willcarh.art

### Content ADDED
 - added project information for aerogram

### Content UPDATED
 - rearranged order of projects

### Deployment
 - removed extraneous password config
 - upgraded Heroku dyno
 - switched nameservers from GoDaddy to Cloudflare
 - implemented SSL
 - improved metrics from Heroku, Cloudflare

### Bugfix
 - fixed incorrect animations on Skills section
 - fixed missing project bug resulting in 500 error (now is 404)
 - fixed missing blog bug resulting in 500 error (now is 404)

## [0.1.0] 2019-07-28 (PR #6)
### Functionality ADDED
 - added `notes.txt` for miscellaneous dev notes about willcarh.art

### Functionality UPDATED
 - updated virtual environment implementation
 - updated static files management with git

### Functionality DEPRECATED
 - removed dynamic content loading from demo section on Cheers project page

### Content ADDED
 - added project information for lurker

### Content UPDATED
 - updated `README.md` with deploy instructions
 - added _magna cum laude_ to About section
 - updated Skills section
 - updated Konphig demo section

### Deployment
 - automated deployment process
 - improved security of allowed hosts
 - updated various security settings

### Bugfix
 - fixed debug setting for production
 - fixed default Django 404, 500 errors, replaced with custom

## [0.0.82] 2019-04-15 (PR #4)
### Functionality ADDED
 - styling for attention, note, etc. style boxes in blog posts
 - styling for demo section of each project page

### Content ADDED
 - demo content for each project
 - visual media for project demos

### Deployment
 - first deploy to Heroku

## [0.0.55] 2019-04-14 (PR ##)
### Functionality ADDED
 - prototype of fullstack Blog app
 - noscript tag on home page
 - prototype of the Maid
 - prototype of the Chronicler
 - introduction of `manifest.json`
 - introduction of `content.json`

### Content ADDED
 - descriptions for each project

### Content UPDATED
 - updated About, Experience sections on home page

## [0.0.0] <2019-04-11 (PR #2)
### Functionality ADDED
 - basic implementation of `index.html` for home page
 - basic implementation of CSS styling for site
 - basic implementations of JS scripts for animations
 - prototype backend
   - Home app
   - Projects app
 - some integration with basic frontend
 - prototype of the Herald
 - prototype of the Scribe
 - integration with the Locksmith

### Content ADDED
 - first draft of home page
 - icons for whole site
