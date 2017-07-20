# dmenu-docker

A script to launch docker container with dmenu.


### Requirements

In order to use dmenu-docker you need the following requirements.

- docker
- docker-py (for Python 3)
- Python 3
- dmenu


### Usage

If you fulfill all of the requirements, just run `./dmenu-docker.py` and you're done :tada:.
Then you're able to see all of your docker containers and which of them are running.

If you select a running container, it will be stopped with docker(similar to `docker stop`).


If you select a non-running container, the container and all linked containers
will be started with docker(similar to `docker stop` except it starts all the linked containers).


### Customization

To customize the appearance of dmenu or the dmenu-executable, edit `src/dmenu.sh`.

**Warning:** Please bear in mind that I use my own [dmenu-fork](https://github.com/dj95/dmenu2). Some of the arguments
may not work for your dmenu.


### License

MIT/X Consortium License

(c) 2017 Daniel Jankowski

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
