import json
import setuptools

kwargs = json.loads("""
{
    "name": "aws-cdk.aws-autoscaling-hooktargets",
    "version": "0.36.0",
    "description": "Lifecycle hook for AWS AutoScaling",
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
        "aws_cdk.aws_autoscaling_hooktargets",
        "aws_cdk.aws_autoscaling_hooktargets._jsii"
    ],
    "package_data": {
        "aws_cdk.aws_autoscaling_hooktargets._jsii": [
            "aws-autoscaling-hooktargets@0.36.0.jsii.tgz"
        ],
        "aws_cdk.aws_autoscaling_hooktargets": [
            "py.typed"
        ]
    },
    "python_requires": ">=3.6",
    "install_requires": [
        "jsii~=0.12.1",
        "publication>=0.0.3",
        "aws-cdk.aws-autoscaling~=0.36.0",
        "aws-cdk.aws-iam~=0.36.0",
        "aws-cdk.aws-lambda~=0.36.0",
        "aws-cdk.aws-sns~=0.36.0",
        "aws-cdk.aws-sns-subscriptions~=0.36.0",
        "aws-cdk.aws-sqs~=0.36.0",
        "aws-cdk.core~=0.36.0"
    ]
}
""")

with open('README.md') as fp:
    kwargs['long_description'] = fp.read()


setuptools.setup(**kwargs)
