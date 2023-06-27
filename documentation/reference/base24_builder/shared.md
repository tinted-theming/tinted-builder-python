# Shared

[Base24-builder-python Index](../README.md#base24-builder-python-index) /
[Base24 Builder](./index.md#base24-builder) /
Shared

> Auto-generated documentation for [base24_builder.shared](../../../base24_builder/shared.py) module.

- [Shared](#shared)
  - [JobOptions](#joboptions)
  - [compat_event_loop](#compat_event_loop)
  - [err_print](#err_print)
  - [get_yaml_dict](#get_yaml_dict)
  - [rel_to_cwd](#rel_to_cwd)
  - [verb_msg](#verb_msg)

## JobOptions

[Show source in shared.py:11](../../../base24_builder/shared.py#L11)

Container for options related to job processing

#### Signature

```python
class JobOptions:
    def __init__(self, **kwargs):
        ...
```



## compat_event_loop

[Show source in shared.py:22](../../../base24_builder/shared.py#L22)

OS agnostic context manager for an event loop.

#### Signature

```python
@contextmanager
def compat_event_loop():
    ...
```



## err_print

[Show source in shared.py:55](../../../base24_builder/shared.py#L55)

Print $msg and exit with $exit_code.

#### Signature

```python
def err_print(msg, exit_code=1):
    ...
```



## get_yaml_dict

[Show source in shared.py:44](../../../base24_builder/shared.py#L44)

Return a yaml_dict from reading yaml_file. If yaml_file is empty or
doesn't exist, return an empty dict instead.

#### Signature

```python
def get_yaml_dict(yaml_file):
    ...
```



## rel_to_cwd

[Show source in shared.py:39](../../../base24_builder/shared.py#L39)

Get absolute real path of $path with $CWD as base.

#### Signature

```python
def rel_to_cwd(*args):
    ...
```



## verb_msg

[Show source in shared.py:61](../../../base24_builder/shared.py#L61)

Print a warning ($lvl=1) or an error ($lvl=2) message.

#### Signature

```python
def verb_msg(msg, lvl=1):
    ...
```


