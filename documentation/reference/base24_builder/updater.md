# Updater

[Base24-builder-python Index](../README.md#base24-builder-python-index) /
[Base24 Builder](./index.md#base24-builder) /
Updater

> Auto-generated documentation for [base24_builder.updater](../../../base24_builder/updater.py) module.

- [Updater](#updater)
  - [generate_jobs_from_yaml](#generate_jobs_from_yaml)
  - [git_clone](#git_clone)
  - [git_clone_scheduler](#git_clone_scheduler)
  - [update](#update)
  - [write_sources_file](#write_sources_file)

## generate_jobs_from_yaml

[Show source in updater.py:62](../../../base24_builder/updater.py#L62)

Get a set of jobs from a yaml file

#### Signature

```python
def generate_jobs_from_yaml(yaml_file, base_dir):
    ...
```



## git_clone

[Show source in updater.py:23](../../../base24_builder/updater.py#L23)

Clone git repository at $git_url to $path. Return True if successful,
otherwise False.

#### Signature

```python
async def git_clone(git_url, path, verbose=False):
    ...
```



## git_clone_scheduler

[Show source in updater.py:55](../../../base24_builder/updater.py#L55)

Create task list for clone jobs and run them asynchronously.

#### Signature

```python
async def git_clone_scheduler(yaml_file, base_dir, verbose=False):
    ...
```



## update

[Show source in updater.py:69](../../../base24_builder/updater.py#L69)

Update function to be called from cli.py

#### Signature

```python
def update(custom_sources=False, verbose=False):
    ...
```



## write_sources_file

[Show source in updater.py:10](../../../base24_builder/updater.py#L10)

Write a sources.yaml file to current working dir.

#### Signature

```python
def write_sources_file():
    ...
```


