import setuptools

with open("README.md", "r") as readme:
	long_description = readme.read()

setuptools.setup(
	name="base24builder",
	version="2020.1",
	author="Base24 - original: Pu Anlai",
	description="A base 24 builder written in Python",
	long_description=long_description,
    long_description_content_type="text/markdown",
	url="https://github.com/Base24/base24-builder-python",
	packages=setuptools.find_packages(),
	classifiers=[
		"Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    keywords="base24",
    install_requires=["pystache", "pyyaml", "aiofiles"],
    python_requires=">=3.5",
    entry_points={"console_scripts": ["base24 = base24_builder.cli:run"]},
)
