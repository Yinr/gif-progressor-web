# Gif Progressor Web

![license](https://img.shields.io/github/license/Yinr/gif-progressor-web?style=flat-square)
![Docker-Build](https://github.com/Yinr/gif-progressor-web/workflows/Docker/badge.svg)

Web server of [GifProgressor](https://github.com/cycoe/Gif-Progressor).

## Discription

A web application to add progress bar to a GIF file.

## Examples

![Example 1](./static/eg1.gif)

## Usage

1. Download the source code

    ```bash
    git clone --recurse-submodules https://github.com/Yinr/gif-progressor-web.git

    ## with older versions of git(<2.13), try the following
    git clone https://github.com/Yinr/gif-progressor-web.git
    cd gif-progressor-web
    git submodule update --init --recursive
    ```

2. Build Docker image

    ```bash
    docker-compose build
    ```

3. Run docker compose

    ```bash
    docker-compose up
    ```

4. Goto <http://127.0.0.1/> and enjoy

## Demo

<https://gif.yinr.cc/>

## License

MIT License

## Thanks to

[Layui](https://layui.com)
