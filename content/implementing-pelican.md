Title: Implementing Pelican
Date: 2018-07-23 16:00
Modified: 2018-07-23 16:00
Category: blog
Tags: writing, website, pelican, git
Slug: implementing-pelican
Authors: Stuart Davis

## Let's roll out!
<!-- PELICAN_BEGIN_SUMMARY -->
I had already mentioned [here](./rebuilding-web-presence.html) that I would write about the process of rolling out this website via [Pelican](https://blog.getpelican.com/) and [github pages](https://pages.github.com/). Instead of trying to recollect how I did it for this website, I am going to go ahead a start cataloging what I do to get one of my other properties up and running. There will definitely be one thing that's a little different based on the folder structure needed within the appropriate repository on github, but I will be sure to highlight that difference and note that it will be useful for others to consider.
<!-- PELICAN_END_SUMMARY -->

## Get Pelican

Well... I suppose that's a couple of stages down the road. First thing to realize is that Pelican is a Python solution and as such you will need a python environment. That's fairly easily accomplished by grabbing the latest distribution from [anaconda](https://www.anaconda.com/download/). You will also need a github account and will need to download and install [git](https://git-scm.com/downloads).

Now here's where I'm going to mess things up quite a bit because it's a part that I'm not really wanting to replicate as I already have my environment installed. But I can summarize a few things that you will readily find at the [Pelican](https://blog.getpelican.com/) reference documentation. But once Python is installed, open up the anaconda prompt and fire off the following command:

```python
pip install pelican
```

Pelican will get you running out of the gate with reStructureText but as I was simply looking for ease of typing I decided that I wanted to opt for Markdown and as such need the following:

```python
pip install Markdown
```

As with almost any python install, It's good to ensure that you have the real latest version which may not actually be what came through pip. So...

```python
pip install --upgrade pelican
```

Now you're pretty much ready to kick start a project. I navigated to an appropriate place to manage my repository for the source files for this project. In some cases you many need to make a folder and then head into it. Regardless, once you're in that base directory kick of the process with:

```python
pelican-quickstart
```

There's a lot to consider with the quickstart. A lot of options you can just accept as default but you absolutely need to pay attention to the deployment options. Many of the items are editable after the fact in the ``pelicanconf.py`` and ``publishconf.py``. Additional considerations evolve around generation and deployment through either Fabric or Make. As such there will be items that are configurable in ``fabfile.py`` or ``Makefile`` respectively. I say all that to say this... please be sure to reference the [Pelican documentation](http://docs.getpelican.com/en/stable/index.html) a lot and many times over. A lot of it didn't sink in the first time through.

## My process

In anaconda I navigated to my project directory then made a file to house my documents

```shell
mkdir /path/to/repo-name
cd /path/to/repo-name
```

In git I navigated to the folder and then initialized a repository

```shell
cd /path/to/repo-name
git init
```

In github I created a repository for these source files to reside in the master branch with the intention that the published information will land in the gh-pages branch. So in my local directory I simply create a ``Readme.md`` file that I will be able to push to the blank repository in github. Then I used the next commands to create a gh-pages branch

```shell
cd /path/to/repo-name
git symbolic-ref HEAD refs/heads/gh-pages
rm .git/index
git clean -fdx
echo "My GitHub Page" > index.html
git add .
git commit -a -m "First pages commit"
git push origin gh-pages
```

This ensures that there is a gh-pages branch to which we will publish our site documents and host the site files.

Now we need to switch back to the master branch and start up pelican

In git bash

```shell
git checkout master
```

In anaconda

```python
pelican-quickstart
```

- create in root ``.``  
if you aren't in the root directory of your repo you can point it where you need it to go.  
- be sure to provide an appropriate url
- the timezone thing got me the first time through. just head to the [List of tz database time zones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) on wikipedia
- I say yes to generating a Fabfile/Makefile as well as site development script
- I only say yes for GitHub Pages  

Now here is where you need to consider something a little different. I am setting up a site that is NOT my username.github.io account. If this is your first ever site you may want to consider just using it, but I already have one and installing a new site so I'm going with ``N`` for the personal page piece. Just keep this in mind.

Now we need to add a couple of things. I want a ``.gitignore`` file that will keep my published info out of my master branch as well as a couple of other files. You can just checkout the [contents of the repo](https://github.com/brokenlyre/Polymathist.me) but for completeness herein this is my file:

```Markdown
# Python-generated Files
__pycache__/
.ipynb_checkpoints/

# Pelican output
output/
```

Because of my prior experience, in my content directory, I am going to add a few folders:

- **extra**  
This will house my ``CNAME`` and ``favicon.ico`` file
- **media**  
All of the images that I might use on the site
- **pages**  
This is meant by pelican to store static pages that can be referenced as opposed to the blog
- **drafts**  
This is just a place I store content that I'm not ready to publish but that I want included in my repository for safekeeping

As far as file creation, the most important one that I want to deal with right away is the CNAME file. I am going to have my domain registrar point to this repo so I definitely want to be sure this file represents the expectations. It's pretty simple and you just need to change it for your needs:

```Markdown
www.site-name.com
site-name.com
```

To round things out and get a feel for the site when it's live, I just create a markdown file in the content folder so that the site generator has something to push. By-the-by, if you are using sublime, you can make great use of snippets to get a head start on the meta information required for the posts. Feel free to take a look at my [New Meta Post Snippet Gist](https://gist.github.com/brokenlyre/ee91a3947fec759e4902808f7f811614) if you care for a head start.

## Combing the ``*conf.py`` files

- To get to the right place I simply copied most of my settings using the bootstrap 3 theme. I'm sure I will be taking the time at some point to change this, but it's a quick way to get things up and running.
- In the makefile I made sure to put in a line for the right repository for the github pages account 
```Makefile
GITHUB_PAGES_REMOTE=git@github.com:username/username.github.io.git
```
- I also make sure that the branch is set to gh-pages  
```Makefile
GITHUB_PAGES_BRANCH=gh-pages
```

## Run ``make html`` and ``make gituhub``

Run ``make html`` and take a gander at the output. To really check things out right, spin up a local server by running ``make serve`` and then opening a browser to ``localhost``. You should be able to have a pretty solid experience before pushing this all into production.

It's time to get that site into the repository. If everything is set up correctly then once you run ``make github`` all of your ``.html`` files will find their way into the ``gh-pages`` branch of your repo. With that and the fact that you have an appropriate ``CNAME`` file, you should be able to check the settings of the repo and notice that it's already picked up the custom domain for your use. Now you just need to be sure that the registrar has some updated settings.

## Updating the Registrar
I use google domains - but in essence every domain registrar should have something similar when it comes to setting up the DNS.  You need and apex entry (or two depending how things are set up) and a www entry.

| NAME | TYPE | TTL | DATA |
| ---- | ---- | --- | ---- |
| @    | A    | 1h  | 192.30.252.153 |
|      |      |     | 192.30.252.154 |
| www  | CNAME | 1h | username.github.io |


Even if this is a project site, just put in the ``username.github.io`` version and don't attempt to add a directory in line. You can then head to your website url and see how fast the dns updates. In my case the updates took a couple of hours. So don't sweat it if the site doesn't load right away.

## And..... go

Hopefully this gets you to a good spot with setting up a static site. I'm sure I've missed a thing here and there. Feel free to offer a correction on my [issues page](https://github.com/brokenlyre/Polymathist.me/issues) if you do see anything grossly out of order.

Regards,  
Stuart



