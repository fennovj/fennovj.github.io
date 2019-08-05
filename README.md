# fenno.dev

Code for personal website. This is still very much a work in progress for now.

Hosted on [fenno.dev](fenno.dev) with github pages.

I am not planning on adding 'advanced' features like search or tags for articles, because I am not expecting anyone to read this website anyway. 

The goals of this website are as follows:

* Get experience with a personal hobby project, which I haven't done in a while. If I enjoy a hobby project I might do more in the future. A website is a natural choice because it can be used to describe future hobby projects (if any)!
* If I have time and enjoy writing it, act as sort of a 'professional diary' that I can store programming lessons for my future self. Also for stuff that is interesting to write a little about, but too basic to share with colleagues.

## Instructions

This website (will eventually) consist of three parts:

* A custom index.html
* A custom about.html
* A generic template for articles

Other than index.html and about.html (which are in the root directory), all other static content is located in the 'html', 'js' and 'css' directories.

The third part is important since it means I can write my articles in markdown instead of html (which is basically what markdown was created for, jay!).

All the stuff to do the third part is in the 'scripts' folder. This folder therefore does not need to be served on the website - but still is because github pages does not allow excluding directories. I run the file 'commit.py' as a precommit hook - this file renders all the markdown files in the 'markdown' folder, adds them to the 'template.html', and puts the result in the 'html' folder.