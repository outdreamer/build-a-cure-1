# install pip, python 

# ubuntu
apt install python3-pip	

# centos
yum install epel-release 
yum install python3-pip

# install xgboost
cd ~/ && git clone --recursive https://github.com/dmlc/xgboost.git && cd xgboost
# cp make/minimum.mk ./config.mk
make # make -j4
cd python-package && python3 setup.py install --user

# pull data
cd ~/ && git clone https://github.com/outdreamer/build-a-cure.git && cd ./build_a_cure

pip3 install -r tasks/model_requirements.txt
