# Windows instructions are here: https://docs.aws.amazon.com/cli/latest/userguide/install-windows.html

# assuming you're using Linux/Mac & have an AWS account already set up

# create your aws account:
# https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/
# add installation of indigo - https://lifescience.opensource.epam.com/indigo/

# install xcode
xcode-select --install

# install homebrew
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

# install python3
brew install python3

# install pip3
curl -O https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py --user

# install aws cli
pip3 install awscli --upgrade --user

# add aws cli to your path so you can just type 'aws' instead of the whole folder path to the command 
export PATH=$PATH:$(which aws | sed 's/\/aws//g')

# now you can run aws cli commands to activate a server using AWS that you can train your model on

# set your ip address in this variable to create a security group to attach to your server that only lets you (or someone who's hacked your laptop) in from your current ip
myipaddr=$(curl http://checkip.amazonaws.com)
mykeyname="ml-train-key"
mystackname="MyModelStack"

# aws command to generate key pair
aws ec2 create-key-pair --key-name $mykeyname

# aws command to upload key pair
chmod_command=$("chmod 600 ${mykeyname}.pem")
# aws command to create stack from cft
cft_contents=$(replace_key_ip.py $myipaddr $mykeyname)

create_stack_output_ip=$(aws cloudformation create-stack --stack-name ${mystackname} ${cft_contents})

echo "public ip of server: ${create_stack_output_ip}"

# ssh command to clone your repo & start training model
keypath=$("${mykeyname}.pem")
ssh_command=$("ssh -i ${keypath} ec2-user@${create_stack_output_ip}")

# type yes, then commands:
source activate tensorflow_p36

# check that git, python3, & pip3 are installed & callable
git clone https://github.com/outdreamer/build-a-cure.git && cd build-a-cure

# assuming you have your libraries listed in a file in your project root called requirements.txt
pip3 install -r requirements.txt

#python3 pull_data.py
#nohup python3 train.py >train.log 2>&1 < /dev/null &