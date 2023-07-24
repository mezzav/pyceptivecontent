from setuptools import find_packages, setup

setup( 
    name="pyceptivecontent",
    packages=find_packages(include=['pyceptivecontent', 'pyceptivecontent.exceptions', 'pyceptivecontent.models']),
    version="0.1.0",
    description="Python wrapper library for the Perceptive Content Integration server REST API",
    install_requires = [
        "requests",
        "requests-toolbelt",
        "pydantic"
    ],
    author="mezzav"
)
