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

The proposed Distributed Autonomous Parking Space Allocation System was designed and implemented using advanced distributed computing concepts and virtualization-based simulation techniques. The software environment was developed to simulate a real-time decentralized parking infrastructure where multiple autonomous parking nodes communicate and coordinate without relying on a centralized controller.

---

### GET Virtual Machine (GETVM)

The primary software platform used in this project is **GET Virtual Machine (GETVM)**. GETVM was utilized to create a distributed simulation environment capable of executing multiple virtual parking nodes simultaneously.

The virtual machine environment enabled:

* Distributed node deployment
* Autonomous inter-node communication
* Real-time parking slot synchronization
* Distributed parking allocation testing
* Event ordering and timestamp synchronization
* Multi-node coordination and fault analysis

Using GETVM, the proposed system successfully simulated a smart parking network in which independent parking nodes dynamically communicate and allocate parking spaces in real time. The virtualized environment provided flexibility for testing concurrent parking requests, node failures, synchronization conflicts, and distributed coordination mechanisms without requiring large-scale physical hardware deployment.

The simulation platform was also used to evaluate:

* Communication efficiency
* Distributed synchronization
* Resource allocation fairness
* Parking request handling
* System scalability
* Fault tolerance behavior

---

## Distributed Algorithms Implemented

The project integrates several advanced distributed computing algorithms to ensure reliable, synchronized, and conflict-free parking allocation across distributed parking nodes.

---

### 1. Lamport’s Logical Clock

Lamport’s Logical Clock algorithm was implemented to maintain logical event ordering among distributed parking nodes.

The algorithm was used for:

* Timestamp generation
* Event synchronization
* Ordering parking requests
* Preventing request conflicts
* Maintaining consistency across distributed nodes

Logical clocks enabled the system to correctly sequence distributed events even in the absence of synchronized physical clocks.

---

### 2. Distributed Mutual Exclusion (Ricart–Agrawala Algorithm)

The Ricart–Agrawala Distributed Mutual Exclusion algorithm was implemented to ensure that only one parking node accesses or allocates a shared parking resource at a given time.

This algorithm provided:

* Conflict-free parking allocation
* Safe distributed resource access
* Elimination of duplicate slot assignments
* Coordinated distributed decision making

The algorithm improved fairness and consistency in handling simultaneous parking requests from multiple distributed nodes.

---

### 3. Leader Election using Bully Algorithm

The Bully Algorithm was implemented for dynamic leader election among distributed parking nodes.

The elected leader node was responsible for:

* Coordinating distributed operations
* Monitoring active node availability
* Managing recovery during node failures
* Maintaining system stability

The leader election mechanism improved fault tolerance and ensured uninterrupted distributed system operation.

---

### 4. Two-Phase Commit Protocol (2PC)

The Two-Phase Commit (2PC) protocol was implemented to maintain distributed transaction consistency during parking allocation operations.

The protocol ensured:

* Reliable parking transaction confirmation
* Consistent slot updates across nodes
* Distributed agreement before final allocation
* Failure recovery support

This mechanism prevented inconsistent parking states and ensured reliable distributed synchronization.

---

### 5. Distributed Snapshot using Chandy–Lamport Algorithm

The Chandy–Lamport Distributed Snapshot algorithm was used to capture the global state of the distributed parking system during execution.

The algorithm enabled:

* Global system state monitoring
* Distributed checkpoint creation
* Fault analysis and debugging
* Performance evaluation of distributed operations

This helped analyze the real-time behavior of distributed parking nodes without interrupting system execution.

---

## Programming Environment

The software implementation was developed using:

* Python
* Linux-based distributed environment
* GETVM virtualization platform

Python was used for:

* Distributed communication logic
* Parking allocation algorithms
* Synchronization mechanisms
* Inter-node messaging
* Real-time event handling

---

## Hardware Integration

The software simulation environment was integrated with embedded hardware-oriented components including:

* Ultrasonic Sensors
* LED indicators
* Microcontroller-based parking nodes

The hardware integration enabled:

* Real-time vehicle detection
* Parking occupancy monitoring
* Slot availability indication
* Distributed parking status updates

---

## Advantages of the Software Architecture

The implemented software environment provides:

* Decentralized parking management
* High scalability
* Improved fault tolerance
* Real-time synchronization
* Distributed coordination
* Conflict-free resource allocation
* Reliable distributed communication

The virtualization-based distributed simulation successfully demonstrated the effectiveness of distributed algorithms in solving real-time smart parking allocation challenges for future smart city applications.



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
