from setuptools import find_packages, setup

setup( 
    name="pyceptivecontent",
    packages=find_packages(include=['pyceptivecontent', 'pyceptivecontent.exceptions']),
    version="0.1.0",
    description="Python wrapper library for the Perceptive Content Integration server REST API",
    author="mezzav"
)
