# Injector

> Auto-generated documentation for [base24_builder.injector](../../../base24_builder/injector.py) module.

Inject theme into a file

- [Base24-builder-python](../README.md#base24-builder-python-index) / [Modules](../MODULES.md#base24-builder-python-modules) / [Base24 Builder](index.md#base24-builder) / Injector
    - [Recipient](#recipient)
        - [Recipient().get_colorscheme](#recipientget_colorscheme)
        - [Recipient().inject_scheme](#recipientinject_scheme)
        - [Recipient().write](#recipientwrite)
    - [inject_into_files](#inject_into_files)

## Recipient

[[find in source code]](../../../base24_builder/injector.py#L13)

```python
class Recipient():
    def __init__(path):
```

Represents a file into which a base16 scheme is to be injected.

### Recipient().get_colorscheme

[[find in source code]](../../../base24_builder/injector.py#L45)

```python
def get_colorscheme(scheme_file):
```

Return a string object with the colorscheme that is to be
inserted.

### Recipient().inject_scheme

[[find in source code]](../../../base24_builder/injector.py#L67)

```python
def inject_scheme(b16_scheme):
```

Inject string $b16_scheme into self.content.

### Recipient().write

[[find in source code]](../../../base24_builder/injector.py#L90)

```python
def write():
```

Write content back to file.

## inject_into_files

[[find in source code]](../../../base24_builder/injector.py#L96)

```python
def inject_into_files(scheme, files):
```

Inject $scheme into list $files.
