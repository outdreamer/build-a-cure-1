'''
cft_contents=$(cat neural_net_ec2.yaml)
replace_key_command="echo $cft_contents | sed s/keyname/${mykeyname}/g"
replace_ip_command="echo $replace_key_command | sed s/ipaddr/${myipaddr}/g"
replaced_contents=$($cft_contents | $replace_key_command | $replace_ip_command)
'''
import sys

args = sys.argv
print('args', args)

iparg = '0.0.0.0'
keyarg = ''

for arg in args:
	if '.' in arg:
		iparg = arg 
	else:
		keyarg = arg 

print('found args', 'iparg', iparg, 'keyarg', keyarg)

newlines = []
with open('neural_net_ec2.yaml', 'r') as f:
	for line in f:
		if 'keyname' in line:
			newline = line.replace('keyname', keyarg)
			newlines.append(newline)
		elif 'myipaddr' in line:
			newline = line.replace('myipaddr', iparg)
			newlines.append(newline)
		else:
			newlines.append(line)

newstring = ''.join(newlines)
print(newstring)
