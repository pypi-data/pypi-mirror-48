# Chronos
Utilities for parsing time strings in Python.

## Building and installation

Before installing chronos you will have to generate some of its
modules as it is explained in [Chronos readme](../readme.md)
Then, you can simply run

```
pip install bigml-chronos
```

## Requirements
Python 2.7 and Python 3 are currently supported.

The basic third-party dependencies are
[isoweek](https://pypi.org/project/isoweek/) and
[pytz](http://pytz.sourceforge.net/). These libraries are
automatically installed during the setup.

## Running the tests
The tests will be run using nose, that is installed on setup. You can
run the test suite simply by issuing

```shell
python setup.py nosetests
```

## Basic methods
There are three main methods in the **chronos** modules that you can
use:

  - With **parse_with_format** you can specify the `format_name` that
    you want to use to parse your date:

    ```python
    from chronos import parser
    parser.parse_with_format("week-date", "1969-W29-1")
    ```

  - With **parse**, you don't need to specify a `format_name`. Chronos
    will try all the possible formats until it finds the appropiate one:

    ```python
    from chronos import parser
    parser.parse("7-14-1969 5:36 PM")
    ```

  - You can also find the format_name from a date with **find_format**:

    ```python
    from chrono import parser
    parser.find_format("1969-07-14Z")
    ```

You can find all the supported formats, and an example for each one of
them inside the [test file](./chronos/tests/test_chronos.py).
