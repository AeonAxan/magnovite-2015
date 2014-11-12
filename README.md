magnovite-2015
==============

Magnovite 2015 - CUFE

Setup and running
=================
Clone the repo and cd to the folder

    $ git clone https://github.com/AeonAxan/magnovite-2015
    $ cd magnovite-2015

Install and setup Vagrant and VirtualBox. This may take sometime depending
on your internet speed

    $ vagrant up
    
    $ vagrant ssh
    $ runserver

Now the website should be available on `localhost:8000`

Development
============

When developing css, run the gulp watch process which will
automatically compile the .less files into the needed .css file
to be included. This will run everytime you save a .less file

    $ gulp watch

or you can run the `css` gulp task manually

    $ gulp css

Contributing
=============

Please work in your own branch, and send a pull request with your branch rebased onto the latest updated version
of master. This will make sure all potential conflicts are resolved. 

    git pull upstream master
    git checkout my-feature
    git rebase master
    
    # fix conflicts if any, and send a pull request
