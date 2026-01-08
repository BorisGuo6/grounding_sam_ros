#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Image
from grounding_sam_ros.client import SamDetector
from cv_bridge import CvBridge

if __name__ == '__main__':
    rospy.init_node('detection_module')
    cv_bridge = CvBridge()
    while not rospy.is_shutdown():
        rate = rospy.Rate(1)  # 1 Hz
        rgb_image = rospy.wait_for_message('/camera/color/image_raw', Image) 
        rgb = cv_bridge.imgmsg_to_cv2(rgb_image, desired_encoding='bgr8')

        text_prompt ='hammer'
        detector = SamDetector()
        annotated_frame, boxes, masks, labels, scores = detector.detect(rgb, text_prompt)

        print(annotated_frame, boxes, masks, labels, scores)
        rate.sleep()
