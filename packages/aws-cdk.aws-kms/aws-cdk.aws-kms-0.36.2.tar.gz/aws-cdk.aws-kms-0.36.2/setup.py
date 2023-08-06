import json
import setuptools

kwargs = json.loads("""
{
    "name": "aws-cdk.aws-kms",
    "version": "0.36.2",
    "description": "CDK Constructs for AWS KMS",
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
        "aws_cdk.aws_kms",
        "aws_cdk.aws_kms._jsii"
    ],
    "package_data": {
        "aws_cdk.aws_kms._jsii": [
            "aws-kms@0.36.2.jsii.tgz"
        ],
        "aws_cdk.aws_kms": [
            "py.typed"
        ]
    },
    "python_requires": ">=3.6",
    "install_requires": [
        "jsii~=0.13.3",
        "publication>=0.0.3",
        "aws-cdk.aws-iam~=0.36.2",
        "aws-cdk.core~=0.36.2"
    ]
}
""")

with open('README.md') as fp:
    kwargs['long_description'] = fp.read()


setuptools.setup(**kwargs)
