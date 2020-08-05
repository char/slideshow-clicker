# Slideshow Clicker

A quick-and-dirty LAN slideshow clicker designed for Linux hosts and smartphone clients.

Requires [xdotool](https://www.semicomplete.com/projects/xdotool/) on your PATH.

## Usage

```
$ pipenv shell
[pipenv] $ pipenv install # Install dependencies
[pipenv] $ python3 slideshow_clicker.py # You can also set the PORT env var
Listening at http://0.0.0.0:8000/
```

1. Open a web browser on the client smartphone, and navigate to the host device's IP with the specified port.
2. Just tap to emulate a spacebar press.
