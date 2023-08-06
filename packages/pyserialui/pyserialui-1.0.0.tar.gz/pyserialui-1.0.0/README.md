# PySerialUI

Support and examples for Python SerialUI callbacks, overrides and functionality.

### SerialUI, Device Druid and Builder

SerialUI provides a user-defined set of menus, commands, inputs, tracked states and data views through a serial channel (e.g. USB or bluetooth LE serial), for embedded and Linux devices (Arduino, Raspberry Pi, etc).

It also includes a programatic API to allow clients, such as [device druid](https://devicedruid.com/), to create and manage the SerialUI menu items while providing any desirable interface such as a GUI.

The [Device Druid Builder](https://devicedruid.com/builder/) is the easiest way to define the SerialUI menu structure and will generate projects that use the SerialUI library and implement your layout.

### Python

On embedded devices, functionality is implemented by fleshing out the various callbacks in C++.

On Linux hosts, such as [Raspberry Pi](https://www.raspberrypi.org/) or [Ubuntu](https://ubuntu.com/), Python may be used instead thanks to the built-in CPython support and (optionally) this library.

### Copyright and License
PySerialUI is 
Copyright (C) 2019 Pat Deegan, [psychogenic.com](https://psychogenic.com/)
and is released under the terms of the LGPLv3.  See the LICENSE file for details.

More information is available through the [device druid](https://devicedruid.com/) and [inductive-kickback](https://inductive-kickback.com/) websites.

