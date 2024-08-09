# aws-tag-collector
Collects tags of AWS resources

Make edits to line 341 - 347, add the necessary tags that needs to be collected.
Mentioned tags will be saved to an Excel sheet.

This script loops through all the AWS profiles in .aws/credentials file.
Now , this script collects tags for following resources : vpc, subnet, fsx,efs,internet gateway,ec2, ebs, workspace, elb,rds,lambda and s3
