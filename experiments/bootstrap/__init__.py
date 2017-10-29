from troposphere import Ref, Template
import troposphere.ec2 as ec2

def fill_template(t):
    instance = ec2.Instance("myinstance")
    instance.ImageId = "ami-951945d0"
    instance.InstanceType = "t1.micro"
    t.add_resource(instance)
    return t
    