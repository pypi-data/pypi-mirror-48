# Overview

Super fast asynchronous HTTP client. I can't wait The requests 3.0. So I create one.

## Installation

`pip install ashttp`

## Usage

```python
import asyncio
from ashttp import *

async def main():
    await get('https://httpbin.org/get')
    await post('https://httpbin.org/post', data=json.dumps({"a": 1}))
    await put('https://httpbin.org/put', data=json.dumps({"a": 1}))
    await patch('https://httpbin.org/patch', data=json.dumps({"a": 1}))
    await delete('https://httpbin.org/delete')
    await option('https://httpbin.org/option')
    
asyncio.run(main())
```

## Todo

- Keep-Alive & Connection Pooling
- Basic/Digest Authentication
- File Uploads