# Cli

[Base24-builder-python Index](../README.md#base24-builder-python-index) /
[Base24 Builder](./index.md#base24-builder) /
Cli

> Auto-generated documentation for [base24_builder.cli](../../../base24_builder/cli.py) module.

- [Cli](#cli)
  - [build_mode](#build_mode)
  - [catch_keyboard_interrupt](#catch_keyboard_interrupt)
  - [inject_mode](#inject_mode)
  - [run](#run)
  - [update_mode](#update_mode)

## build_mode

[Show source in cli.py:21](../../../base24_builder/cli.py#L21)

Check command line arguments and run build function.

#### Signature

```python
@catch_keyboard_interrupt
def build_mode(arg_namespace): ...
```

#### See also

- [catch_keyboard_interrupt](#catch_keyboard_interrupt)



## catch_keyboard_interrupt

[Show source in cli.py:9](../../../base24_builder/cli.py#L9)

Decorator for catching KeyboardInterrupt and quitting gracefully.

#### Signature

```python
def catch_keyboard_interrupt(func): ...
```



## inject_mode

[Show source in cli.py:42](../../../base24_builder/cli.py#L42)

Check command line arguments and run build function.

#### Signature

```python
@catch_keyboard_interrupt
def inject_mode(arg_namespace): ...
```

#### See also

- [catch_keyboard_interrupt](#catch_keyboard_interrupt)



## run

[Show source in cli.py:79](../../../base24_builder/cli.py#L79)

Run the program

#### Signature

```python
def run(): ...
```



## update_mode

[Show source in cli.py:61](../../../base24_builder/cli.py#L61)

Check command line arguments and run update function.

#### Signature

```python
@catch_keyboard_interrupt
def update_mode(arg_namespace): ...
```

#### See also

- [catch_keyboard_interrupt](#catch_keyboard_interrupt)