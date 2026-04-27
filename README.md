# Ray Optics Simulator

## Overview
This project implements a ray optics simulation using Snell's Law. It offers a command line interface where you can specify model parameters, such as light sources and lenses, and run the simulation. 

Currently, elliptical lenses and a standard lightsource type (akin to a lightbulb) is implemented. More complex lenses and types can be approximated through proper parameterization of these objects, but this usage is not reccomended.

### Available Commands

| Command | Description | Example Usage | 
|---------|-------------|---------------|
| `help` | Show help pages| `help` or `help model` |
| `model` | Initialize model parameters | `model create source standard 0 0 0.001 1` |
| `run` | Execute simulation | `run 1500` |
| `quit` | Quit the program | `quit` |

## Installation
TBA
