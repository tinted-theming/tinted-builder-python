# Injector

[Base24-builder-python Index](../README.md#base24-builder-python-index) /
[Base24 Builder](./index.md#base24-builder) /
Injector

> Auto-generated documentation for [base24_builder.injector](../../../base24_builder/injector.py) module.

- [Injector](#injector)
  - [Recipient](#recipient)
    - [Recipient().get_colorscheme](#recipient()get_colorscheme)
    - [Recipient().inject_scheme](#recipient()inject_scheme)
    - [Recipient().write](#recipient()write)
  - [inject_into_files](#inject_into_files)

## Recipient

[Show source in injector.py:13](../../../base24_builder/injector.py#L13)

Represents a file into which a base16 scheme is to be injected.

#### Signature

```python
class Recipient:
    def __init__(self, path):
        ...
```

### Recipient().get_colorscheme

[Show source in injector.py:45](../../../base24_builder/injector.py#L45)

Return a string object with the colorscheme that is to be
inserted.

#### Signature

```python
def get_colorscheme(self, scheme_file):
    ...
```

### Recipient().inject_scheme

[Show source in injector.py:67](../../../base24_builder/injector.py#L67)

Inject string $b16_scheme into self.content.

#### Signature

```python
def inject_scheme(self, b16_scheme):
    ...
```

### Recipient().write

[Show source in injector.py:90](../../../base24_builder/injector.py#L90)

Write content back to file.

#### Signature

```python
def write(self):
    ...
```



## inject_into_files

[Show source in injector.py:96](../../../base24_builder/injector.py#L96)

Inject $scheme into list $files.

#### Signature

```python
def inject_into_files(scheme, files):
    ...
```


