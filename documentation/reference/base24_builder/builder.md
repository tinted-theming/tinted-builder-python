# Builder

[Base24-builder-python Index](../README.md#base24-builder-python-index) /
[Base24 Builder](./index.md#base24-builder) /
Builder

> Auto-generated documentation for [base24_builder.builder](../../../base24_builder/builder.py) module.

- [Builder](#builder)
  - [TemplateGroup](#templategroup)
    - [TemplateGroup().get_templates](#templategroup()get_templates)
  - [build](#build)
  - [build_scheduler](#build_scheduler)
  - [build_single](#build_single)
  - [build_single_task](#build_single_task)
  - [format_scheme](#format_scheme)
  - [get_parent_dir](#get_parent_dir)
  - [get_pystache_parsed](#get_pystache_parsed)
  - [get_scheme_dirs](#get_scheme_dirs)
  - [get_scheme_files](#get_scheme_files)
  - [get_template_dirs](#get_template_dirs)
  - [reverse_hex](#reverse_hex)
  - [slugify](#slugify)

## TemplateGroup

[Show source in builder.py:12](../../../base24_builder/builder.py#L12)

Representation of a template group, i.e. a group of templates specified
in a config.yaml.

#### Signature

```python
class TemplateGroup:
    def __init__(self, base_path): ...
```

### TemplateGroup().get_templates

[Show source in builder.py:21](../../../base24_builder/builder.py#L21)

Return a list of template_dicts based on the config.yaml in
$self.base_path. Keys correspond to templates and values represent
further settings regarding each template. A pystache object containing
the parsed corresponding mustache file is added to the sub-dictionary.

#### Signature

```python
def get_templates(self): ...
```



## build

[Show source in builder.py:201](../../../base24_builder/builder.py#L201)

Main build function to initiate building process.

#### Signature

```python
def build(templates=None, schemes=None, base_output_dir=None, verbose=False): ...
```



## build_scheduler

[Show source in builder.py:195](../../../base24_builder/builder.py#L195)

Create a task list from scheme_files and run tasks asynchronously.

#### Signature

```python
async def build_scheduler(scheme_files, job_options): ...
```



## build_single

[Show source in builder.py:141](../../../base24_builder/builder.py#L141)

Build colorscheme from $scheme_file using $job_options. Return True if
completed without warnings. Otherwise false.

#### Signature

```python
async def build_single(scheme_file, job_options): ...
```



## build_single_task

[Show source in builder.py:185](../../../base24_builder/builder.py#L185)

Worker thread for picking up scheme files from $queue and building b16
templates using $templates until it receives None.

#### Signature

```python
async def build_single_task(scheme_file, job_options): ...
```



## format_scheme

[Show source in builder.py:87](../../../base24_builder/builder.py#L87)

Change $scheme so it can be applied to a template.

#### Signature

```python
def format_scheme(scheme, slug): ...
```



## get_parent_dir

[Show source in builder.py:36](../../../base24_builder/builder.py#L36)

Get the directory $level levels above $base_dir.

#### Signature

```python
def get_parent_dir(base_dir, level=1): ...
```



## get_pystache_parsed

[Show source in builder.py:44](../../../base24_builder/builder.py#L44)

Return a ParsedTemplate instance based on the contents of
$mustache_file.

#### Signature

```python
def get_pystache_parsed(mustache_file): ...
```



## get_scheme_dirs

[Show source in builder.py:60](../../../base24_builder/builder.py#L60)

Return a set of all scheme directories.

#### Signature

```python
def get_scheme_dirs(): ...
```



## get_scheme_files

[Show source in builder.py:68](../../../base24_builder/builder.py#L68)

Return a list of all (or those matching $pattern) yaml (scheme)
files.

#### Signature

```python
def get_scheme_files(patterns=None): ...
```



## get_template_dirs

[Show source in builder.py:52](../../../base24_builder/builder.py#L52)

Return a set of all template directories.

#### Signature

```python
def get_template_dirs(): ...
```



## reverse_hex

[Show source in builder.py:81](../../../base24_builder/builder.py#L81)

Reverse a hex foreground string into its background version.

#### Signature

```python
def reverse_hex(hex_str): ...
```



## slugify

[Show source in builder.py:133](../../../base24_builder/builder.py#L133)

Format $scheme_file_name to be used as a slug variable.

#### Signature

```python
def slugify(scheme_file): ...
```