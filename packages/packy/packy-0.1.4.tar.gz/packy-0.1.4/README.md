# 📦 Packy

[![Build Status](https://travis-ci.org/codetent/packy.svg?branch=master)](https://travis-ci.org/codetent/packy)

## What is packy?
Packy is a simple package manager working like pip which allows downloading packages from content delivery providers like cdnjs.

## How does it work?

1. Install it via pip:

    ```bash
    pip install packy
    ```

2. Install packages

    ```bash
    # Latest version
    packy jquery
    # Specific version
    packy jquery==3.2
    # Version range
    packy jquery>=2.0

    # Install from packages.txt (syntax like requirements.txt)
    packy -r packages.txt

    # Set CD provider
    packy -p cdnjs ...
    
    # Set installation directory
    packy -o ./static/ ...
    ```

## 🔧 API
Additionally, packy can be used directly with Python:

```python
from packy import Packy

packy.install('jquery')
```
