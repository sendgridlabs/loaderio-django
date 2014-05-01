import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-loaderio',
    version='0.2.0',
    packages=['loaderio'],
    include_package_data=True,
    license='MIT License',
    description='An app for adding loader.io validation tokens',
    long_description=README,
    author='Lorin Hochstein',
    author_email='lorin.hochstein@sendgrid.com',
    url='https://github.com/sendgridlabs/loaderio-django',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
