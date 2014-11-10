PROJECT_NAME=magnovite
PROJECT_HOME=/home/vagrant/magnovite

cd $PROJECT_HOME

# Install essential packages from Apt
apt-get update -y

# Install libraries we need
apt-get install -y build-essential libpq-dev python3-pip

set up virtual environment
pip3 install virtualenv
pip3 install virtualenvwrapper

export WORKON_HOME=/home/vagrant/.virtualenvs

# set up virtualenvwrapper
echo 'export WORKON_HOME=/home/vagrant/.virtualenvs' >> /home/vagrant/.bashrc
echo 'export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3' >> /home/vagrant/.bashrc
echo '. /usr/local/bin/virtualenvwrapper.sh' >> /home/vagrant/.bashrc

export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
export WORKON_HOME=/home/vagrant/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh

mkvirtualenv -p /usr/bin/python3 $PROJECT_NAME
workon $PROJECT_NAME

pip install -r requirements/dev.txt

# edit bashrc so when we ssh we are in the right place
echo 'workon magnovite' >> /home/vagrant/.bashrc
echo 'cd /home/vagrant/magnovite/' >> /home/vagrant/.bashrc
