Title: Sphinx, Intersphinx, & Submodules for Document Compendium
Date: 2018-07-24 12:30
Modified: 2018-07-24 12:30
Category: Blog
Tags: writing, sphinx, git, submodules, intersphinx
Slug: sphinx-submodules
Authors: Stuart Davis
Status: published

## Read the Docs in the Docs
<!-- PELICAN_BEGIN_SUMMARY -->
I love that in the course of my work I get the opportunity to be exposed to a lot of different initiatives with the chance to make some impact. One of the major efforts being carried on by a select few right now is to codify our standards of execution as well training, references, and best practice documentation amongst a slew of other potential tangents. We've landed pretty solidly on implementing the presentation layer with [Sphinx](http://sphinx-doc.org/), a documentation generator that is already quite prevalent for offering docs alongside a codebase. We started off with a handful of individual repositories with the same installation pattern each covering a sensible category of information. The desire was to bring this all together in one place. There are two cheap ways to do that.  
<!-- PELICAN_END_SUMMARY -->

- Copy all of the documentation directly in a single one and just drop the other repositories.
- Simply create a page that links out to the other repositories wherein the user switches environments from one set to another.

### What we really want

What we really wanted was the ability to maintain stable independent sensible collections of documentation that could be used on their own **AND** to have all of the content centralized in one collection in which the user *does not* change context as they are click around.

### Where the challenge is

The challenge here is that some of these individual documents have links to other documents where those links are currently in the form of full URLs. So how do we maintain links across these docs when they are separate but also within the docs when they are combined?

## Intersphinx

So right now, as mentioned previously, one document reaches another document by fully verbose URLs.

<center>

![Verbose URL Link](http://www.polymathist.me/media/verboseurl.png)

</center>

As a first step we can implement cross reference labels to assist with linking inside of documentation. (Be sure to take a look at the [``:ref:`` role](http://www.sphinx-doc.org/en/stable/markup/inline.html#role-ref) documentation to learn more). In summary you can put a ``:ref:`` role before a heading with a label and then reference that label later on to create a link. So:

	:::ReST
	.. _myFancyLabel:

	Section Header
	==============

Can be referenced later on with:

	:::ReST
	Check out the cool information in :ref:'myFancyLabel' to learn more

Which will show up as a link like

> Check out the cool information in [Section Header](url) to learn more

By applying this methodology internally the connections feel something like this:

<center>

![Mixed Links](http://www.polymathist.me/media/mixedlinks.png)

</center>

Now what's happening under the covers is that Sphinx is putting those references into an ``objects.inv`` file that allows it to resolve the references to the full urls relative to the documentation's root. This is handy. If you can have one set of documentation retrieve that ``objects.inv`` file from another set of documentation then you can leverage the references without knowing the full url. Something like...

<center>

![Intersphinxing](http://www.polymathist.me/media/intersphinx.png)

</center>

This is accomplished by using the intersphinx extension and using the appropriate reference labels. You need to first enable intersphinx in your ``conf.py`` file with:

	:::python
	extensions = [
    	'sphinx.ext.intersphinx'
	]

and then creating the appropriate mapping with something like...

	:::python
	intersphinx_mapping = {'python': ('https://docs.python.org/', None),
                       'document_b': ('http://www.fullurltodocs.com/', None)}

The grand thing with intersphinx is that as long as there is no label naming collision between the local document (the one that folks are viewing) and the remote document (the one you're trying to link to), then simple ``:ref:`` links work just as that should. If there is a risk of collision then you simply make the link a little more verbose with something like...

	:::ReST
	Check out the cool information in :ref:`this document's stuff <document_b:myFancyLabel>` to learn more

This will ensure that Sphinx only grabs the ``myFancyLabel`` anchor in ``document_b``'s documentation regardless of its existence in the local document.

Now if you have a master plan as you are writing your documentation perhaps you (read: I) would go the extra step to create a convention of reference creating to ensure uniqueness within and among documents. It's a little tedious but making a label like ``_docname_page_section`` as opposed to simply ``_section`` will allow you to control your surroundings. This becomes especially true if what you want is:

> maintain stable independent sensible collections of documentation that could be used on their own **AND** to have all of the content centralized in one collection in which the user *does not* change context as they are click around.

Ah yes... I knew we had a plan here.

## Submodules

The answer here is to leverage the submodule capabilities in git. By including a repository as a submodule within a host repository, the host will consider the submodule to be of its own. By pulling and committing updates recursively and in the right order, you can keep the host documentation in sync. The benefit of all of this when it comes to Sphinx is that you would have one master documentation resource with a singular table of contents tree and the user will stay within that single construct. Sort of like this...

<center>
	
![Submodule](http://www.polymathist.me/media/submodule.png)

</center>

Now getting to that point where you have your independent and collective documentation set takes just a little git patience. My patience was initially shored up with a quick read of [an article by Marco Fargetta](http://fmarco76.github.io/git%20and%20related%20services/readthedocs/). I'd recommend you give it a quick read as well. First, be sure that your documents are as current as can be, committed and pushed. Now head into the root of your host repo (local) and run the following to get the child repo inducted:

	:::bash
	$ git submodule add https://github.com/username/repository.git

That should create a folder for the repository and bring in all of the appropriate files. Now you need to head to your index page and add some entries into the TOC tree to the new content. Something simple like:

	:::ReST
	My Documents
	============

	.. toctree::
	:maxdepth: 2
	:caption: Contents:

	pre-existing links
	submodulerepofolder/index

When you ``make html`` for this new construct, the submodule will now be included in your host documentation. And if you've been following along and setting reference anchors and using those as opposed to links, then all of the links between sections of your documentation will be dancing along just nicely.

Now let's have a moment of sober honesty. Mucking around with submodules can be a hassle and becoming fully familiar with the various options of the ``git submodule`` is recommended. To that end, a thorough couple of reads through [this documentation on Submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules) should just begin to produce that familiarity. A couple of specific takeaways for me include:

	:::bash
	$ git clone --recurse-submodules https://github.com/username/repository.git

... which will grab an entire repository along with the submodules **and their contents**. Trust me. It's important.

Additionally...

	:::bash
	$ git submodule update --remote --recursive

... is an important tool to get your local repository updated through all of the submodule layers. Did I say layers? **YES**! In our use case, we have the need for nested submodules and keeping everything organized takes a bit of work but the results are exactly what we needed. It sort of looks something like this:

<center>
	
![Our Use Case](http://www.polymathist.me/media/ourusecase.png)

</center>

## Breathe Out

So yeah. It's been quite a bit to run through both in real life and documenting it here to at least a surface level. I'm sure there are a lot of other options that could have been considered, but this seemed to meet the needs at the moment. Thanks for sticking with me on this ride. I look forward to seeing you on the next.

Regards,  
Stuart