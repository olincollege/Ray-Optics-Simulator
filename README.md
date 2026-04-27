# Ray Optics Simulator

## Overview
This project implements a ray optics simulation using Snell's Law. It offers a command line interface where you can specify model parameters, such as light sources and lenses, and run the simulation. 

Currently, elliptical lenses and a standard lightsource type (akin to a lightbulb) is implemented. More complex lenses and types can be approximated through proper parameterization of these objects, but this usage is not reccomended.

## Available Commands

There are four main commands that are used in running the program:

| Command | Description | Example Usage | 
|---------|-------------|---------------|
| `help` | Show help pages| `help` or `help model` |
| `model` | Initialize model parameters | `model create source standard 0 0 0.001 1` |
| `run` | Execute simulation | `run 1500` |
| `quit` | Quit the program | `quit` |

Here is a more detailed breakdown of each command:

### `help` Command

This command can be executed by itself by typing `help` or in combination with other commands such as `help model`. The `help` command on it's own gives you a brief overview of the program as well as a brief description of how to use it. When used in combination with other commands, it will give you a description of how to use the other command. i.e. entering `help run` will give you detailed information on the `run` command.

### `model` Command

The model command is used to create light sources and lenses. Each of these uses are detailed as follows with the angled brackets <> representing arguments the command requires:
 - `model create source <source_type> <x_position> <y_position> <ray_step_size> <ray_angle_step_size>`

    - `<source_type>` represents the type of source. Currently the model only supports `standard` which is a 360° point source.
    - `<x_position>` is the position of the light source on the x-axis (meters). This value should be between 0 and 2 for the light source to be on screen.
    - `<y_position>` is the position of the light source on the y-axis (meters). This value should be between -1 and 1 for the light source to be on screen.
    - `<ray_step_size>` denotes how far to step forward each ray per iteration of the simulation (meters). It is recommended to have this on the order of ~0.001
    - `<ray_angle_step_size>` defines the angle (in degrees) between each ray of the light source. Smaller angle values produce more rays and larger angle values produce fewer rays.

 - `model create lens <x_position> <y_position> <width> <height> <radius> <refraction_index>`

    - `<x_position>` is the position of the lens on the x-axis (meters). This should be between 0 and 2 for the lens to be on screen.
    - `<y_position>` is the position of the lens on the y-axis (meters). This should be between -1 and 1 for the lens to be on screen.
    - `<width>` is the horizontal width of the lens (meters) from the center of the lens to the edge i.e. 1/2 the total thickness
    - `<height>` is the vertical length of the lens (meters) from the center of the lens to the edge. Again, 1/2 the total vertical size
    - `<radius>` acts as a multiplier to the width and height. Radius must be positive. (Recommended to set this to 1)
    - `<refraction_index>` represents the the index of refraction for the lens. (Glass is around ~1.5)

`model` Examples:
  - `model create source standard 0 0 0.001 1`
  - `model create lens 1 0 0.125 0.5 1 1.5`


### `run` Command

The command `run <timesteps>` will simulate the model for a specified number of timesteps, plot the results, and save the plot as `sim_result.png` in the local directory. The command expects one argument, `<timesteps>` representing the amount of timesteps, or iterations, of the model to run. Typically `<timesteps>` is on the order of ~4000.

`run` Example:
  - `run 4000`

### `quit` Command

Running `quit` will exit the program. This wipes the current model data letting you restart from scratch.


## Installation
TBA

## Usage

Once the project files are installed the program can be used by running the `main.py` file. If you are using an IDE, open the `main.py` file in the IDE and click the run button. If you are only using command line, navigate to the directory `main.py` is in with `cd` and then run the command `python main.py`.

The program should open a command line window that has a small intro message. The command line should then display the text `Enter a command:`. Once at this stage you can begin using the program.

1. First you need to specify a few things like light sources and lenses. You can add as many light sources and lenses as you want.
   - Light sources can be specified with the command `model create source <parameters>` (Parameter descriptions [here](#model-command))
   - Lenses can be specified with the command `model create lens <parameters>` (Parameter descriptions [here](#model-command))
2. Once you are done specifying the model parameters you can run the simulation
   - Use the command `run <timesteps>` to run the simulation for a specified amount of time steps. (More info [here](#run-command))
3. The command line will show the progress of the simulation and once it has finished you may safely exit the program.
   - Use the command `quit` to exit the program
   - The resulting plot from the simulation will be stored as an image named `sim_result.png` in the current directory
   - NOTE: You may need to refresh your file viewer for the image to appear (especially if you are on Unity)

### Lens Types
TANZI

### Light Source Types
Currently the program only supports `standard` which represents a 360° point source.

### Assumptions and Limitations
If multiple lenses overlap they are considered as one continuous lens

## Attributions
This project was developed in 2026 by [Tanzi](https://github.com/Someon332), [Hayden](https://github.com/HaydenZS), and [Derek](https://github.com/derek-forgot) 
