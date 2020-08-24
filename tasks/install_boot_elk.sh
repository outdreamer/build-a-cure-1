# install pip, python 

# ubuntu
apt install python3-pip	

# centos
yum install epel-release 
yum install python3-pip

# pull data
cd ~/ && git clone https://github.com/outdreamer/build-a-cure.git && cd ./build_a_cure
pip3 install -r tasks/elk_requirements.txt

"[elasticsearch]\nname=Elasticsearch repository\nbaseurl=http://packages.elastic.co/elasticsearch/2.x/centos\ngpgcheck=1\ngpgkey=http://packages.elastic.co/GPG-KEY-elasticsearch\nenabled=1" >> /etc/yum.repos.d/elasticsearch.repo
"[logstash]\nname=Logstash\nbaseurl=http://packages.elasticsearch.org/logstash/2.2/centos\ngpgcheck=1\ngpgkey=http://packages.elasticsearch.org/GPG-KEY-elasticsearch\nenabled=1" >> /etc/yum.repos.d/logstash.repo
"[kibana-4.5]\nname=Kibana repository for 4.5.x packages\nbaseurl=http://packages.elastic.co/kibana/4.5/centos\ngpgcheck=1\ngpgkey=http://packages.elastic.co/GPG-KEY-elasticsearch\nenabled=1" >> /etc/yum.repos.d/kibana.repo

yum install elasticsearch -y
yum install logstash -y
yum install kibana -y

systemctl daemon-reload
systemctl start elasticsearch
systemctl enable elasticsearch
systemctl start kibana
systemctl enable kibana

firewall-cmd --permanent --add-port 9200/tcp
firewall-cmd --permanent --add-port 5601/tcp
firewall-cmd --reload

curl -X GET http://localhost:9200

# configure schema/import email data
# sudo curl -XPUT 'http://127.0.0.1:9200/_template/sample' -d@/home/ec2-user/sample.template.json

python - <<'END_SCRIPT'
print("importing to elk stack")
from import_elk import
import_to_elk\nimport_to_elk('fgt_event', data, '/data/event/')
print('finished importing')
END_SCRIPT