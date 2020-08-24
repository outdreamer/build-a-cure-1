# install pip, python 

# centos
yum install java-1.8.0-openjdk-devel git epel-release python3-pip firewalld -y

# pull data
cd /home/ec2-user && git clone https://github.com/outdreamer/build-a-cure.git && cd ./build-a-cure/tasks && pip3 install -r elk_requirements.txt

rpm –import https://artifacts.elastic.co/GPG-KEY-elasticsearch

echo "[elasticsearch]" >> /etc/yum.repos.d/elasticsearch.repo
echo "name=Elasticsearch repository" >> /etc/yum.repos.d/elasticsearch.repo
echo "baseurl=https://artifacts.elastic.co/packages/6.x/yum" >> /etc/yum.repos.d/elasticsearch.repo
echo "gpgcheck=1" >> /etc/yum.repos.d/elasticsearch.repo
echo "gpgkey=http://artifacts.elastic.co/GPG-KEY-elasticsearch" >> /etc/yum.repos.d/elasticsearch.repo
echo "enabled=1" >> /etc/yum.repos.d/elasticsearch.repo
echo "autorefresh=1" >> /etc/yum.repos.d/elasticsearch.repo
echo "type=rpm-md" >> /etc/yum.repos.d/elasticsearch.repo

echo "[logstash]" >> /etc/yum.repos.d/logstash.repo
echo "name=Logstash" >> /etc/yum.repos.d/logstash.repo
echo "baseurl=http://packages.elasticsearch.org/logstash/2.2/centos" >> /etc/yum.repos.d/logstash.repo
echo "gpgcheck=1" >> /etc/yum.repos.d/logstash.repo
echo "gpgkey=http://packages.elasticsearch.org/GPG-KEY-elasticsearch" >> /etc/yum.repos.d/logstash.repo
echo "enabled=1" >> /etc/yum.repos.d/logstash.repo

echo "[kibana-4.5]" >> /etc/yum.repos.d/kibana.repo
echo "name=Kibana repository for 4.5.x packages" >> /etc/yum.repos.d/kibana.repo
echo "baseurl=http://packages.elastic.co/kibana/4.5/centos" >> /etc/yum.repos.d/kibana.repo
echo "gpgcheck=1" >> /etc/yum.repos.d/kibana.repo
echo "gpgkey=http://packages.elastic.co/GPG-KEY-elasticsearch" >> /etc/yum.repos.d/kibana.repo
echo "enabled=1" >> /etc/yum.repos.d/kibana.repo

yum install elasticsearch logstash kibana -y
sudo systemctl enable firewalld
sudo systemctl daemon-reload
sudo systemctl start elasticsearch
sudo systemctl enable elasticsearch
sudo systemctl start kibana
sudo systemctl enable kibana
reboot

firewall-cmd --permanent --add-port 9200/tcp
firewall-cmd --permanent --add-port 5601/tcp
firewall-cmd --reload

python3 test.py

curl -X GET http://localhost:9200
curl -X GET http://localhost:9200/_cat/indices?v
curl -X GET http://localhost:9200/_aliases
curl -X GET http://localhost:9200/fgt_event/_search
# curl -XDELETE http://localhost:9200/fgt_event

# configure schema/import email data
# sudo curl -XPUT 'http://127.0.0.1:9200/_template/sample' -d@/home/ec2-user/sample.template.json