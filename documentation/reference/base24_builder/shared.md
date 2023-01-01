# Shared

> Auto-generated documentation for [base24_builder.shared](../../../base24_builder/shared.py) module.

Shared utils used by the other builder components

- [Base24-builder-python](../README.md#base24-builder-python-index) / [Modules](../MODULES.md#base24-builder-python-modules) / [Base24 Builder](index.md#base24-builder) / Shared
    - [JobOptions](#joboptions)
    - [compat_event_loop](#compat_event_loop)
    - [err_print](#err_print)
    - [get_yaml_dict](#get_yaml_dict)
    - [rel_to_cwd](#rel_to_cwd)
    - [verb_msg](#verb_msg)

## JobOptions

[[find in source code]](../../../base24_builder/shared.py#L11)

```python
class JobOptions():
    def __init__(**kwargs):
```

Container for options related to job processing

## compat_event_loop

[[find in source code]](../../../base24_builder/shared.py#L22)

```python
@contextmanager
def compat_event_loop():
```

OS agnostic context manager for an event loop.

## err_print

[[find in source code]](../../../base24_builder/shared.py#L55)

```python
def err_print(msg, exit_code=1):
```

Print $msg and exit with $exit_code.

## get_yaml_dict

[[find in source code]](../../../base24_builder/shared.py#L44)

```python
def get_yaml_dict(yaml_file):
```

Return a yaml_dict from reading yaml_file. If yaml_file is empty or
doesn't exist, return an empty dict instead.

## rel_to_cwd

[[find in source code]](../../../base24_builder/shared.py#L39)

```python
def rel_to_cwd(*args):
```

Get absolute real path of $path with $CWD as base.

## verb_msg

[[find in source code]](../../../base24_builder/shared.py#L61)

```python
def verb_msg(msg, lvl=1):
```

Print a warning ($lvl=1) or an error ($lvl=2) message.
