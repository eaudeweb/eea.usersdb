from setuptools import setup, find_packages

setup(
    name='eea.usersdb',
    version='1.3.46',
    author='Eau de Web',
    author_email='office@eaudeweb.ro',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['python-ldap', 'colander', 'phonenumbers'],
)
