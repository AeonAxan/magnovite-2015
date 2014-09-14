magnovite-2015
==============

Magnovite 2015 - CUFE

Setup and running
=================
Clone the repo and cd to the folder

    git clone https://github.com/AeonAxan/magnovite-2015
    cd magnovite-2015

Install python3 and use pip3, if your default pip is pip3 use `pip`. (Note: You might want to do this in a virtualenv)
**If you're pip defaults to python2 pip you should use `pip3` instead**
  
    pip install -r requirements/dev.txt
    
If you get an error about postgres look [here](http://stackoverflow.com/questions/5420789/how-to-install-psycopg2-with-pip-on-python)
    
Run a development server.
**If you're default python is python2 instead run `python3 manage.py runserver`**
    
    ./manage.py runserver
    

Contributing
=============

Please work in your own branch, and send a pull request with your branch rebased onto the latest updated version
of master. This will make sure all potential conflicts are resolved. 

    git pull upstream master
    git checkout my-feature
    git rebase master
    
    # fix conflicts if any, and send a pull request
