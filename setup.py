try: 
	from setuptools import setup
except ImportError: 
	from distutils.core import setup

config = { 
	'description': 'My LPTHW Project', 
	'author': 'quantum-cupcake', 
	'url': 'N/A',
	'download_url': 'N/A',
	'author_email': 'eugen.azan@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['LPTHW_web'],
	'scripts': [],
	'name': 'projectname'
}

setup(**config)