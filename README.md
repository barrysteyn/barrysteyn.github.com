#Doctrina - personal website of Barry Steyn

## Requirments:

First do this:

```
git config user.name "Barry Steyn"
git config user.email "barry.steyn@gmail.com"
```

### Python

`pip install -r requirements.txt`

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

 1. Make sure that `/etc/hosts` has an entry for *doctrina* like so:

```
"127.0.0.1 	doctrina"
```
 2. Build the theme: `make theme`
 3. Start serving: `pelican --autoreload --listen  --output ./output`

Then go to *http://doctrina:8000* and write away.
