try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description' : 'My Project',
	'author' : 'Alec H',
	'url' : 'none',
	'download_url': 'none',
	'author_email': 'My email',
	'version' : '0.1',
	'install_requires' : ['nose'],
	'packages' : ['NAME'],
	'scripts' : [],
	'name' : 'projectname'
}

setup(**config)
