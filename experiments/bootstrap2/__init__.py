from troposphere import Ref, Template
import troposphere.ec2 as ec2

def fill_template(t):
    instance = ec2.Instance("bootstrap2")
    instance.ImageId = "ami-bs2"
    instance.InstanceType = "t1.micro"
    t.add_resource(instance)
    return t
    