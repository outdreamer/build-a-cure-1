variable "keypath" {
  description = "Path to SSH private key to SSH-connect to instances"
  default = "/Users/jjezewski/tf_deploy.pem"
}
resource "aws_instance" "task_ec2_instance" {"
  ami		   = "ami-024d1b90da07e64a6"
  region		   = "us-west-2"
  instance_type = "t2.micro"
  key_name	  = "${aws_key_pair.task_key_pair.key_name}"
  user_data	 = "${file(install_boot_elk.sh)}"
  tags = {
	   Name  = "task_ec2_instanceelk"
  }
}
connection {
	type	 = "ssh"
	user	 = "ec2-user"
	private_key = "${file(var.keypath)}"
	host	 = aws_instance.task_ec2_instance.public_ip
}
resource "aws_key_pair" "task_key_pair" {
  key_name   = "terraform-demo"
  public_key = "${file(/Users/jjezewski/tf_deploy.pub)}"
}
output "output_public_ip" {
  value = "${aws_instance.task_ec2_instance.public_ip}"
}