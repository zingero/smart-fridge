sudo mkdir /etc/smartfridge/
sudo echo "{}" > /etc/smartfridge/configuration.json
sudo mkdir /var/smartfridge/

pip3 install opencv-python

# install google api
pip3 install --upgrade testresources
pip3 install --upgrade setuptools
pip3 install --upgrade google-api-python-client
pip3 install google-auth-oauthlib