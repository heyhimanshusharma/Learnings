# FANUC Tech Transfer Structured Learning Curriculum

Compiled from the FANUC America Tech Transfer video library across all six pages of the site. The following curriculum is organized as a progressive learning path from foundational orientation to advanced integration topics. Each phase builds directly on the previous one, and skipping phases is not recommended until the prerequisites are solidly understood.

---

## Phase 1: System Orientation and Ecosystem Understanding

These videos establish the conceptual and physical foundations before any hands-on software work begins. Do not skip these, as they prevent major misunderstandings later.

1. New Naming Convention for R-50iA FANUC Robots — understand the hardware and controller nomenclature you will encounter throughout all subsequent content
2. Delta vs SCARA vs Articulated Robots — establish awareness of robot morphology and the use cases each architecture addresses
3. Cartesian vs. Joint Representation — critical conceptual foundation for all motion programming; understand how the robot sees itself in space
4. Navigating between Quick Menu and Full Menu — practical orientation for working with the Teach Pendant interface
5. FANUC Changing Batteries — maintenance and safety baseline; the first thing that goes wrong on any real cell
6. FANUC Backup and Restore Files — data protection discipline before you touch anything else on a real controller

---

## Phase 2: ROBOGUIDE Simulation Environment Setup

This phase covers the simulation software you will spend most of your time in during initial learning and customer project work.

7. FANUC ROBOGUIDE Tutorial — Robot Setup, Fixture, Parts — the definitive beginner tutorial for building your first workcell in simulation
8. ROBOGUIDE V10 New Features — understand what version you are working with and what capabilities are available
9. ROBOGUIDE V10 Highlights — path edits, Move To Panel, dynamic object linking; essential workflow tips
10. FANUC Optimizing Robot Position — use the Optimize Position Utility to place your robot correctly in the 3D layout before writing a single line of code
11. ROBOGUIDE Robot Dressout, Cables and Hoses — interference checking and cable routing simulation; prevents real-world surprises
12. FANUC ROBOGUIDE Profiler Data — learn to gather cycle time and performance data from your simulation; essential for customer proposals

---

## Phase 3: Coordinate Frames, Registers, and Teach Pendant Fundamentals

Once the simulation environment is running, learn the programming building blocks before any motion statements.

13. FANUC How to Add PR's, Frames, Registers — expanding Position Registers, Numeric Registers, User Frames, and Tool Frames via the Controlled Start Menu
14. FANUC Copy + Paste, Edit Commands in Teach Pendant Programs — Remark, Undo, Reverse Paste, and other efficiency tools for code creation
15. Search and Replace in Teach Pendant Program — essential for modifying large programs when speed, registers, or motion types need bulk changes
16. FANUC Incremental Moves — teaching points that are relative to a single starting position; fundamental for offset-based applications
17. Understanding OFFSETS in FANUC TP Code — how offsets optimize code structure across entire programs

---

## Phase 4: Motion Planning and Trajectory Control

With the environment and registers understood, progress to motion instruction details.

18. FANUC Joint vs. Linear Motion Tuning — optimize cycle time and path using linear and joint motion statements; understand CNT values and FINE termination
19. Approach and Retract Linear Distance (AP_LD & RT_LD) Introduction — guaranteeing linear approach and retract motion; critical for pick-and-place accuracy
20. Singularity — What it is and how to avoid it — identify and resolve wrist singularity in 6-axis robots before it causes production stops
21. ROBOGUIDE V10 Pick and Place — practical simulation of a pick-and-place application tying together motion, frames, and registers

---

## Phase 5: Program Logic, I/O, and Flow Control

This phase covers the decision-making and execution control structures that make programs production-capable.

22. FANUC Simulate I/O, Comment Code — force or simulate digital I/O for testing without external hardware; comment/remark code for debugging
23. Background Logic — setup and rules for background logic; runs in parallel with the main program
24. FANUC Jump Label — Jump Label and Label instruction functionality for conditional branching
25. FANUC Timers in Teach Pendant Programs — program timers for measuring robot cycle time in TP code
26. FANUC Speed Control, Override Select — controlling robot speed from external inputs such as PLCs or Ethernet IP
27. FANUC Run Command Parallel Processing — programming multiple program control simultaneously on a single controller
28. FANUC PNS and RSR — how Program Number Select and Robot Service Request work for production scheduling from external systems
29. User Alarms — setup and severity adjustment of user-defined alarms for custom fault handling
30. Argument Registers — how to use and create argument registers for modular code
31. FANUC Passing Arguments — passing variables between programs as arguments; enables modular programming architecture
32. FANUC How to use Strings — using String Registers for HMI status updates and program calls
33. FANUC Skip Function — using the SKIP instruction to handle unexpected conditions during motion
34. FANUC Touch Skip / CRX Touch Skip — Touch sensing and collision-skip logic for real-world part contact detection
35. FANUC Background Edit (Online Edit) — make program edits without stopping production; also called Online Edit

---

## Phase 6: Safety Systems

Safety must be understood before moving into any application-specific or deployment work.

36. FANUC DCS Setup (Dual Check Safety) — full overview of setting up DCS on a robot; position zones, speed checks, and tool models
37. Configuring a Restricted DCS Zone with a Speed Check — limit robot speed in designated collaborative areas using the Tablet Teach Pendant
38. DCS Working Zone Setup for CRX using Tablet TP — Working Safety Zone configuration with User Target Models for the CRX series
39. FANUC Multiple Mastering Methods — Zero Axis Mastering, Quick Mastering, Reference Position; what to do after battery loss or BZAL alarms
40. Risk Assessment Overview for Power and Force Limited Robots — ISO/TS 15066 context for collaborative applications and safety measure selection

---

## Phase 7: Tooling, End Effectors, and Payload

Real applications require accurate tooling models and payload configuration. Errors here affect path accuracy and cause overheating.

41. Payload Checker — walkthrough of the FANUC Payload Checker tool with payload tips and tricks
42. CRX Payload Setup — using the Utool Payload Setup tool included on every CRX robot
43. M-10 and M-20 Faceplate Interfaces — differences between hollow-wrist and solid-wrist variants and interface options
44. LR Mate/25 (M-20iB) Series End of Arm Tooling Cable Routing — routing cables and hoses from J3 arm connections to End of Arm Tooling
45. 13kg Payload Mode for the LR-10iA/10 — switching between payload modes and understanding operational limits
46. Angle Mounting an LR-10iA/10 — setting up the robot for angle-mount installations
47. FANUC and OnRobot Vacuum Setup — CRX-5iA and OnRobot vacuum gripper setup including key integration tricks
48. R-2000iC 300kg Software Option — configuring extended payload capability on the R-2000iC/270F

---

## Phase 8: CRX Collaborative Robot Track

If your work involves the CRX series specifically (which it does with the CRX-10iA/L), complete this track after Phase 7.

49. CRX Manual Guided Teaching — introduction to hand-guiding the CRX for point teaching
50. CRX Constant Push — setting up and troubleshooting internal force control for constant-push applications such as surface contact tasks
51. Arc Teach Icon for CRX — the ARC teaching icon for simplified arc welding programming without external devices
52. CRX Controller Software Update — updating CRX controller software via the Tablet Teach Pendant
53. CRX - Changing Batteries — battery replacement procedure specific to all CRX models

---

## Phase 9: Advanced Robot Programming Techniques

With the foundations solid and tooling configured, move into production-grade programming patterns.

54. FANUC Robot Homing Program — autonomous and safe return to home position after cycle interruption
55. FANUC Pallet Array Programming — modular programs using FOR LOOPS and one taught point for tray tending and pallet load/unload
56. FANUC Pallet Machine Tending, Using Counters — using Registers and counting math to track and offset pick positions
57. FANUC Menu Utility — setup and use of the FANUC Menu Utility option for custom operator interfaces
58. FANUC Jump Label — (revisit with more complex branching scenarios at this stage)
59. FANUC Background Edit (Online Edit) — (revisit for production-level program management)

---

## Phase 10: Material Removal — CAD-to-Path (Grinding, Deburring Context)

Directly relevant to your grinding automation proof-of-concept with the CRX-10iA/L.

60. ROBOGUIDE CAD to Path Setup Pt.1 — workcell preparation and part setup, specifically for CAD-2-PATH feature creation
61. ROBOGUIDE CAD To Path Features Pt.2 — creating features and segments from edges; edge lines and closed-loop options
62. ROBOGUIDE CAD To Path Properties Pt.3 — configuring feature and segment properties to generate and execute a TP program from CAD data

---

## Phase 11: Extended Axes and Rail Systems

For cells involving additional linear or rotary motion axes.

63. Aux Axis Motor Sizing — Three Key Elements — key criteria for selecting the right servo motor for an auxiliary axis
64. Aux Axis Software Setup for R-30iB Mini Plus Controller — installing an auxiliary axis motor on a FANUC CRX robot with the R-30iB Mini Plus
65. ROBOGUIDE Aux Axis Setup — setting up AUX axis as RTU with DCS Cartesian Position Check function
66. Robot Aux Axis Setup — Independent Axis (RTL-H895) configuration in a Dual-Arm system
67. Robot Transfer Unit (RTU) Setup — setting up and simulating FANUC's RTU in ROBOGUIDE; motor settings, travel directions, and extended axis coordination
68. FANUC 7th Axis Rail Programming — basic rules, setup, and code for programming a FANUC auxiliary rail axis
69. ROBOGUIDE Machines Conveyor and Indexer Motion — advanced techniques for creating linear or rotary machine motion within ROBOGUIDE simulations

---

## Phase 12: Palletizing Application Track

For complete palletizing cell commissioning.

70. FANUC PalletTool3 — Unit Load Creation — system setup, product configuration, and run screen operations
71. PalletTool 3 Gripper Setup — payload, UTool, and IO configuration for efficient palletizing
72. PalletTool 3 — Determining the Utool Values for Standard Grippers — setting accurate UTOOL values including Z and R offsets
73. PalletTool 3 Custom Patterns — building custom palletizing patterns with drag-and-drop layout control
74. PalletTool 3 — Run Screen — managing cycles, switching products, and operating the run screen in production
75. PalletPRO: Upload and Download Files — file transfer between robot and PalletPRO via USB backup and Ethernet
76. Palletizing Mode for CRX and Standard 6-axis Robots — enabling Palletizing Mode via Tablet TP, Manual Guided Teaching, or iPendant
77. FANUC RoboGuide Tutorial: Picking Multiple Parts Simultaneously — picking and placing multiple parts at once in RoboGuide simulation programs

---

## Phase 13: Vision — iRVision Track

Vision is a standalone discipline. Complete Phases 1 through 8 before starting here.

78. iRVision First Time Users and Tutorials — built-in guided tutorials for 2D robot-mounted and fixed camera setups
79. FANUC Lens Calculator for Vision Guided Robots — calculating field of view, camera standoff, and lens size for iRVision projects
80. iRVision 2D Lens Calculator / 3DV Field of View Determination — hardware selection for your vision application
81. iRVision — Camera Calibration — calibrating iRVision cameras for 2D and 3D setups in ROBOGUIDE
82. iRCalibration Vision Multi-Cal Introduction — Vision MultiCal for simplified multi-camera calibration and coordinated motion
83. iRVision Fixed Camera Automatic Grid Frame Set — Automatic Grid Frame setup with a fixed camera
84. iRVision Robot Mounted Camera Automatic Grid Frame Set — Automatic Grid Frame setup with a robot-mounted camera
85. iRVision — Vision Utilities Automatic Grid Frame Set — combined robot and fixed camera approach
86. iRVision Part Z Height — properly setting Part Z Height in a 2D Vision Process
87. iRVision Part Z Height & Offset Frame — mastering offset frames and Part Z height for boosted accuracy
88. iRVision Fixed Frame Offset — in-depth explanation using ROBOGUIDE, virtual cameras, and UTOOL
89. iRVision Tool Offset vs Frame Offset — describing the two offset modes with ROBOGUIDE examples
90. iRVision Frame Offset and Found Position — understanding the difference between Frame Offset and Found Position outputs
91. iRVision Setting the Reference Position — setting the reference position correctly for different applications and offset modes
92. iRVision Multiple Parts in One Picture — picking multiple parts with one vision shot using iRVision and ROBOGUIDE
93. iRVision Color Cameras — using color cameras for sorting, classification, and guidance applications
94. iRVision AI Error Proof Tool — training the AI Error Proof tool to distinguish good/bad, up/down, present/absent
95. iRVision GPM Locator G Edit Feature — manually creating edges on trained models for more consistent and accurate finds
96. iRVision Image Playback — reviewing logged images, troubleshooting vision processes, and optimizing performance
97. iRVision — Runtime (Log) Screen — new buffering function and troubleshooting using the Runtime Log Screen for R-50iA
98. iRVision Vision Override — programmatically changing parameters within any vision process at runtime
99. iRVision CXV Camera Disconnect — managing CXV camera disconnects during tool changes with key programs and best practices
100. iRVision Viewing Vision Data from Backup — backing up and viewing vision processes offline in ROBOGUIDE
101. iRPickTool Tracking Frames — tracking frame concepts, x/y/z directions, and how robots, cameras, and sensors identify conveyor origins
102. iRVision 3D Point Cloud Viewer Overview — navigating, analyzing, and optimizing 3D vision setups

---

## Phase 14: External Motion Control and ROS Integration

Directly relevant to your ROS 2 digital twin and fanuc_ros2_driver project.

103. External Motion Control Options — overview of all FANUC software options enabling external motion control; which options suit which applications
104. Remote Motion Interface — primary external motion control option; inner workings of the RMI option in depth
105. External Motion Control Using Dynamic Path Modification — real-time path adjustments using DPM via external motion control
106. Stream Motion — low-level control for external applications requiring precise path profiles; control architecture and program flow
107. PLC Motion Interface — how the PLC Motion Interface option fits into PLC-controlled system architectures
108. KAREL & User Socket Messaging — external motion control for older FANUC robots using KAREL and User Socket Messaging in tandem
109. ASCII Program Loader — sending offline-created paths to vintage and current controllers; compatible back 20+ years
110. ROS 2 Interface — FANUC's ROS 2 interface using the Remote Motion Interface and HMI Device (Modbus) options; directly applicable to the CRX-10iA/L digital twin
111. R-30iB Plus Communications Protocols — EtherNet/IP, PROFINET, EtherCAT, DeviceNet, OPC UA integration for industrial networks

---

## Phase 15: Advanced Controller Capabilities

Reserved for when the fundamentals across all prior phases are solid.

112. FANUC PAC Codes — obtaining and installing new software on the robot using the PAC Code process
113. iRProgrammer Introduction and setup for first time users — web browser programming interface without a teach pendant; no software install required
114. FANUC iRProgrammer — for SCARA Robots — the native web-browser interface on all new FANUC SCARA models
115. FANUC R-50iA Robot Controller Software PLC — Getting Started — the Software PLC option on the R-50iA using CODESYS, Operator Panel, and Process Axis Control
116. Python Programming on the R-50iA Controller — script execution, data handling, and Python integration into robotics workflows on the R-50iA

---

## Phase 16: Welding Application Track

For arc welding and spot welding applications only — complete after Phase 8 CRX track.

117. Weld Equipment Setup using Weld EQ Setup Tool Option — setting up digital weld equipment with FANUC robots using the J708 tool
118. Servo Gun Setup — initial setup of a new servo gun axis including controller configuration and axis definition
119. Servo Gun Setup — Pressure Calibration — accurate servo gun pressure calibration using FANUC's Weld Force Gauge tool
120. Servo Gun Setup Utility — optimizing servo weld guns using the FANUC Gun Setup Utility for precise, efficient welding
121. Setting Up Photoelectric Sensor for TCP — S627 TCP calibration using a photoelectric sensor including IO config and pendant setup

---

## Phase 17: Hardware-Specific One-Off References

These are reference videos to consult when specific hardware conditions arise rather than watch in sequence.

122. FANUC Multiple Mastering Methods — (revisit when a BZAL alarm or battery loss occurs in the field)
123. FANUC PAC Codes — (revisit when new software installation is required)
124. CRX Controller Software Update — (revisit during firmware update cycles)
125. ROBOGUIDE Machines Conveyor and Indexer Motion — (revisit when adding indexer or conveyor machines to an existing workcell)
126. Stainless Link B Arm Installation — DR-3iB/6 Stainless robot Link B Arm removal and installation procedure
127. SCARA Tool Flange — what the SCARA tool flange is and how to mount it on SCARA robots

---

## Recommended Usage Strategy

Work through phases sequentially and do not advance past Phase 6 before building at least one complete working simulation in ROBOGUIDE with motion, frames, and basic I/O. Application-specific tracks (Phases 10 through 16) can be pursued in parallel once Phase 9 is complete, based on the project at hand. For your current grinding automation proof-of-concept, the highest priority after Phase 9 is Phase 10 (CAD-to-Path) followed immediately by Phase 14 (ROS 2 and External Motion Control).

For the digital twin work specifically, Phase 14 is where the CRX-10iA/L and fanuc_ros2_driver integration concepts are addressed directly by FANUC's own engineers, and the ROS 2 Interface video is the single most relevant piece of content in the entire library for that project.

---

## References and Further Reading

FANUC America Tech Transfer Platform
https://techtransfer.fanucamerica.com

FANUC CRX Series Official Product Page
https://www.fanucamerica.com/products/robots/collaborative-robots/crx-series

FANUC R-30iB Plus Controller Operator Manual (B-83284EN)
Available via MyFANUC portal at https://www.fanucamerica.com/home/my-fanuc

FANUC Robot Series Operator's Manual for Handling (B-83284EN-1)
Available via MyFANUC

fanuc_ros2_driver — Official ROS 2 Driver for FANUC Robots
https://github.com/ros-industrial/fanuc_ros2_driver

ROS 2 MoveIt 2 Documentation
https://moveit.ros.org/documentation/

ISO 10218-1:2011 — Robots and Robotic Devices: Safety Requirements for Industrial Robots
International Organization for Standardization

ISO/TS 15066:2016 — Robots and Robotic Devices: Collaborative Robots
Applicable specifically to CRX power-and-force-limited operation

Siciliano, B., Sciavicco, L., Villani, L., & Oriolo, G. (2009). Robotics: Modelling, Planning and Control. Springer. — Foundational textbook for kinematics, trajectory planning, and singularity analysis

Craig, J. J. (2005). Introduction to Robotics: Mechanics and Control (3rd ed.). Pearson Prentice Hall. — Standard reference for coordinate frames, homogeneous transforms, and Denavit-Hartenberg parameters

Niku, S. B. (2020). Introduction to Robotics: Analysis, Control, Applications (3rd ed.). Wiley. — Approachable reference for robot workspace, motion planning, and end effector design

ROS Industrial Consortium Documentation and Tutorials
https://rosindustrial.org/

FANUC Academy Training Programs (Hands-on complement to Tech Transfer self-study)
https://www.fanucamerica.com/training/classes

Corke, P. (2017). Robotics, Vision and Control: Fundamental Algorithms in MATLAB (2nd ed.). Springer. — Excellent reference for iRVision conceptual foundations, camera calibration mathematics, and vision-guided robot control