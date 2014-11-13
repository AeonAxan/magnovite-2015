# This file is run as the vagrant user to setup the project

PROJECT_NAME=magnovite
PROJECT_HOME=/home/vagrant/magnovite

cd $PROJECT_HOME

# virtualenv settings
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
export WORKON_HOME=/home/vagrant/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh

echo "=======Creating virtualenv $PROJET_NAME"
mkvirtualenv -p /usr/bin/python3 $PROJECT_NAME
workon $PROJECT_NAME

echo "=======Removing node_modules folder"
rm -rf node_modules

# setup project dependencies
echo "=======Pip installing python dependencies"
pip install -r requirements/dev.txt

echo "=======Npm installing Node dependencies"
npm install

# Update bashrc
echo "=======Updating bashrc"
cat <<EOF >> ~/.bashrc
workon magnovite
cd /home/vagrant/magnovite/
alias runserver="python manage.py runserver 0.0.0.0:8000"
echo -e "\n================\n$ runserver - runs the python server"
echo -e "================\n"
EOF
