from setuptools import setup

setup(
	name='shotty',
	version='0.1',
	author="Andrew Callan",
	author_email="andrew.g.callan@gmail.com",
	description="Shotty manages aws snapshots",
	license="GPLv3+",
	packages=['shotty'],
	url="https://github.com/a-callan94/AWSPython",
	install_requires=[
		'click',
		'boto3'
		],
	entry_points='''
		[console_scripts]
		shotty=shotty.shotty:cli
	''',
)			