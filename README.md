# This repository is archived.
This is v1 of willcarh.art. It is a monolithic Django application and was a first version of my website. It was a great first attempt, but has become difficult to maintain and support. This repository has been archived for historical purposes. Please refer to the current repository for the latest version of willcarh.art: https://github.com/wcarhart/willcarh.art

# [willcarh.art](https://www.willcarh.art/)

[![willcarh.art demo](static/readme_demo.png)](https://www.willcarh.art/)

Full-stack web application for my portfolio!

Track active development progress and bug fixes here: https://trello.com/b/glDTHpCJ/willcarhart

## Install and deploy
To install or deploy, clone this repo and use the `deploy.sh` script.

To run _locally_:
```
deploy.sh local
```
To deploy to _development_ staging area:
```
deploy.sh dev
```
To deploy to _production_:
```
deploy.sh prod
```
Note that [willcarh.art](https://www.willcarh.art) encrypts its secrets in a GPG file, so you'll have to replicate those values with your own if you'd like to run the app locally.

## Utilities
The following are custom utilities I've written in Python to facilitate the microservices of [willcarh.art](https://www.willcarh.art).

### `Scribe`
The `scribe` writes content to the database from a JSON file. Checkout the code --> [`scribe.py`](https://github.com/wcarhart/willcarh.art/blob/master/scribe.py)

**Usage**:
```bash
# read from default file 'contents.json'
$ python3 scribe.py
# read from custom file 'custom.json'
$ python3 scribe.py -f custom.json
```
### `Herald`
The `herald` sends emails. Checkout the code --> [`herald.py`](https://github.com/wcarhart/willcarh.art/blob/master/herald.py)

**Usage**:
```python
# the herald exposes an easy-to-use API:
from herald import send_message
send_message(
  from_name="Will Carhart", 
  from_email="my_email@mail.com", 
  from_message="Hey! How's it going?"
)
```
### `Locksmith`
The `locksmith` encrypts project secrets so nefarious individuals can't see them when my code's stored in GitHub. Checkout the code --> [`locksmith`](https://github.com/wcarhart/locksmith)

**Usage**:
See linked repository: [`locksmith`](https://github.com/wcarhart/locksmith)
### `Maid`
The `maid` cleans and refreshes the database for updates. Checkout the code --> [`maid.py`](https://github.com/wcarhart/willcarh.art/blob/master/maid.py)

**Usage**:
```bash
# clean the database
$ python3 maid.py
# clean the database and update using Scribe
$ python3 maid.py -u
```
### `Chronicler`
The `chronicler` updates, records, and manages the app's manifest file (which contains version, etc.). Checkout the code --> [`chronicler.py`](https://github.com/wcarhart/willcarh.art/blob/master/chronicler.py)

**Usage**:
```bash
# update manifest.json to reflect changes
$ python3 chronicler.py
# bump major version for app
$ python3 chronicler.py -M
# bump minor version for app
$ python3 chronicler.py -m
```

## Nomenclature Explained
As you may have noticed, the URL for [willcarh.art](https://www.willcarh.art) is rather odd. In order to preserve my full name, Will Carhart, in the URL, I opted to use a .art [top-level domain (TLD)](https://en.wikipedia.org/wiki/Top-level_domain). Since the .art TLD is usually reserved for art portfolios, I thought it was a fitting name for my _coding portfolio._ However, the naming convention doesn't stop there! If you peruse the file structure of [willcarh.art](https://www.willcarh.art), you may notice that the back-end of the app is called the _easel_ while the front end of the app is called the _canvas,_ which I felt fit with the whole "art" vibe of the project 🤗

## Technologies Used
### Front-end
 * HTML5
 * CSS3
 * Bootstrap 4
 * Javascript + jQuery
### Back-end
 * Python 3.6.8
 * Django 2.2.4
### Database
 * PostgreSQL 11.2
### Deployment
 * Heroku 18 (Ubuntu 18)
 * Cloudflare (DNS, SSL)
 * GoDaddy (Registrar)
 * Gmail API
