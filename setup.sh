# this file is run as the root user

PROJECT_NAME=magnovite
PROJECT_HOME=/home/vagrant/magnovite

cd $PROJECT_HOME

# Install essential packages from Apt
apt-get update -y

# Install libraries we need
echo "=======Installing Base Dependencies"
apt-get install -y sqlite3


# Install libraries we need
echo "=======Installing Python requirements"
apt-get install -y build-essential libpq-dev python3-pip

# install nodejs npm
echo "=======Installing Node requirements"
apt-get install -y nodejs nodejs-legacy npm

# set up virtual environment
echo "=======Settings up Virtualenvironment"
pip3 install virtualenv
pip3 install virtualenvwrapper

# set up virtualenvwrapper
echo "=======Settings up virtualenvwrapper in bashrc"
echo 'export WORKON_HOME=/home/vagrant/.virtualenvs' >> /home/vagrant/.bashrc
echo 'export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3' >> /home/vagrant/.bashrc
echo '. /usr/local/bin/virtualenvwrapper.sh' >> /home/vagrant/.bashrc

# gulp needs to be installed globally
echo "=======Installing gulp globally"
npm install -g gulp
