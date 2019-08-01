# Contributing
[willcarh.art](https://www.willcarh.art) is not an open source project, as it is not licensed with an open source license. This is a document for my own benefit for how to update and add to [willcarh.art](https://www.willcarh.art).

If you've found a bug or would like to request a new feature, please do open [a new issue](https://github.com/wcarhart/willcarh.art/issues/new) 😊

## Contribution Workflow
1. Create a story in the backlog on [Trello](https://trello.com/b/glDTHpCJ/willcarhart) that describes the new feature, content update, or bugfix.
2. Create a new feature or bugfix GIT branch.
3. Implement the code, content, or infrastructure updates.
4. Test the changes _locally_ by running:
```
$ ./deploy.sh local
```
5. If any tests fail _locally_, return to **Step 3**.
6. Commit working code to the feature or bugfix branch.
7. Test the changes in the _dev_ environment. Push to the _dev_ environment by running:
``` 
$ ./deploy.sh dev
```
8. If any tests fail in the _dev_ environment, return to **Step 3**.
9. Bump the appropriate version with the Chronicler by running:
```bash
$ python chronicler.py
# or
$ python chronicler.py -m
# or
$ python chronicerl.py -M
```
10. Update `changelog.md` with the appropriate changes. Make sure to use the proper format.
11. Open a Pull Request with your changes.
12. Review **every** file in the open Pull Request. Look for bugs and [smelly code](https://blog.codinghorror.com/code-smells/).
13. Merge the Pull Request into _master_.
14. On your local machine, update to master by running:
```
$ git checkout master
$ git pull
```
15. Deploy to _prod_.
```
$ ./deploy prod
Are you *absolutely* sure you want to push to production? yes
```
16. Test the changes in _prod_. If any tests fail, return to **Step 1**.
