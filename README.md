[![Github top language](https://img.shields.io/github/languages/top/Base24/base24-builder-python.svg?style=for-the-badge&cacheSeconds=28800)](../../)
[![Codacy grade](https://img.shields.io/codacy/grade/3479c0638ef54d57839343ad4be367e0.svg?style=for-the-badge&cacheSeconds=28800)](https://www.codacy.com/gh/Base24/base24-builder-python)
[![Issues](https://img.shields.io/github/issues/Base24/base24-builder-python.svg?style=for-the-badge&cacheSeconds=28800)](../../issues)
[![License](https://img.shields.io/github/license/Base24/base24-builder-python.svg?style=for-the-badge&cacheSeconds=28800)](/LICENSE.md)
[![Commit activity](https://img.shields.io/github/commit-activity/m/Base24/base24-builder-python.svg?style=for-the-badge&cacheSeconds=28800)](../../commits/master)
[![Last commit](https://img.shields.io/github/last-commit/Base24/base24-builder-python.svg?style=for-the-badge&cacheSeconds=28800)](../../commits/master)
[![PyPI](https://img.shields.io/pypi/dm/base24builder.svg?style=for-the-badge&cacheSeconds=28800)](https://pypi.org/project/base24builder/)

<!-- omit in TOC -->
# base24-builder-python

<img src="readme-assets/icons/name.png" alt="Project Icon" width="750">

A base 24 builder written in Python

Thank you to https://github.com/InspectorMustache/base16-builder-python (MIT)
for the original base16-builder

- [Installation](#installation)
- [Install With PIP](#install-with-pip)
- [Usage](#usage)
	- [Basic Usage](#basic-usage)
	- [Update](#update)
	- [Build](#build)
	- [Inject](#inject)
	- [Exit](#exit)
- [Language information](#language-information)
	- [Built for](#built-for)
- [Install Python on Windows](#install-python-on-windows)
	- [Chocolatey](#chocolatey)
	- [Download](#download)
- [Install Python on Linux](#install-python-on-linux)
	- [Apt](#apt)
- [How to run](#how-to-run)
	- [With VSCode](#with-vscode)
	- [From the Terminal](#from-the-terminal)
- [How to update, build and publish](#how-to-update-build-and-publish)
- [Download](#download-1)
	- [Clone](#clone)
		- [Using The Command Line](#using-the-command-line)
		- [Using GitHub Desktop](#using-github-desktop)
	- [Download Zip File](#download-zip-file)
- [Community Files](#community-files)
	- [Licence](#licence)
	- [Changelog](#changelog)
	- [Code of Conduct](#code-of-conduct)
	- [Contributing](#contributing)
	- [Security](#security)

## Installation
As this project uses async/await syntax, the lowest supported Python version is
3.5.

## Install With PIP

```python
pip install base24builder
```

Head to https://pypi.org/project/base24builder/ for more info


## Usage
There are three modes of operation:

```bash
./base24.py update
./base24.py build
./base24.py inject
```

### Basic Usage

If you just want to build all base24 colorschemes and then pick out the ones you
need, simply run:
```bash
./base24.py update
./base24.py build
```

Once the process is finished, you can find all colorschemes in a folder named
output located in the current working directory.

For a more detailed explanation of the individual commands, read on.

### Update

Downloads all base24/ base16 schemes and templates to the current working
directory.
The source files, i.e. the files pointing to the scheme and template
repositories


will also be updated by default.  If you want to use your own versions of these
files (to exclude specific repositories, for example), you can prevent the
builder from updating the source files by using the `-c/--custom` option.

You can use `-v/--verbose` for more detailed output.

### Build

Builds base24 colorschemes for all schemes and templates.  This requires the
directory structure and files created by the update operation to be present in
the working directory.  This operation accepts four parameters:

- `-s/--scheme` restricts building to specific schemes

  Can be specified more than once.  Each argument must match a scheme.
  Wildcards can be used but must be escaped properly so they are not expanded
  by the shell.

- `-t/--template` restricts building to specific templates

  Can be specified more than once.  Each argument must correspond to a folder
  name in the templates directory.

- `-o/--output` specifies a path where built colorschemes will be placed

  If this option is not specified, an "output" folder in the current working
  directory will be created and used.

- `-v/--verbose` increases verbosity

  With this option specified the builder prints out the name of each scheme as
  it's built.

Example:
```bash
./base24.py build -t dunst -s atelier-heath-light -o /tmp/output
```

### Inject

This operation provides an easier way to quickly insert a specific colorscheme
into one or more config files.  In order for the builder to locate the necessary
files, this command relies on the folder structure created by the update
command.  The command accepts two parameters:

- `-s/--scheme` specifies the scheme you wish to inject

  Refers to the scheme that should be inserted.  You can use wildcards and the
  same restrictions as with update apply.  A pattern that matches more than one
  scheme will cause an error.

- `-f/--file` specifies the file(s) into which you wish the scheme to be
  inserted

  Can be specified more than once.  Each argument must be specified as a path
  to a config file that features proper injection markers (see below).

You will need to prepare your configuration files so that the script knows where
to insert the colorscheme.  This is done by including two lines in the file
```bash
# %%base24_template: TEMPLATE_NAME##SUBTEMPLATE_NAME %%

Everything in-between these two lines will be replaced with the colorscheme.

# %%base24_template_end%%
```

Both lines can feature arbitrary characters before the first two percentage
signs.  This is so as to accomodate different commenting styles.  Both lines
need to end exactly as demonstrated above, however.  "TEMPLATE_NAME" and
"SUBTEMPLATE_NAME" are the exception to this.  Replace TEMPLATE_NAME with the
name of the template you wish to insert, for example "gnome-terminal".  This
must correspond to a folder in the templates directory.  Replace
SUBTEMPLATE_NAME with the name of the subtemplate as it is defined at the
top level of the template's config.yaml file (see
`file.md <https://github.com/chriskempson/base16/blob/master/file.md>`_ for
details), for example "default-256".  If you omit the subtemplate name (don't
omit "##" though), "default" is assumed.



Specify the name of the scheme you wish to inject with the -s option.  Use the
-f option for each file into which you want to inject the scheme.

As an example, here's the command I use to globally change the color scheme in
all applications that support it:
```bash
./base24.py inject -s ocean -f ~/.gtkrc-2.0.mine -f ~/.config/dunst/dunstrc -f
~/.config/i3/config -f ~/.config/termite/config -f ~/.config/zathura/zathurarc
```

### Exit

The program exits with exit code 1 if it encountered a general error and with
2 if one or more build or update tasks produced a warning or an error.



## Language information
### Built for
This program has been written for Python 3 and has been tested with
Python version 3.8.0 <https://www.python.org/downloads/release/python-380/>.

## Install Python on Windows
### Chocolatey
```powershell
choco install python
```
### Download
To install Python, go to <https://www.python.org/> and download the latest
version.

## Install Python on Linux
### Apt
```bash
sudo apt install python3.8
```

## How to run
### With VSCode
1. Open the .py file in vscode
2. Ensure a python 3.8 interpreter is selected (Ctrl+Shift+P > Python:Select
Interpreter > Python 3.8)
3. Run by pressing Ctrl+F5 (if you are prompted to install any modules, accept)
### From the Terminal
```bash
./[file].py
```

## How to update, build and publish

1. Ensure you have installed the following dependencies
	Linux
	```bash
	wget dephell.org/install | python3.8
	wget https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3.8
	```
	Windows
	```powershell
	(wget dephell.org/install -UseBasicParsing).Content | python
	(wget https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python
	```
2. Use poetry for the heavy lifting and dephell to generate requirements
	```bash
	poetry update
	dephell deps convert
	```
3. Build/ Publish
	```bash
	poetry build
	poetry publish
	```
	or
	```bash
	poetry publish --build
	```


## Download
### Clone
#### Using The Command Line
1. Press the Clone or download button in the top right
2. Copy the URL (link)
3. Open the command line and change directory to where you wish to
clone to
4. Type 'git clone' followed by URL in step 2
```bash
$ git clone https://github.com/Base24/base24-builder-python
```

More information can be found at
<https://help.github.com/en/articles/cloning-a-repository>

#### Using GitHub Desktop
1. Press the Clone or download button in the top right
2. Click open in desktop
3. Choose the path for where you want and click Clone

More information can be found at
<https://help.github.com/en/desktop/contributing-to-projects/cloning-a-repository-from-github-to-github-desktop>

### Download Zip File

1. Download this GitHub repository
2. Extract the zip archive
3. Copy/ move to the desired location

If you don't want to clutter your computer with something that you're just
going to use once you can also just clone this repository and use the provided base24.py file.

## Community Files
### Licence
MIT License
(See the [LICENSE](/LICENSE.md) for more information.)

### Changelog
See the [Changelog](/CHANGELOG.md) for more information.

### Code of Conduct
In the interest of fostering an open and welcoming environment, we
as contributors and maintainers pledge to make participation in our
project and our community a harassment-free experience for everyone.
Please see the
[Code of Conduct](https://github.com/Base24/.github/blob/master/CODE_OF_CONDUCT.md) for more information.

### Contributing
Contributions are welcome, please see the [Contributing Guidelines](https://github.com/Base24/.github/blob/master/CONTRIBUTING.md) for more information.

### Security
Thank you for improving the security of the project, please see the [Security Policy](https://github.com/Base24/.github/blob/master/SECURITY.md) for more information.
