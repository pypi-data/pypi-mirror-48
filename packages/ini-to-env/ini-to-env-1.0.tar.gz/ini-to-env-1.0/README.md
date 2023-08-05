# INI TO ENV

[![Build Status](https://travis-ci.com/MichaelKim0407/ini-to-env.svg?branch=master)](https://travis-ci.com/MichaelKim0407/ini-to-env)
[![Coverage Status](https://coveralls.io/repos/github/MichaelKim0407/ini-to-env/badge.svg?branch=master)](https://coveralls.io/github/MichaelKim0407/ini-to-env?branch=master)

Load environment variables from `.ini` files.

Author: Michael Kim <mkim0407@gmail.com>

## Installation

```bash
pip install ini-to-env
```

## Usage

`conf.ini`:

```
[default]
HELLO = WORLD

[web]
HOST = localhost
PORT = 8000
```

```python
from ini2env import load

load('conf.ini')
```

This will add `HELLO`, `HOST` and `PORT` to environment variables.

The `[section]` part doesn't matter,
but you can utilize it to organize your `.ini` file.

## `ini2env` command

The `ini2env` command will output a bash script you can then source
to export environment variables.

Run

```bash
$(ini2env ...)
```

to export the env vars directly.
