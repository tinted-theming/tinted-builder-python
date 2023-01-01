# Cli

> Auto-generated documentation for [base24_builder.cli](../../../base24_builder/cli.py) module.

CLI entry point

- [Base24-builder-python](../README.md#base24-builder-python-index) / [Modules](../MODULES.md#base24-builder-python-modules) / [Base24 Builder](index.md#base24-builder) / Cli
    - [build_mode](#build_mode)
    - [catch_keyboard_interrupt](#catch_keyboard_interrupt)
    - [inject_mode](#inject_mode)
    - [run](#run)
    - [update_mode](#update_mode)

## build_mode

[[find in source code]](../../../base24_builder/cli.py#L21)

```python
@catch_keyboard_interrupt
def build_mode(arg_namespace):
```

Check command line arguments and run build function.

#### See also

- [catch_keyboard_interrupt](#catch_keyboard_interrupt)

## catch_keyboard_interrupt

[[find in source code]](../../../base24_builder/cli.py#L9)

```python
def catch_keyboard_interrupt(func):
```

Decorator for catching KeyboardInterrupt and quitting gracefully.

## inject_mode

[[find in source code]](../../../base24_builder/cli.py#L42)

```python
@catch_keyboard_interrupt
def inject_mode(arg_namespace):
```

Check command line arguments and run build function.

#### See also

- [catch_keyboard_interrupt](#catch_keyboard_interrupt)

## run

[[find in source code]](../../../base24_builder/cli.py#L79)

```python
def run():
```

Run the program

## update_mode

[[find in source code]](../../../base24_builder/cli.py#L61)

```python
@catch_keyboard_interrupt
def update_mode(arg_namespace):
```

Check command line arguments and run update function.

#### See also

- [catch_keyboard_interrupt](#catch_keyboard_interrupt)
