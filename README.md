# MineBannerLib

Python library for drawing banners.

## How it works?

Draws a banner image from the received nbts. The flag will be saved to the _**buildbanner**_ root folder.

## Installation

```
pip install minebannerlib
```

or

```
python -m pip install minebannerlib
```

## Create a banner

To do this, call the `create_banner()` function, to which you need to pass the _**NBTS**_, _**name of the flag**_ and the _**base color**_

## Example

```python
from MineBannerLib import CreateBanner

banner = CreateBanner

nbts = '{BlockEntityTag:{Patterns:[{Color:14,Pattern:"cre"},{Color:4,Pattern:"sku"}]}}'
color_base = 15
name = 'test'

def main():
  banner.create_banner(name, nbts, color_base)

if __name__ == '__main__':
  main()
```
