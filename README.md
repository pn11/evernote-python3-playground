# Evernote Python3 API のおためし

## Usage

!!Caution!! This runs in your Evernote DB, not a sandbox.

### Create new note

```sh
$ cat .env
EVERNOTE_TOKEN="YOUR_TOKEN_HERE"
$ pip3 install -r requirements.txt
$ python3 EDAMTest.py
```

### Search note

```sh
$ cat .env
EVERNOTE_TOKEN="YOUR_TOKEN_HERE"
$ pip3 install -r requirements.txt
$ python3 search_sample.py
```

## Reference

- [evernote/evernote-sdk-python3: Testing the Evernote Cloud API for Python 3](https://github.com/evernote/evernote-sdk-python3)
  - Especially, [evernote-sdk-python3/sample/client](https://github.com/evernote/evernote-sdk-python3/tree/master/sample/client)
- [Search - Evernote Developers](https://dev.evernote.com/doc/articles/search.php)
- [Note Links - Evernote Developers](https://dev.evernote.com/doc/articles/note_links.php)
