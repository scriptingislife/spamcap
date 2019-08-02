provider "aws" {
    region = "us-east-1"
}

data "aws_ami" "ubuntu" {
    most_recent = true
    filter {
        name = "name"
        values = ["ubuntu/images/hvm-ssd/ubuntu-bionic-18.04-amd64-server-*"]
    }

    filter {
        name = "virtualization-type"
        values = ["hvm"]
    }

    owners = ["099720109477"] # Canonical
}

resource "aws_security_group" "allow_smtp" {
    name = "allow_smtp"
    description = "Allow SMTP on port 25"

    ingress {
        from_port = 22
        to_port = 25
        protocol = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }
}

resource "aws_instance" "spamcap" {
    ami = "${data.aws_ami.ubuntu.id}"
    instance_type = "t3.nano"
    security_groups = ["${aws_security_group.allow_smtp.name}"]
    key_name = "AWSDefault"

    tags = {
        Name = "Spamcap"
    }
}
