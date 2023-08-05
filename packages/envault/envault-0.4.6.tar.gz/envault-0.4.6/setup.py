from setuptools import setup, find_packages

import envault

long_description = (
        "A simple CLI tool to run processes with secrets from HashiCorp Vault."
    )

setup(
    name="envault",
    version=envault.__version__,
    author="Pratish Shrestha",
    author_email="pratishshr@gmail.com",
    packages=find_packages(),
    description="A simple CLI tool to run processes with secrets from HashiCorp Vault.",
    long_description=long_description,
    py_modules=["envault"],
    install_requires=[
        "Click==7.0",
        "requests==2.21.0",
        "boto3==1.9.135",
        "PyYAML==5.1",
    ],
    entry_points="""
        [console_scripts]
        envault=envault.cli:cli
    """,
    url="https://github.com/pratishshr/envault",
)
