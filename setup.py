from setuptools import setup


# Define __version__
with open('holepunch/version.py', 'r') as fp:
    exec(fp.read())


setup(
    name='holepunch',
    version=__version__,
    description="Punch holes in your AWS account security",
    author='Erik Price',
    url='https://github.com/erik/holepunch',
    packages=['holepunch'],
    entry_points={
        'console_scripts': [
            'holepunch = holepunch:main',
        ],
    },
    license='MIT',
    install_requires=[
        'boto3==1.5.6',
        'docopt==0.6.2',
        'six==1.11.0',
        # Backport for python2.7
        'ipaddress==1.0.19'
    ]
)
