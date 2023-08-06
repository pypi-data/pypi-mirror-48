# AsHTTP

Super fast asynchronous HTTP client. For the future of python.

![[Build](https://travis-ci.org/gaojiuli/ashttp)](https://travis-ci.org/gaojiuli/ashttp.svg?branch=master)
[![codecov](https://codecov.io/gh/gaojiuli/ashttp/branch/master/graph/badge.svg)](https://codecov.io/gh/gaojiuli/ashttp)
![[License](https://pypi.python.org/pypi/ashttp/)](https://img.shields.io/pypi/l/ashttp.svg)
![[Pypi](https://pypi.python.org/pypi/ashttp/)](https://img.shields.io/pypi/v/ashttp.svg)
![[Python](https://pypi.python.org/pypi/ashttp/)](https://img.shields.io/pypi/pyversions/ashttp.svg)

## Installation

`pip install ashttp`

## Usage


```python
import ashttp as http

async def main():                                                                    
    r = await http.get('https://httpbin.org/get')                                                         
    print(r.status_code) # 200
    print(r.encoding) # 'ASCII' 
    print(await r.json())
    
if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_running_loop()
    loop.run_until_complete(main())
```

## Todo

- Keep-Alive & Connection Pooling
- Basic/Digest Authentication
- File Uploads