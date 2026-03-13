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
## Dont for got run 2D pose estimate in navigation (ห้ามลืมสำคัญ)
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

# and we will got two local 
local one can open on your notebook
local two can open on your phone just copy localhost and sent to home massage and open it, it can be use
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


# 👨‍💻 Author

Rawi Thongsong
Robotics and Mechatronics Engineering
Contact me via instagram: cn.rwts

---

# 📄 License

This project is for **educational and research purposes**.
