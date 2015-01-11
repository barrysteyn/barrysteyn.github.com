Date: 29-11-2012 
Title: Upstart With Python VirtualEnv
Slug: VirtualEnv-With-Upstart
Author: Barry Steyn
Category: Blog
Tags: System Administration

I thought I would write this very short blog article to help anyone who would who wants to launch a [uwsgi](http://projects.unbit.it/uwsgi/) server that refers to a python script in a virtual environment via upstart.

In order to run a [uwsgi](http://projects.unbit.it/uwsgi/) server that runs a python script that in [virtualenv](http://pypi.python.org/pypi/virtualenv), the following switches must be defined:

1. **pythonpath** - this should be set to the folder where your script lives. Uwsgi uses this switch to define the [PYTHONPATH](http://docs.python.org/2/using/cmdline.html#envvar-PYTHONPATH) environment variable for the script to be executed.
2. **virtualenv** - this must be set the folder where your virtual environment is defined. It is normally `~/.virtualenvs/<name of virtual environment>`. Uwsgi uses this switch to define the [PYTHONHOME](http://docs.python.org/2/using/cmdline.html#envvar-PYTHONHOME) environment variable for the script to be executed.
3. **file** - this is the file that will be run by uwsgi

# An Upstart Example
Lets assume the following:

1. **pythonpath** = "/home/dev/python-script"
2. **virutalenv** = "/home/dev/.virtualenvs/python-script"
3. **file** = "/home/dev/python-script/script.py"

Then an upstart script to start uwsgi that will run this script in the virutalenv is as follows:
<script src="https://gist.github.com/4469288.js"></script>

There are many options that one can give uwsgi. The above example is running a flask app, and therefore uses the `--callable` switch (although your particular needs should be defined by the documentation).
