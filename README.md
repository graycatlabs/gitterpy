# gitterpy

[https://github.com/graycatlabs/gitterpy](https://github.com/graycatlabs/gitterpy)

Copyright (c) 2015 - Gray Cat Labs, Alex Hiam <alex@graycat.io>

gitterpy is a Python client API for the [Gitter](https://gitter.im) web chat platform.

It uses the [Gitter REST API](https://developer.gitter.im/docs/rest-api).

# Installation

To install, first clone the repository:

    $ git clone https://github.com/graycatlabs/gitterpy.git

Then install the Python module:

    $ sudo python setup.py install

# Usage

Once installed, you can import the `gitterpy` module into your Python script and instantiate a `Gitter` object with your Gitter auth token:

```python
import gitterpy
gitter_token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
gitter = gitterpy.Gitter(gitter_token)
```
You can find your Gitter token by logging into [https://developer.gitter.im/login](https://developer.gitter.im/login).

More docs coming soon... for now check out the function docs for the [Gitter class](https://github.com/graycatlabs/gitterpy/tree/master/gitterpy/gitterpy.py).

# License

gitterpy is licensed under the MIT license.

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
    THE SOFTWARE.
