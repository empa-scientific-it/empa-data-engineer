# Case study for the interview at Empa Scientific IT

## Data management system optimization

We have a software to keep track of any activities labs are doing in their research, and we keep a history of the actions that each lab performs. Each lab is composed of several groups. We want to see how active groups are to optimize available resources.

The configuration of the software is as follows:

- Each lab receives an *instance* of the software
- One *instance* runs on a separate virtual machine (VM)
- Each instance can be divided into *spaces*. Spaces are mechanism to partition an instance and manage permissions
- Currently, each group in a lab is assigned a different space
- We pay each VM. The cost is composed as follows
  - Fixed costs: keep the VM always running
  - Variable costs: depending on usage (CPUs + Storage)

### Notes

- Spaces are a mechanism to partition an instance and manage permissions
- Instance usage:
  - total number of entities/instance (each space will be billed independently)
  - number of operations performed with entity over a certain time period
- The assignment of instances to labs and spaces to groups can be changed anytime

### Questions

- Are we spending too much on instances?
- Who is causing more costs?
- How do you find out?
- Is the VM usage balanced?
- How can we change this configuration to reduce costs?

Check out a visual description of the setup [here on Excalidraw](https://excalidraw.com/#room=2cdf2c6b3adacc791f87,Sryi25ej9XVRyLyeFiRgFQ)
