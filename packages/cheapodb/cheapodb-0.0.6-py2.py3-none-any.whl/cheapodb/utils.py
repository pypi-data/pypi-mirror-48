import os
import json
import logging
from datetime import datetime
import boto3

log = logging.getLogger(__name__)


class CheapoDBException(Exception):
    pass


def create_session(**kwargs):
    return boto3.session.Session(
        region_name=kwargs.get('aws_default_region', os.getenv('AWS_DEFAULT_REGION')),
        aws_access_key_id=kwargs.get('aws_access_key_id', os.getenv('AWS_ACCESS_KEY_ID')),
        aws_secret_access_key=kwargs.get('aws_secret_access_key', os.getenv('AWS_SECRET_ACCESS_KEY'))
    )


def normalize_table_name(name):
    """Check if the table name is obviously invalid."""
    if not isinstance(name, str):
        raise ValueError()
    name = name.replace('-', '_').strip()
    if not len(name):
        raise ValueError(f'Invalid table name: {name}')
    return name


def create_cheapodb_role(name, client, bucket) -> str:
    """
    Create an AWS IAM service role with the appropriate permissions for Glue and the database's S3 bucket.

    :param name:
    :param client:
    :param bucket:
    :return:
    """
    try:
        response = client.create_role(
            RoleName=name,
            Path='/service-role/',
            Description=f'IAM role created by CheapoDB on {datetime.now():%Y-%m-%d %H:%M:%S}',
            AssumeRolePolicyDocument=json.dumps(dict(
                Version='2012-10-17',
                Statement=[
                    {
                        'Sid': '',
                        'Effect': 'Allow',
                        'Principal': {
                            'Service': 'glue.amazonaws.com'
                        },
                        'Action': 'sts:AssumeRole'
                    }
                ]
            ))
        )
        iam_role_arn = response['Role']['Arn']

        response = client.attach_role_policy(
            RoleName=name,
            PolicyArn='arn:aws:iam::aws:policy/service-role/AWSGlueServiceRole'
        )
        log.debug(response)

        response = client.put_role_policy(
            RoleName=name,
            PolicyName='CheapoDBRolePolicy',
            PolicyDocument=json.dumps(dict(
                Version='2012-10-17',
                Statement=[
                    {
                        'Effect': 'Allow',
                        'Action': [
                            's3:GetObject',
                            's3:PutObject'
                        ],
                        'Resource': [
                            f'arn:aws:s3:::{bucket}*'
                        ]
                    }
                ]
            ))
        )
        log.debug(response)
    except client.exceptions.EntityAlreadyExistsException:
        msg = f'Role already exists for database: CheapoDBRole-{bucket}. ' \
              f'Provide the role ARN as iam_role_arn.'
        raise CheapoDBException(msg)

    return iam_role_arn
