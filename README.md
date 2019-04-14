# willcarh.art
Full-stack web application for my portfolio! Will eventually be deployed to [willcarh.art]()...

Track development progress here: https://trello.com/b/glDTHpCJ/willcarhart

## Utilities
The following are custom utilities I've written in Python to facilitate the microservices of willcarh.art.

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
```bash
# send an email with the subject "News Flash!" to "you@email.com" describing the news
$ python3 herald.py -s "News Flash!" -t "you@email.com" "willcarh.art is a sick website!"
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

## Technologies Used
### Front-end
 * HTML5
 * CSS3
 * Bootstrap 4
 * Javascript
### Back-end
 * Python 3.7
 * Django 2.1.5
### Database
 * PostgreSQL 11.2
