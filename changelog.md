# Changelog
This is a history of the development to willcarh.art. Changes can happen in one of the following categories:
 - FUNCTIONALITY [ADDED, UPDATED, DEPRECATED]
 - CONTENT [ADDED, UPDATED, REMOVED]
 - BUGFIX
 - DEPLOYMENT

Version numbers follow the format _[major.minor.commit]_. See `chronicler.py` for more details.

## Unreleased

## [0.1.130] 2019-07-29
### Functionality UPDATED
 - migrated the Herald to the official Gmail API
 - moved large visual media to third party hosting solution
 - updated requirements.txt

### Functionality DEPRECATED
 - removed admin features on publicly deployed willcarh.art

### Content ADDED
 - added project information for aerogram

### Content UPDATED
 - rearranged order of projects

### Deployment
 - removed extraneous password config

### Bugfix
 - fixed incorrect animations on Skills section
 - fixed missing project bug resulting in 500 error (now is 404)
 - fixed missing blog bug resulting in 500 error (now is 404)

## [0.1.0] 2019-07-28
### Functionality ADDED
 - added notes.txt for miscellaneous dev notes about willcarh.art

### Functionality UPDATED
 - updated virtual environment implementation
 - updated staticfile management with git

### Functionality DEPRECATED
 - removed dynamic content loaded from Cheers project page

### Content ADDED
 - added project information for lurker

### Content UPDATED
 - added _magna cum laude_ to About section
 - updated Skills section
 - updated Konphig demo section

### Deployment
 - automated deployment process
 - improved security of allowed hosts
 - updated various security settings

### Bugfix
 - fixed debug settings for production
 - fixed default Django 404, 500 errors, replaced with custom

### Content ADDED
 - updated README with deploy instructions

## [0.0.82] 2019-04-15
### Deployment
 - first deploy to Heroku

### Functionality ADDED
 - styling for attention, note, etc. style boxes in blog posts
 - styling for demo section of each project page

### Content ADDED
 - demo content for each project
 - visual media for project demos

## [0.0.55] 2019-04-14
### Functionality ADDED
 - prototype of fullstack Blog app
 - noscript tag on home page
 - prototype of the Maid
 - prototype of the Chronicler
 - introduction of manifest.json
 - introduction of content.json

### Content ADDED
 - descriptions for each project

### Content UPDATED
 - About, Experience sections on home page

## [0.0.0] <2019-04-11
### Functionality ADDED
 - basic implementation of index.html for home page
 - basic implementation of CSS styling for site
 - basic drafts of JS for animations
 - prototype backend
   - Home app
   - Projects app
 - some integration with basic frontend
 - prototype of the Herald
 - prototype of the Scribe
 - integration with Locksmith

### Content ADDED
 - first draft of home page
 - icons for whole site
