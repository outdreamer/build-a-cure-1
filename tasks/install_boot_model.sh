# install pip, python 

# ubuntu
apt install python3-pip	

# centos
yum install epel-release 
yum install python3-pip


pip3 install -r model_requirements.txt

# install xgboost
cd ~/ && git clone --recursive https://github.com/dmlc/xgboost.git && cd xgboost
make
cd python-package && python3 setup.py install --user

# pull data
cd ~/ && git clone https://github.com/outdreamer/build-a-cure.git