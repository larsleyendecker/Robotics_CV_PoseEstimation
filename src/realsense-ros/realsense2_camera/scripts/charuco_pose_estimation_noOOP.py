#!/usr/bin/env python

import os
import numpy
import cv2
from cv_bridge import CvBridge
from cv_bridge.boost.cv_bridge_boost import getCvType

import rospy
from sensor_msgs.msg import Image, CameraInfo
from realsense2_camera.msg import EstimatedPose

def create_charuco_board(config):
    '''Creates and returns a charuco board with the given configuration'''
    return cv2.aruco.CharucoBoard_create(config["squaresX"], config["squaresY"], config["squareLength"], config["markerLength"], config["dictionary"])

def charuco_pose_estimation(cv_image):
    '''Does the pose estimation using the charuco board (chessboard + aruco marker) in the given configuration'''
    corners, ids, _ = cv2.aruco.detectMarkers(cv_image, charuco_config["dictionary"], parameters=params)
    if ids is not None:
        _, charuco_corners, charuco_ids = cv2.aruco.interpolateCornersCharuco(corners, ids, cv_image, charuco_board, minMarkers=1)
        cv2.aruco.drawDetectedCornersCharuco(cv_image, charuco_corners, charuco_ids)
        retval, rotation_vector, translation_vector = cv2.aruco.estimatePoseCharucoBoard(charuco_corners, charuco_ids, charuco_board, camera_matrix, distortion_coefficients, None, None)
        if retval == True:
            cv2.aruco.drawAxis(cv_image, camera_matrix, distortion_coefficients, rotation_vector, translation_vector, 0.03)
            cv2.imshow("Charuco", cv_image)
            return translation_vector, rotation_vector
        else:
            cv2.imshow("Charuco", cv_image)
            return numpy.zeros(3), numpy.zeros(3)
    else:
        cv2.imshow("Charuco, cv_image")
        return numpy.zeros(3), numpy.zeros(3)

def image_callback(ros_image):
    '''Callback function for the subscription of the ROS topic /camera/color/image_raw (sensor_msgs Image)'''
    global bridge
    cv_image = bridge.imgmsg_to_cv2(ros_image, "bgr8")
    tvec, rvec = charuco_pose_estimation(cv_image)
    publish_pose(tvec, rvec)
    cv2.waitKey(1)

def calibration_callback(data):
    '''Sets the calibration parameters - camera_matrix and distortion_coefficients - by reading the ROS topic /camera/color/cameraInfo'''
    global camera_matrix
    global distortion_coefficients
    camera_matrix = numpy.array(data.K).reshape(3,3)
    distortion_coefficients = numpy.array(data.D).reshape(5,)

def run_ros_node():
    '''Initialize the ROS node and setting up Subscriptions and Publishers'''
    rospy.init_node("aruco_estimator", anonymous=True)
    rospy.Subscriber("/camera/color/image_raw", Image, image_callback)
    rospy.Subscriber("/camera/color/CameraInfo", CameraInfo, calibration_callback)
    rate = rospy.Rate(30)

def publish_pose(tvec, rvec):
    '''Publishes the estimated pose from the charuco board to a ROS topic'''
    command = EstimatedPose()
    command.tx = tvec[0]
    command.ty = tvec[1]
    command.tz = tvec[2]
    command.rx = rvec[0]
    command.ry = rvec[1]
    command.rz = rvec[2]
    pose_publisher.publish(command)

def main():
    '''Initializing ROS node (Subscriptions + Publications) and fullfilling the pose estimation'''
    global bridge
    global charuco_config
    global params
    global pose_publisher
    global charuco_board

    bridge = CvBridge()
    charuco_config = {
        "squaresX" : 5,
        "squaresY" : 5,
        "squareLength" : 0.0115,
        "markerLength" : 0.008,
        "dictionary" : cv2.aruco.Dictionary_get(cv2.aruco.DICT_7X7_50)
    }
    charuco_board = create_charuco_board(charuco_config)
    params = cv2.aruco.DetectorParameters_create()

    rospy.init_node("charuco_estimator", anonymous=True)
    rospy.Subscriber("/camera/color/image_raw", Image, image_callback)
    rospy.Subscriber("/camera/color/camera_info", CameraInfo, calibration_callback)
    pose_publisher = rospy.Publisher("/pose_estimation", EstimatedPose, queue_size=1)
    rate = rospy.Rate(30)

    while True:
        rospy.spin()

if __name__ == "__main__":
    main()

