import boto3
import openpyxl
from botocore.exceptions import ClientError
from uuid import uuid4


def get_ec2_tags(required_tags):
    mandatory_tags_dict = required_tags
    client = session.client('ec2')
    paginator = client.get_paginator('describe_instances')
    response_iterator = paginator.paginate()

    for page in response_iterator:
        for reservation in page['Reservations']:
            for instance in reservation['Instances']:
                for tag in instance['Tags']:
                    for item in mandatory_tags_dict:
                        if item == tag['Key']:
                            mandatory_tags_dict[item] = tag['Value']

                required_tags_list = [mandatory_tags_dict[keys] for keys in mandatory_tags_dict]
                final_list = [account_id, region, 'instance', instance['InstanceId']]
                final_list.extend(required_tags_list)
                print(final_list)
                ws.append(final_list)


def get_vpc_tags(required_tags):
    mandatory_tags_dict = required_tags
    client = session.client('ec2')
    paginator = client.get_paginator('describe_vpcs')
    response_iterator = paginator.paginate()

    for page in response_iterator:
        for vpc in page['Vpcs']:
            try:
                for tag in vpc['Tags']:
                    for item in mandatory_tags_dict:
                        if item == tag['Key']:
                            mandatory_tags_dict[item] = tag['Value']

                    required_tags_list = [mandatory_tags_dict[keys] for keys in mandatory_tags_dict]
                    final_list = [account_id, region, 'vpc', vpc['VpcId']]
                    final_list.extend(required_tags_list)
                    print(final_list)
                    ws.append(final_list)
            except KeyError:
                final_list = [account_id, region, 'vpc', vpc['VpcId']]
                ws.append(final_list)


def get_subnet_tags(required_tags):
    mandatory_tags_dict = required_tags
    client = session.client('ec2')
    paginator = client.get_paginator('describe_subnets')
    response_iterator = paginator.paginate()

    for page in response_iterator:
        for subnet in page['Subnets']:
            try:
                for tag in subnet['Tags']:
                    for item in mandatory_tags_dict:
                        if item == tag['Key']:
                            mandatory_tags_dict[item] = tag['Value']

                    required_tags_list = [mandatory_tags_dict[keys] for keys in mandatory_tags_dict]
                    final_list = [account_id, region, 'subnet', subnet['SubnetId']]
                    final_list.extend(required_tags_list)
                    print(final_list)
                    ws.append(final_list)
            except KeyError:
                final_list = [account_id, region, 'subnet', subnet['SubnetId']]
                ws.append(final_list)


def get_fsx_tags(required_tags):
    mandatory_tags_dict = required_tags
    client = session.client('fsx')
    paginator = client.get_paginator('describe_file_systems')
    response_iterator = paginator.paginate()

    for page in response_iterator:
        for fsx in page['FileSystems']:
            try:
                for tag in fsx['Tags']:
                    for item in mandatory_tags_dict:
                        if item == tag['Key']:
                            mandatory_tags_dict[item] = tag['Value']

                    required_tags_list = [mandatory_tags_dict[keys] for keys in mandatory_tags_dict]
                    final_list = [account_id, region, 'fsx', fsx['FileSystemId']]
                    final_list.extend(required_tags_list)
                    print(final_list)
                    ws.append(final_list)
            except KeyError:
                final_list = [account_id, region, 'fsx', fsx['FileSystemId']]
                ws.append(final_list)


def get_efs_tags(required_tags):
    mandatory_tags_dict = required_tags
    client = session.client('efs')
    paginator = client.get_paginator('describe_file_systems')
    response_iterator = paginator.paginate()

    for page in response_iterator:
        for efs in page['FileSystems']:
            try:
                for tag in efs['Tags']:
                    for item in mandatory_tags_dict:
                        if item == tag['Key']:
                            mandatory_tags_dict[item] = tag['Value']

                    required_tags_list = [mandatory_tags_dict[keys] for keys in mandatory_tags_dict]
                    final_list = [account_id, region, 'efs', efs['FileSystemId']]
                    final_list.extend(required_tags_list)
                    print(final_list)
                    ws.append(final_list)
            except KeyError:
                final_list = [account_id, region, 'efs', efs['FileSystemId']]
                ws.append(final_list)


def get_igw_tags(required_tags):
    mandatory_tags_dict = required_tags
    client = session.client('ec2')
    paginator = client.get_paginator('describe_internet_gateways')
    response_iterator = paginator.paginate()

    for page in response_iterator:
        for igw in page['InternetGateways']:
            try:
                for tag in igw['Tags']:
                    for item in mandatory_tags_dict:
                        if item == tag['Key']:
                            mandatory_tags_dict[item] = tag['Value']

                    required_tags_list = [mandatory_tags_dict[keys] for keys in mandatory_tags_dict]
                    final_list = [account_id, region, 'igw', igw['InternetGatewayId']]
                    final_list.extend(required_tags_list)
                    print(final_list)
                    ws.append(final_list)
            except KeyError:
                final_list = [account_id, region, 'igw', igw['InternetGatewayId']]
                ws.append(final_list)


def get_ebs_tags(required_tags):
    mandatory_tags_dict = required_tags
    client = session.client('ec2')
    paginator = client.get_paginator('describe_volumes')
    response_iterator = paginator.paginate()

    for page in response_iterator:
        for ebs in page['Volumes']:
            try:
                for tag in ebs['Tags']:
                    for item in mandatory_tags_dict:
                        if item == tag['Key']:
                            mandatory_tags_dict[item] = tag['Value']

                    required_tags_list = [mandatory_tags_dict[keys] for keys in mandatory_tags_dict]
                    final_list = [account_id, region, 'ebs', ebs['VolumeId']]
                    final_list.extend(required_tags_list)
                    print(final_list)
                    ws.append(final_list)
            except KeyError:
                final_list = [account_id, region, 'ebs', ebs['VolumeId']]
                ws.append(final_list)


def get_workspaces_tags(required_tags):
    """ Using describe_tags method """
    mandatory_tags_dict = required_tags
    client = session.client('workspaces')
    paginator = client.get_paginator('describe_workspaces')
    response_iterator = paginator.paginate()

    for page in response_iterator:
        for workspace in page['Workspaces']:
            response = client.describe_tags(
                ResourceId=workspace['WorkspaceId']
            )
            try:
                for tag in response['TagList']:
                    for item in mandatory_tags_dict:
                        if item == tag['Key']:
                            mandatory_tags_dict[item] = tag['Value']

                    required_tags_list = [mandatory_tags_dict[keys] for keys in mandatory_tags_dict]
                    final_list = [account_id, region, 'workspace', workspace['WorkspaceId']]
                    final_list.extend(required_tags_list)
                    print(final_list)
                    ws.append(final_list)
            except KeyError:
                final_list = [account_id, region, 'workspace', workspace['WorkspaceId']]
                ws.append(final_list)


def get_clb_tags(required_tags):
    """ Using describe_tags method """
    mandatory_tags_dict = required_tags
    client = session.client('elb')
    paginator = client.get_paginator('describe_load_balancers')
    response_iterator = paginator.paginate()

    for page in response_iterator:
        for clb in page['LoadBalancerDescriptions']:
            response = client.describe_tags(
                ResourceId=clb['LoadBalancerName']
            )
            try:
                for tag in response['TagList']:
                    for item in mandatory_tags_dict:
                        if item == tag['Key']:
                            mandatory_tags_dict[item] = tag['Value']

                    required_tags_list = [mandatory_tags_dict[keys] for keys in mandatory_tags_dict]
                    final_list = [account_id, region, 'classic load balancer', clb['WorkspaceId']]
                    final_list.extend(required_tags_list)
                    print(final_list)
                    ws.append(final_list)
            except KeyError:
                final_list = [account_id, region, 'classic load balancer', clb['WorkspaceId']]
                ws.append(final_list)


def get_elb_tags(required_tags):
    """ Using describe_tags method """
    mandatory_tags_dict = required_tags
    client = session.client('elbv2')
    paginator = client.get_paginator('describe_load_balancers')
    response_iterator = paginator.paginate()

    for page in response_iterator:
        for elb in page['LoadBalancers']:
            response = client.describe_tags(
                ResourceArns=[
                    elb['LoadBalancerArn'],
                ]
            )
            try:
                for tags in response['TagDescriptions']:
                    for tag in tags['Tags']:
                        for item in mandatory_tags_dict:
                            if item == tag['Key']:
                                mandatory_tags_dict[item] = tag['Value']

                    required_tags_list = [mandatory_tags_dict[keys] for keys in mandatory_tags_dict]
                    final_list = [account_id, region, f'{elb["Type"]} load balancer', elb['WorkspaceId']]
                    final_list.extend(required_tags_list)
                    print(final_list)
                    ws.append(final_list)
            except KeyError:
                final_list = [account_id, region, f'{elb["Type"]} load balancer', elb['WorkspaceId']]
                ws.append(final_list)


def get_rds_tags(required_tags):
    mandatory_tags_dict = required_tags
    client = session.client('rds')
    paginator = client.get_paginator('describe_db_instances')
    response_iterator = paginator.paginate()

    for page in response_iterator:
        for rds in page['DBInstances']:
            try:
                for tag in rds['TagList']:
                    for item in mandatory_tags_dict:
                        if item == tag['Key']:
                            mandatory_tags_dict[item] = tag['Value']

                    required_tags_list = [mandatory_tags_dict[keys] for keys in mandatory_tags_dict]
                    final_list = [account_id, region, 'rds', rds['DBInstanceIdentifier']]
                    final_list.extend(required_tags_list)
                    print(final_list)
                    ws.append(final_list)
            except KeyError:
                final_list = [account_id, region, 'rds', rds['DBInstanceIdentifier']]
                ws.append(final_list)


def get_lambda_tags(required_tags):
    """ Using list_tags method, different from rest of the code """
    mandatory_tags_dict = required_tags
    client = session.client('lambda')
    paginator = client.get_paginator('list_functions')
    response_iterator = paginator.paginate()

    for page in response_iterator:
        for lambda_function in page['Functions']:
            response = client.list_tags(
                Resource=lambda_function['FunctionArn']
            )
            try:
                for tag in response['Tags']:
                    for item in mandatory_tags_dict:
                        if item == tag:
                            mandatory_tags_dict[item] = response['Tags'][tag]

                    required_tags_list = [mandatory_tags_dict[keys] for keys in mandatory_tags_dict]
                    final_list = [account_id, region, 'lambda', lambda_function['FunctionName']]
                    final_list.extend(required_tags_list)
                    print(final_list)
                    ws.append(final_list)
            except KeyError:
                final_list = [account_id, region, 'lambda', lambda_function['FunctionName']]
                ws.append(final_list)


def get_s3_tags(required_tags):
    """ No paginator """
    mandatory_tags_dict = required_tags
    client = session.client('s3')
    response = client.list_buckets()
    for s3 in response['Buckets']:
        try:
            tag_response = client.get_bucket_tagging(
                Bucket=s3['Name']
            )
            for tag in tag_response['TagSet']:
                for item in mandatory_tags_dict:
                    if item == tag['Key']:
                        mandatory_tags_dict[item] = tag['Value']

                required_tags_list = [mandatory_tags_dict[keys] for keys in mandatory_tags_dict]
                final_list = [account_id, region, 's3', s3['Name']]
                final_list.extend(required_tags_list)
                print(final_list)
                ws.append(final_list)
        except KeyError:
            final_list = [account_id, region, 's3', s3['Name']]
            ws.append(final_list)


if __name__ == "__main__":
    profiles = boto3.session.Session().available_profiles
    regions = boto3.session.Session().get_available_regions('ec2')
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(['AWS Account ID', 'Region', 'Resource Type', 'Resource ID', 'name', 'application', 'environment', 'owner'])

    mandate_tags = {
        'name': '',
        'application': '',
        'environment': '',
        'owner': ''}

    for profile in profiles:
        account_id = profile.split('-')[0]
        for region in regions:
            print(account_id, region)
            try:
                session = boto3.session.Session(profile_name=profile, region_name=region)
                get_ec2_tags(mandate_tags)
                get_vpc_tags(mandate_tags)
                get_subnet_tags(mandate_tags)
                get_fsx_tags(mandate_tags)
                get_igw_tags(mandate_tags)
                get_ebs_tags(mandate_tags)
                get_workspaces_tags(mandate_tags)
                get_clb_tags(mandate_tags)
                get_elb_tags(mandate_tags)
                get_rds_tags(mandate_tags)
                get_lambda_tags(mandate_tags)
                get_s3_tags(mandate_tags)

            except ClientError as err:
                if err.response['Error']['Code'] == 'AuthFailure':
                    pass
                else:
                    print(err)

    wb.save(f"TagReport-{str(uuid4())[:7]}.xlsx")
