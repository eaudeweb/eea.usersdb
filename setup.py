from setuptools import setup, find_packages

setup(
    name='eea.usersdb',
    version='1.2.4-ispra',
    author='Eau de Web',
    author_email='office@eaudeweb.ro',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['python-ldap', 'colander'],
)
