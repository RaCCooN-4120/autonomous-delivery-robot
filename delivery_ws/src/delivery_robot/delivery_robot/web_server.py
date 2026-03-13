from flask import Flask, render_template
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
import threading
import time

app = Flask(__name__, template_folder='../../../../web/templates')

rooms = {
"A": (13.0,-0.15),
"B": (12.2,2.0),
"C": (8.0,4.3),
"D": (4.3,2.16),
"E": (0.97,4.0),
"F": (0.703,0.716)
}

class GoalNode(Node):

    def __init__(self):
        super().__init__('web_goal_sender')
        self.pub = self.create_publisher(PoseStamped,'/goal_pose',10)

    def send_goal(self,x,y):

        goal=PoseStamped()

        goal.header.frame_id="map"
        goal.header.stamp=self.get_clock().now().to_msg()

        goal.pose.position.x=x
        goal.pose.position.y=y
        goal.pose.orientation.w=1.0

        for _ in range(5):
            self.pub.publish(goal)
            time.sleep(0.3)

        print("Robot going to",x,y)

rclpy.init()
node=GoalNode()

def ros_spin():
    rclpy.spin(node)

threading.Thread(target=ros_spin).start()

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/go/<room>')
def go_room(room):

    if room in rooms:
        x,y=rooms[room]
        node.send_goal(x,y)
        return f"Robot going to Room {room}"

    return "Room not found"

app.run(host='0.0.0.0',port=5000)
