# MineBannerLib

Python library for drawing banners.

## How it works?

Draws a banner image from the received nbts. The flag will be saved to the _**buildbanner**_ root folder.

## Installation

```
pip install minebannerlin
```

or

```
python -m pip install minebannerlib
```

## Create a banner

To do this, call the `create_banner()` function, to which you need to pass the _**NBTS**_ and the _**name of the flag**_

## Example

```python
from minebannerlib import CreateBanner

def main()
  create_banner('test', '{BlockEntityTag:{Patterns:[{Color:14,Pattern:"cre"},{Color:4,Pattern:"sku"}]}}'

if __name__ == '__main__':
  main()
```
