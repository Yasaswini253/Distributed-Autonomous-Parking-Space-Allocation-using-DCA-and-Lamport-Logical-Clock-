# Distributed Autonomous Parking Space Allocation using DCA and Lamport Logical Clock

## Project Overview

This project presents a **Distributed Autonomous Parking Space Allocation System** designed for smart city environments using principles of Distributed Computing. The system eliminates the dependency on centralized parking management by enabling autonomous parking nodes to communicate, coordinate, and allocate parking spaces collaboratively in real time.

The proposed architecture integrates:

* Distributed Coordination Algorithm (DCA)
* Lamport Logical Clock
* Ultrasonic Sensors
* Wireless Node Communication
* Real-Time Parking Slot Monitoring

The system ensures fair and conflict-free parking allocation while improving scalability, fault tolerance, and overall parking efficiency.

---

## Problem Statement

Traditional parking systems rely heavily on centralized servers for slot management and allocation. These systems suffer from:

* Single point of failure
* Communication delays
* Scalability limitations
* Poor real-time responsiveness
* Increased congestion and waiting time

This project addresses these limitations by implementing a decentralized distributed parking allocation framework capable of making intelligent local decisions without centralized control.

---

## Proposed Solution

The proposed system treats each parking area as an independent distributed node. Every node maintains:

* Parking slot availability
* Request queue
* Logical clock synchronization
* Local allocation decisions

Nodes communicate with neighboring nodes to coordinate parking allocation efficiently.

The system uses:

* **DCA (Distributed Coordination Algorithm)** for distributed decision-making
* **Lamport Logical Clock** for maintaining event ordering and avoiding allocation conflicts

This enables:

* Fair parking allocation
* Conflict-free slot assignment
* Reduced waiting time
* Improved scalability

---

## System Architecture

The system consists of three major layers:

### 1. Sensing Layer

* Ultrasonic sensors detect vehicle presence
* Real-time occupancy monitoring

### 2. Processing Layer

* Embedded node-level decision making
* DCA-based parking allocation logic
* Lamport timestamp synchronization

### 3. Communication Layer

* Wireless communication between parking nodes
* Distributed coordination without central controller

---

## Hardware Components

* Ultrasonic Sensor
* LED Indicators
* Microcontroller (Arduino / Embedded Controller)
* Wireless Communication Modules

### LED Status Indication

* ON → Parking slot occupied
* OFF → Parking slot available

---

## Methodology

The complete workflow of the system includes:

1. System initialization of distributed parking nodes
2. Vehicle parking request generation
3. Timestamp assignment using Lamport Logical Clock
4. Distributed communication between nodes
5. Conflict-free parking slot allocation
6. Real-time slot update and synchronization
7. Parking slot release and reallocation
8. Performance evaluation and analysis

---

## Software and Simulation Environment

The proposed Distributed Autonomous Parking Space Allocation System was developed and tested using multiple software tools and distributed computing concepts to simulate real-time parking coordination among autonomous nodes.

### GET Virtual Machine (GETVM)

A major software platform used in this project is **GET Virtual Machine (GETVM)**. GETVM was used to create a simulated distributed environment where multiple parking nodes operate independently and communicate with each other in real time.

The virtual machine environment enabled:

* Distributed node execution
* Inter-node communication testing
* Simulation of parking request handling
* Validation of Distributed Coordination Algorithm (DCA)
* Synchronization using Lamport Logical Clock
* Conflict-free parking slot allocation

Using GETVM, multiple virtual parking nodes were executed simultaneously to replicate a real-world distributed smart parking infrastructure. The environment helped in analyzing:

* Communication efficiency
* Allocation delay
* Request synchronization
* Distributed coordination performance
* Scalability of the proposed architecture

The virtualized setup also provided flexibility for testing node failures, simultaneous parking requests, and dynamic parking slot updates without requiring large-scale physical hardware deployment.

---

### Programming Environment

The project logic and communication modules were implemented using:

* **Python** – for distributed node communication, parking allocation logic, and synchronization mechanisms
* **Linux-based Environment** – for executing distributed node simulations inside GETVM

---

### Distributed Computing Concepts Used

The project integrates several distributed system concepts including:

* Distributed Coordination Algorithm (DCA)
* Lamport Logical Clock
* Distributed Event Ordering
* Autonomous Node Communication
* Decentralized Resource Allocation

These concepts enabled the implementation of a scalable and fault-tolerant parking allocation system suitable for smart city applications.

---

### Hardware Integration

The software environment was integrated with hardware-oriented simulation components such as:

* Ultrasonic Sensors for vehicle detection
* LED indicators for slot availability
* Microcontroller-based node processing

The integration between software simulation and hardware logic allowed real-time monitoring and autonomous parking management operations.


## Features

* Distributed autonomous parking allocation
* Conflict-free slot assignment
* Real-time parking monitoring
* Fair request handling using logical clocks
* Reduced waiting time
* Scalable distributed architecture
* Smart city compatible solution
* Decentralized coordination mechanism

---

## Tools and Technologies

### Software

* Python
* Distributed Computing Concepts
* GetVM / Linux Environment

### Concepts Used

* Distributed Coordination Algorithm (DCA)
* Lamport Logical Clock
* Distributed Systems
* Smart Parking Systems
* Wireless Node Communication

---

## Results and Analysis

The proposed system demonstrated:

* Efficient communication between distributed parking nodes
* Accurate vehicle detection using ultrasonic sensors
* Fair allocation during simultaneous parking requests
* Reduced parking allocation delay
* Improved system responsiveness
* Better scalability compared to centralized systems

The implementation successfully prevented:

* Duplicate slot allocation
* Request conflicts
* Allocation inconsistencies

---

## Advantages

* Eliminates centralized dependency
* Reduces parking congestion
* Improves resource utilization
* Supports large-scale deployment
* Enhances fault tolerance
* Suitable for smart city infrastructure

---

## Future Scope

Future improvements may include:

* Integration with IoT cloud platforms
* Mobile application support
* Real-time GPS-based parking navigation
* AI-based traffic prediction
* Deployment using Raspberry Pi and edge devices
* Smart reservation and priority parking systems

---

## Conclusion

This project demonstrates an efficient and scalable distributed parking allocation framework using DCA and Lamport Logical Clock mechanisms. By enabling autonomous node-level coordination, the system achieves reliable, fair, and real-time parking management suitable for next-generation smart transportation infrastructure.
