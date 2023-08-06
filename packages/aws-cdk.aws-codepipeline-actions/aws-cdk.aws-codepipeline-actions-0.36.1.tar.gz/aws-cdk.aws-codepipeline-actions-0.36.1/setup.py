import json
import setuptools

kwargs = json.loads("""
{
    "name": "aws-cdk.aws-codepipeline-actions",
    "version": "0.36.1",
    "description": "Concrete Actions for AWS Code Pipeline",
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
        "aws_cdk.aws_codepipeline_actions",
        "aws_cdk.aws_codepipeline_actions._jsii"
    ],
    "package_data": {
        "aws_cdk.aws_codepipeline_actions._jsii": [
            "aws-codepipeline-actions@0.36.1.jsii.tgz"
        ],
        "aws_cdk.aws_codepipeline_actions": [
            "py.typed"
        ]
    },
    "python_requires": ">=3.6",
    "install_requires": [
        "jsii~=0.13.2",
        "publication>=0.0.3",
        "aws-cdk.aws-cloudformation~=0.36.1",
        "aws-cdk.aws-codebuild~=0.36.1",
        "aws-cdk.aws-codecommit~=0.36.1",
        "aws-cdk.aws-codedeploy~=0.36.1",
        "aws-cdk.aws-codepipeline~=0.36.1",
        "aws-cdk.aws-ec2~=0.36.1",
        "aws-cdk.aws-ecr~=0.36.1",
        "aws-cdk.aws-ecs~=0.36.1",
        "aws-cdk.aws-events~=0.36.1",
        "aws-cdk.aws-events-targets~=0.36.1",
        "aws-cdk.aws-iam~=0.36.1",
        "aws-cdk.aws-lambda~=0.36.1",
        "aws-cdk.aws-s3~=0.36.1",
        "aws-cdk.aws-sns~=0.36.1",
        "aws-cdk.aws-sns-subscriptions~=0.36.1",
        "aws-cdk.core~=0.36.1"
    ]
}
""")

with open('README.md') as fp:
    kwargs['long_description'] = fp.read()


setuptools.setup(**kwargs)
