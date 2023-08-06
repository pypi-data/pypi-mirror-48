# kFPGA
[![Build Status](https://jenkins.slaanesh.org/job/kfpga/badge/icon)](https://jenkins.slaanesh.org/job/kfpga/)

kFPGA is an opensource platform for creating and programming FPGA cores.

## Installation
### Using pip
```
python3 -m pip install kfpga
```
### From source
```
git clone https://git.slaanesh.org/killruana/kfpga.git
python3 kfpga/setup.py install
```


## Usage
### Creating a new kFPGA core
First, create the kFPGA core
```
kfpga-creator createcore \
    --width 5 \
    --height 5 \
    --io 4 \
    --clocks 1 \
    --sets 1 \
    --resets 1 \
    --enables 1 \
    --interconnect_width 10 \
    --le 4 \
    --lut 4 \
    kFPGADemoCore 
```

Then, you can generate the RTL of the core like this
```
kfpga-creator generatertl \
    kFPGADemoCore/kFPGADemoCore.kcp
```

### Implementation
kFPGA cores can be implemented on FPGA for testing purpose, as an ASIC or integrated in a SoC.

TODO

### Programming
kFPGA cores are programmed with the `kfpga-programmer` command

TODO

## Architecture
Currently, the architecture of kFPGA core is very simple: only LUTs and interconnect. The following functionalities are planned:
* DSP blocks
* memory blocks
* carry chain
* support for generated clock, set, reset and enable signals