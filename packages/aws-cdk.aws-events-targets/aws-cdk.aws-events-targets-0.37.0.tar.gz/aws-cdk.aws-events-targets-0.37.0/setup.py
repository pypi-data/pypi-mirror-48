import json
import setuptools

kwargs = json.loads("""
{
    "name": "aws-cdk.aws-events-targets",
    "version": "0.37.0",
    "description": "Event targets for AWS CloudWatch Events",
    "url": "https://github.com/awslabs/aws-cdk",
    "long_description_content_type": "text/markdown",
    "author": "Amazon Web Services",
    "project_urls": {
        "Source": "https://github.com/awslabs/aws-cdk.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "aws_cdk.aws_events_targets",
        "aws_cdk.aws_events_targets._jsii"
    ],
    "package_data": {
        "aws_cdk.aws_events_targets._jsii": [
            "aws-events-targets@0.37.0.jsii.tgz"
        ],
        "aws_cdk.aws_events_targets": [
            "py.typed"
        ]
    },
    "python_requires": ">=3.6",
    "install_requires": [
        "jsii~=0.13.3",
        "publication>=0.0.3",
        "aws-cdk.aws-cloudformation~=0.37.0",
        "aws-cdk.aws-codebuild~=0.37.0",
        "aws-cdk.aws-codepipeline~=0.37.0",
        "aws-cdk.aws-ec2~=0.37.0",
        "aws-cdk.aws-ecs~=0.37.0",
        "aws-cdk.aws-events~=0.37.0",
        "aws-cdk.aws-iam~=0.37.0",
        "aws-cdk.aws-lambda~=0.37.0",
        "aws-cdk.aws-sns~=0.37.0",
        "aws-cdk.aws-sns-subscriptions~=0.37.0",
        "aws-cdk.aws-sqs~=0.37.0",
        "aws-cdk.aws-stepfunctions~=0.37.0",
        "aws-cdk.core~=0.37.0",
        "aws-cdk.custom-resources~=0.37.0"
    ]
}
""")

with open('README.md') as fp:
    kwargs['long_description'] = fp.read()


setuptools.setup(**kwargs)
