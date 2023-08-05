""" package aries_staticagent """

from setuptools import setup, find_packages

def parse_requirements(filename):
    """Load requirements from a pip requirements file."""
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]

if __name__ == '__main__':
    with open('README.md', 'r') as fh:
        long_description = fh.read()

    setup(
        name='aries-staticagent',
        version='0.2.0',
        author='Daniel Bluhm <daniel.bluhm@sovrin.org>, Sam Curren <sam@sovrin.org>',
        description='Library and example Python Static Agent for Aries',
        long_description=long_description,
        long_description_content_type='text/markdown',
        url='https://github.com/hyperledger/aries-staticagent-python',
        license='Apache 2.0',
        packages=find_packages(),
        install_requires=parse_requirements('requirements.txt'),
        python_requires='>=3.6',
        classifiers=[
            'Programming Language :: Python :: 3',
            'License :: OSI Approved :: Apache Software License',
            'Operating System :: OS Independent'
        ]
    )
