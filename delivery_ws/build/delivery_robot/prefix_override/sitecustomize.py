import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/raccoon/autonomous-delivery-robot/delivery_ws/install/delivery_robot'
