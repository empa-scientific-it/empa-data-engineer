# Data management system optimization

We have software to keep track of any activities labs are doing in their research, and we keep a history of the actions that each lab performs. Each lab is composed of several groups. We want to see how active groups are to optimize available resources.

- Instance → lab
- Space → mechanism to partition an instance and manage permissions
- An instance can host multiple groups
- One instance runs on a separate virtual machine (VM)
- We pay each VM
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
