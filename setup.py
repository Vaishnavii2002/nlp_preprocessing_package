import setuptools
with open('README.md', 'r') as file:
	long_dexcription = file.read()

setuptools.setup(
	name ='preprocess_',
	version = '0.0.1',
	author = 'Vaishnavi Jambe',
	description = 'This is preprocessing package',
	long_description = long_description,
	long_description_content_type = 'text',
	packages = setuptools.find_packages(),
	classifiers = [
	'Programming Language' :: Python :: 3,
	'license :: OSI Approved :: MIT License']
	)