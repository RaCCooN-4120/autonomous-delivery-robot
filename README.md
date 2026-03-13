# 🤖 Autonomous Delivery Robot (ROS2 + Web Control)

Autonomous Delivery Robot is a **ROS2-based robot navigation system** integrated with a **web interface** for controlling delivery destinations inside a simulated environment.

This project demonstrates how a mobile robot can autonomously navigate between multiple rooms using **TurtleBot3**, **Gazebo Simulation**, and **Navigation2**, while users control the robot through a simple **web dashboard**.

The system is designed as an **educational robotics project** for studying autonomous navigation, robot control, and human-robot interaction.

---

# 🧠 System Overview

The system consists of four main components:

1. **Gazebo Simulation**
2. **ROS2 Navigation2**
3. **Web Control Interface**
4. **Robot Goal Publisher**

The user selects a destination room from the web page, and the robot will autonomously navigate to that location using the ROS2 navigation stack.

---

# 🏗 System Architecture

User → Web Browser → Flask Web Server → ROS2 Goal Publisher → Navigation2 → Robot Movement in Gazebo

---

# 🧰 Technologies Used

* ROS2 Humble
* TurtleBot3
* Gazebo Simulator
* Navigation2 (Nav2)
* Python
* Flask
* HTML / JavaScript

---

# 📁 Project Structure

```
autonomous-delivery-robot
│
├── map
│   ├── map.yaml
│   └── map.pgm
│
├── delivery_ws
│   └── src
│       └── delivery_robot
│           ├── delivery_robot
│           │   └── web_server.py
│           ├── package.xml
│           └── setup.py
│
└── web
    └── templates
        └── index.html
```

---

# 🗺 Delivery Locations

The robot can navigate to **6 different rooms**:

| Room | Coordinate (x,y) |
| ---- | ---------------- |
| A    | (13.0, -0.15)    |
| B    | (12.2, 2.0)      |
| C    | (8.0, 4.3)       |
| D    | (4.3, 2.16)      |
| E    | (0.97, 4.0)      |
| F    | (0.703, 0.716)   |

These coordinates correspond to locations in the navigation map.

---

# 🚀 Installation

## 1 Clone Repository

```
git clone https://github.com/RaCCooN-4120/autonomous-delivery-robot.git
cd autonomous-delivery-robot
```

---

## 2 Build ROS2 Workspace

```
cd delivery_ws
colcon build
source install/setup.bash
```

---

## 3 Install Python Dependency

```
pip install flask
```

---

# ▶ Running the System

## Terminal 1 — Launch Gazebo Simulation

```
export TURTLEBOT3_MODEL=burger
ros2 launch turtlebot3_gazebo turtlebot3_house.launch.py
```

---

## Terminal 2 — Launch Navigation2

```
ros2 launch turtlebot3_navigation2 navigation2.launch.py \
use_sim_time:=True \
map:=$HOME/autonomous-delivery-robot/map/map.yaml
```

---

## Terminal 3 — Start Web Server

```
python3 ~/autonomous-delivery-robot/delivery_ws/src/delivery_robot/delivery_robot/web_server.py
```

Server will start at

```
http://localhost:5000
```

---

# 🌐 Web Control Interface

Open your browser and go to

```
http://localhost:5000
```

You will see the **Autonomous Delivery Robot dashboard** where you can select a room.

Available buttons:

Room A
Room B
Room C
Room D
Room E
Room F

When a room is selected, the robot will navigate to that location.

---

# 📸 Example Interface

Autonomous Delivery Robot
Select Room

[ Room A ]
[ Room B ]
[ Room C ]
[ Room D ]
[ Room E ]
[ Room F ]

---

# 🎯 Project Objectives

* Demonstrate **autonomous navigation with ROS2**
* Integrate **robotics with web technologies**
* Provide a **simple human-robot interface**
* Study **mobile robot navigation in indoor environments**

---

# 🔬 Future Improvements

Possible improvements for this project:

* Real robot deployment (TurtleBot3)
* Obstacle detection and dynamic replanning
* Real-time robot position display on web
* Camera streaming
* Database for delivery tasks
* Multi-robot coordination

---

# 👨‍💻 Author

Rawi Thongsong
Robotics and Mechatronics Engineering

---

# 📄 License

This project is for **educational and research purposes**.
