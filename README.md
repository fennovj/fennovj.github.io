# fenno.dev

Code for personal website. This is still very much a work in progress for now.

Hosted on [fenno.dev](https://fenno.dev) with github pages.

I am not planning on adding 'advanced' features like search or tags for articles, because I am not expecting anyone to read this website anyway. 

The goals of this website are as follows:

* Get experience with making a website as a personal hobby project. A website is a natural choice for a hobby project because it can be used to write about future hobby projects (if any)!
* If I have time and enjoy writing it, act as sort of a 'professional diary' that I can store programming lessons for my future self. Also for stuff that is interesting to write a little about, but too basic to share with colleagues.

## Instructions

Other than index.html, pages are markdowns that are rendered inside a template html. This can be done by running 'scripts/pre-commit.py'. For convenience sake, this can be done as a pre-commit hook. To install this pre-commit hook, run the command `ln -s -f ../../scripts/pre-commit.sh .git/hooks/pre-commit`. This will automatically render all html with the latest template, and add it to the commit.

Basically, this means the html folder should not be edited manually.
