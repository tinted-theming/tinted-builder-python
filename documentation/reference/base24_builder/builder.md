# Builder

> Auto-generated documentation for [base24_builder.builder](../../../base24_builder/builder.py) module.

Combine schemes and templates to generate user-ready themes

- [Base24-builder-python](../README.md#base24-builder-python-index) / [Modules](../MODULES.md#base24-builder-python-modules) / [Base24 Builder](index.md#base24-builder) / Builder
    - [TemplateGroup](#templategroup)
        - [TemplateGroup().get_templates](#templategroupget_templates)
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

[[find in source code]](../../../base24_builder/builder.py#L12)

```python
class TemplateGroup():
    def __init__(base_path):
```

Representation of a template group, i.e. a group of templates specified
in a config.yaml.

### TemplateGroup().get_templates

[[find in source code]](../../../base24_builder/builder.py#L21)

```python
def get_templates():
```

Return a list of template_dicts based on the config.yaml in
$self.base_path. Keys correspond to templates and values represent
further settings regarding each template. A pystache object containing
the parsed corresponding mustache file is added to the sub-dictionary.

## build

[[find in source code]](../../../base24_builder/builder.py#L201)

```python
def build(templates=None, schemes=None, base_output_dir=None, verbose=False):
```

Main build function to initiate building process.

## build_scheduler

[[find in source code]](../../../base24_builder/builder.py#L195)

```python
async def build_scheduler(scheme_files, job_options):
```

Create a task list from scheme_files and run tasks asynchronously.

## build_single

[[find in source code]](../../../base24_builder/builder.py#L141)

```python
async def build_single(scheme_file, job_options):
```

Build colorscheme from $scheme_file using $job_options. Return True if
completed without warnings. Otherwise false.

## build_single_task

[[find in source code]](../../../base24_builder/builder.py#L185)

```python
async def build_single_task(scheme_file, job_options):
```

Worker thread for picking up scheme files from $queue and building b16
templates using $templates until it receives None.

## format_scheme

[[find in source code]](../../../base24_builder/builder.py#L87)

```python
def format_scheme(scheme, slug):
```

Change $scheme so it can be applied to a template.

## get_parent_dir

[[find in source code]](../../../base24_builder/builder.py#L36)

```python
def get_parent_dir(base_dir, level=1):
```

Get the directory $level levels above $base_dir.

## get_pystache_parsed

[[find in source code]](../../../base24_builder/builder.py#L44)

```python
def get_pystache_parsed(mustache_file):
```

Return a ParsedTemplate instance based on the contents of
$mustache_file.

## get_scheme_dirs

[[find in source code]](../../../base24_builder/builder.py#L60)

```python
def get_scheme_dirs():
```

Return a set of all scheme directories.

## get_scheme_files

[[find in source code]](../../../base24_builder/builder.py#L68)

```python
def get_scheme_files(patterns=None):
```

Return a list of all (or those matching $pattern) yaml (scheme)
files.

## get_template_dirs

[[find in source code]](../../../base24_builder/builder.py#L52)

```python
def get_template_dirs():
```

Return a set of all template directories.

## reverse_hex

[[find in source code]](../../../base24_builder/builder.py#L81)

```python
def reverse_hex(hex_str):
```

Reverse a hex foreground string into its background version.

## slugify

[[find in source code]](../../../base24_builder/builder.py#L133)

```python
def slugify(scheme_file):
```

Format $scheme_file_name to be used as a slug variable.
