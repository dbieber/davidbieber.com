+++
title = "Running Firefox in the Cloud"
subtitle = ""

date = 2014-11-08T00:00:00
lastmod = 2014-11-08T00:00:00
draft = false
authors = ["David Bieber"]

tags = ["Automation"]
summary = "Run a headless version of Firefox in the cloud and drive it with Selenium."

[image]
  caption = "Image credit: [**Pixabay**](https://www.pexels.com/photo/animal-art-canine-close-up-459122/)"
  focal_point = ""
+++

I found running Firefox in the cloud difficult, but with enough digging around I was able to get it working. Now I'm able to drive a headless version of Firefox with Selenium using Python. This lets me do things like have my [Scrabble Bot](https://github.com/dbieber/ScrabbleBot) play Words with Friends autonomously on Facebook.

**What am I going to show you how to do?**

I'm going to explain how you can install Firefox and Selenium on a virtual machine in the cloud. I'm going to show this using a Debian instance on [Google Compute Engine](https://cloud.google.com/compute/), but you could also do this using a virtual machine from Amazon EC2.

Before continuing you should create a virtual machine running Debian on Google Compute Engine (GCE). [You can learn how to spin up a VM here](https://cloud.google.com/compute/docs/quickstart). Make sure that you can SSH into your machine.

**Installing Firefox**

We're actually going to install Iceweasel. To the best of my knowledge, the only difference between Iceweasel and Firefox is the branding. To do this, we're going to:

1. Update the sources list that apt-get uses to find packages.
Edit the file `/etc/apt/sources.list` and add the line `deb http://mozilla.debian.net/ wheezy-backports iceweasel-release`.
2. Update apt-get by running the command `sudo apt-get update`.
3. Install Iceweasel by running the command `sudo apt-get install -t wheezy-backports iceweasel`.

I figured this out by searching for "iceweasel sources list", which brought me to [http://mozilla.debian.net/](http://mozilla.debian.net/). If you're looking to install a different version of Iceweasel/Firefox or have a different version of Debian, check there.

**Running Firefox**

We can now run the browser we installed with the command `firefox` or `iceweasel`, but it will shut down because there is no display. To run the browser without a display (that is, to run it "headlessly"), we're going to:

1. Install the display server Xvfb (X virtual framebuffer) with the command `sudo apt-get install xvfb`.
2. Start the display server with the command `sudo Xvfb :10`. Here, :10 is the server number we chose for the virtual display we're creating.
3. Now run `export DISPLAY=:10`.
 
You should now be able to run `firefox` or `iceweasel` successfully.

If you'd like to see what's on your virtual display, [Wikipedia provides an example of how to take a screenshot of your virtual display](http://en.wikipedia.org/wiki/Xvfb#Usage_examples).

**Installing Selenium**

We can now run a headless version of Firefox. Since there's no user interface to click around in, the next logical step is to learn how to drive the browser. For this, we're going to set up Selenium in Python. When dealing with packages in Python, I recommend using pip inside a virtualenv with virtualenvwrapper. There are instructions for setting up these packages below.

Once you have virtualenvwrapper installed and you're safely working in a virtual environment, just issue the command `pip install selenium` to install selenium. If you're not in a virtualenv, you may need to issue the command with sudo.

Try running this Python script to see if it's all working. It should take you to Google Images, search for cute kittens, and then save a screenshot to the file 'adorable.png'.

<script src="https://gist.github.com/dbieber/1c4a7bdca8f9820b3612.js"></script>

**Installing virtualenvwrapper**

As promised above, here is a section about virtualenvwrapper. 

Managing Python packages effectively is difficult, and I can't do the topic justice here. I recommend using virtualenvwrapper to help, and [you can read more about how to do this here](http://virtualenvwrapper.readthedocs.org/en/latest/install.html). For completeness, I'll briefly run through the steps of getting set up with pip, virtualenv, and virtualenvwrapper.

`pip` is Python's package manager. Once you have pip set up, you can run `pip install package-name` to install the package called package-name.

To set up pip, run the following commands:

1. `curl https://bootstrap.pypa.io/get-pip.py > get-pip.py`
2. `sudo python get-pip.py`

`virtualenv` is a tool that let's you have different versions of Python and Python packages for different projects that you work on. Combined with `virtualenvwrapper`, it will help you avoid headaches of keeping track of where your various Python versions live and where they can find their packages on your machine.

To install virtualenv, run the command `sudo pip install virtualenv`.

To install virtualenvwrapper, run the command `sudo pip install virtualenvwrapper`.

Add the following three lines to your .bashrc or another startup script:

`export WORKON_HOME=$HOME/.virtualenvs`

`export PROJECT_HOME=$HOME/Devel`

`source /usr/local/bin/virtualenvwrapper.sh`

You're now ready to go. [Learn more about how to use virtualenvwrapper effectively here](http://virtualenvwrapper.readthedocs.org/en/latest/command_ref.html).

**Last thoughts**

I hope you find this helpful. You can now install Firefox on Google Compute Engine, run it using a virtual display, and drive it using Selenium with Python. If something isn't working, or if something is working really well and has you super excited, I'm happy to talk it through with you. Email's the best way to contact me. Go forth and automate your life!