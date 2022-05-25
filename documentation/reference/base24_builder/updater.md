# Updater

> Auto-generated documentation for [base24_builder.updater](../../../base24_builder/updater.py) module.

Pull git repos and update the local schemes and templates files

- [Base24-builder-python](../README.md#base24-builder-python-index) / [Modules](../MODULES.md#base24-builder-python-modules) / [Base24 Builder](index.md#base24-builder) / Updater
    - [generate_jobs_from_yaml](#generate_jobs_from_yaml)
    - [git_clone](#git_clone)
    - [git_clone_scheduler](#git_clone_scheduler)
    - [update](#update)
    - [write_sources_file](#write_sources_file)

## generate_jobs_from_yaml

[[find in source code]](../../../base24_builder/updater.py#L62)

```python
def generate_jobs_from_yaml(yaml_file, base_dir):
```

Get a set of jobs from a yaml file

## git_clone

[[find in source code]](../../../base24_builder/updater.py#L23)

```python
async def git_clone(git_url, path, verbose=False):
```

Clone git repository at $git_url to $path. Return True if successful,
otherwise False.

## git_clone_scheduler

[[find in source code]](../../../base24_builder/updater.py#L55)

```python
async def git_clone_scheduler(yaml_file, base_dir, verbose=False):
```

Create task list for clone jobs and run them asynchronously.

## update

[[find in source code]](../../../base24_builder/updater.py#L69)

```python
def update(custom_sources=False, verbose=False):
```

Update function to be called from cli.py

## write_sources_file

[[find in source code]](../../../base24_builder/updater.py#L10)

```python
def write_sources_file():
```

Write a sources.yaml file to current working dir.
