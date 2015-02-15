Date: 5-12-2012 
Title: Upstart With NodeJS And NVM
Slug: NodeJS-Under-NVM-With-Upstart
Author: Barry Steyn
Tags: System Administration

Yet another very short blog article to help anyone who wants to setup an upstart process that runs a [NodeJS](http://nodejs.org/) app under [nvm](https://github.com/creationix/nvm). Unlike the [uwsgi setup](http://doctrina.org/VirtualEnv-With-Upstart.html), there is no specific argument switch to give Node that will make it use nvm environment variables. In fact, since Node is single threaded, there is no special server process that must run in the background to interact with it (unlike [uwsgi](http://projects.unbit.it/uwsgi/) that is needed for Python). This means that whatever executes Node must also introduce the environment variables manually. But doesn't that defeat the purpose of [nvm](https://github.com/creationix/nvm)? Yes, it does! So lets just use [nvm](https://github.com/creationix/nvm) to *manually introduce those environment variables*.

In order to run a [Node](http://nodejs.org/) server in upstart that is under nvm, two things need to be determined:

1. The folder where the node app is defined. Not only is this the path where node will execute your app, but node will also search a folder called *node_modules* under this path for *locally installed libraries*
2. The folder where you have installed your `nvm.sh` script.

**NOTE**: For what follows, the assumption is that the version of node that will be used for execution is the [default version of nvm](https://github.com/creationix/nvm#usage). This accomplished by using `alias` with nvm to set `default` (see previous link).

# An Upstart Example
Lets assume the following:

* Your app is defined in the path `"/home/dev/node-script"`
* The *nvm.sh* script is installed in `"/home/dev/nvm/nvm.sh"`

Then an upstart script to start node that will run this script under nvm is as follows:
<script src="https://gist.github.com/4467515.js"></script>

The above upstart script is very basic, so you should customize it to suit your needs. Yet it has the essential ingredients. The important bit is the *exec* command on line 11, which starts a bash shell script with the argument `-c`. This argument means that any text afterwards will be executed as a command script. The command script passed does two things that are separated by `&&` (the logical and operator):

1. `source /home/dev/nvm/nvm.sh` - this will execute the `nvm.sh` shell script that loads/creates all relevant environment variables. By using the [source](http://ss64.com/bash/period.html) command, all these variables are put within the current shell that it is running in.
2. `exec node app` - it is essential that we use [exec](http://ss64.com/bash/exec.html) to execute the node app. This will replace the current shell with `node app` *without creating a new process*.

The result of the above two commands is that the node app is executed within its own process but which has access to all environment variables that results from running the nvm shell script.
