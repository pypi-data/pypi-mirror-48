import json
import setuptools

kwargs = json.loads("""
{
    "name": "aws-cdk.aws-autoscaling-common",
    "version": "0.39.0",
    "description": "Common implementation package for @aws-cdk/aws-autoscaling and @aws-cdk/aws-applicationautoscaling",
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
        "aws_cdk.aws_autoscaling_common",
        "aws_cdk.aws_autoscaling_common._jsii"
    ],
    "package_data": {
        "aws_cdk.aws_autoscaling_common._jsii": [
            "aws-autoscaling-common@0.39.0.jsii.tgz"
        ],
        "aws_cdk.aws_autoscaling_common": [
            "py.typed"
        ]
    },
    "python_requires": ">=3.6",
    "install_requires": [
        "jsii~=0.14.0",
        "publication>=0.0.3",
        "aws-cdk.aws-iam~=0.39.0",
        "aws-cdk.core~=0.39.0"
    ]
}
""")

with open('README.md') as fp:
    kwargs['long_description'] = fp.read()


setuptools.setup(**kwargs)
