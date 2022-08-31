from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in hwc_app/__init__.py
from hwc_app import __version__ as version

setup(
	name="hwc_app",
	version=version,
	description="hwc",
	author="eric",
	author_email="5577999@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
