# ROS_exercise1
This is my first simple exercise on how to create a publisher and subscriber node in ROS package. To know more about ROS👇

# Robot Operating System (ROS)
An open-source middleware package for robotics is called Robot Operating System (ROS). While not an operating system (OS), ROS is a collection of software frameworks for the creation of robot software. As such, it offers services like hardware abstraction, low-level device control, the implementation of frequently used functionality, message-passing between processes, and package management that are intended for a heterogeneous computer cluster. A graph architecture is used to describe the running sets of ROS-based processes, with processing taking place in nodes that can receive, post, and multiplex messages relating to control, state, planning, actuators, and other topics.

http://wiki.ros.org/ROS/Tutorials

# Problem Statement of exercise1
1. Create two nodes. Create two topics named informer1 and informer2. Let one node publish these two topics into another node.

2. Create three nodes starter, middleman and getter. Let starter publish a integer data randomly in the range [-100,100] in a topic. Middle man publishes another topic called relay that relays data only if starter's topic sends message with a positive integer. Getter subscribes to relay topic and prints content.

starter-------------->middleman-------->getter

3. Observe the nodes, topics using ros command line tools.
