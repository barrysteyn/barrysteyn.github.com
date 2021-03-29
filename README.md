#Doctrina - personal website of Barry Steyn

## Requirments:

### Python

`pip install pelican markfown inflect beautifulsoup4 html5lib ghp-import`

## Checking The Theme Submodule Out
The repo has a submodule that also needs to be cloned:

 1. Clone the repo as per usual
 2. Initialize submodule: `git submodule init`
 3. Update the submodule: `git submodule update`

To get the latest version of the submodule: `git submodule update --remote`

## Plugins
The site needs the following repos checked out and available in `../`:

 1. pelican-plugins: https://github.com/getpelican/pelican-plugins
 2. links-to-print: git@github.com:barrysteyn/links_in_print.git

## Developing
Make sure that `/etc/hosts` has an entry for *doctrina* like so:

```
127.0.0.1 	doctrina
```

Then go to *http://doctrina:8000* and write away.
