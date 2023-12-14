from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in tutorial_app/__init__.py
from tutorial_app import __version__ as version

setup(
	name="tutorial_app",
	version=version,
	description="to learn",
	author="jatin",
	author_email="jatinsarna64@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
