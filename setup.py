from setuptools import setup, find_packages

version = '0.1'

setup(
	name='ckanext-ogdch_actions',
	version=version,
	description="CKAN actions related to OGD@Bund project",
	long_description="""\
	""",
	classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
	keywords='',
	author='Stefan Reinhard',
	author_email='sr@feinheit.ch',
	url='',
	license='BSD',
	packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
	namespace_packages=['ckanext', 'ckanext.ogdch_actions'],
	include_package_data=True,
	zip_safe=False,
	install_requires=[
		# -*- Extra requirements: -*-
	],
	entry_points=\
	"""
    [ckan.plugins]
	ogdch_actions=ckanext.ogdch_actions.actions:OGDActions
	""",
)
