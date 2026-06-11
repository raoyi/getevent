# getevent

Android's `getevent` utility ported to Linux. Monitors and displays raw input events from keyboards, mice, touchpads, and other input devices via the Linux input event subsystem.

## Requirements

- GCC (or a cross-compiler via `CROSS_COMPILE`)
- Python 3
- Linux kernel headers (`linux/input.h`)

## Build

```bash
sudo apt install gcc make python3 linux-libc-dev
make
```

For cross-compilation:

```bash
sudo apt install gcc-arm-linux-gnueabihf python3 gcc-arm-linux-gnueabihf
make clean && make CROSS_COMPILE=arm-linux-gnueabihf-
```

The build generates `input.h-labels.h` by running `generate-input.h-labels.py` against the system's `linux/input.h`, then compiles `getevent`.

By default, the script reads from `/usr/arm-linux-gnueabihf/include/linux/input.h`. To use a different path:

```bash
python3 generate-input.h-labels.py /usr/include/linux/input.h > input.h-labels.h
make
```

To clean build artifacts:

```bash
make clean
```

## Usage

```
getevent [-t] [-n] [-s switchmask] [-S] [-v [mask]] [-d] [-p] [-i] [-l] [-q] [-c count] [-r] [device]
```

With no arguments, monitors all devices under `/dev/input` and prints events as they occur.

### Options

| Option | Description |
|--------|-------------|
| `-t` | Show timestamps for each event |
| `-n` | Suppress newlines between events |
| `-s <mask>` | Print switch states for the given bitmask, then exit |
| `-S` | Print all switch states, then exit |
| `-v [mask]` | Set verbosity (default: device + name + info + version). Bitmask: errors=1, dev=2, name=4, info=8, version=16, possible events=32, props=64 |
| `-d` | Show HID descriptor if available |
| `-p` | Show device info and possible events, then exit |
| `-i` | Show all device info and possible events, then exit |
| `-l` | Label event types and codes in plain text |
| `-q` | Quiet mode (clear verbosity) |
| `-c <count>` | Print `count` events then exit |
| `-r` | Print event receive rate |

### Examples

Monitor all input devices:

```bash
./getevent
```

Monitor a specific device with labels:

```bash
./getevent -l /dev/input/event0
```

Show all device info and possible events:

```bash
./getevent -i
```

Capture 10 events from a device:

```bash
./getevent -c 10 /dev/input/event0
```

Show events with timestamps:

```bash
./getevent -t /dev/input/event0
```

## License

Apache License 2.0 — Copyright (C) 2015 The Android Open Source Project
