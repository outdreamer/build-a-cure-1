resource "aws_instance" "task_ec2_instance" {
  ami		   = "ami-024d1b90da07e64a6"
  instance_type = "t2.micro"
  user_data	 = file("/Users/jjezewski/Documents/build_a_cure/tasks/install_boot_elk.sh")
  tags = {
    Name  = "task_ec2_instance_elk"
  }
}
output "output_public_ip" {
  value = aws_instance.task_ec2_instance.public_ip
}