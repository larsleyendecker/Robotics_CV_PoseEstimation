#!/usr/bin/env python

import os
import numpy
import cv2
import json
from cv_bridge import CvBridge
from cv_bridge.boost.cv_bridge_boost import getCvType

import rospy
from sensor_msgs.msg import Image, CameraInfo
from realsense2_camera.msg import EstimatedPose

class PoseEstimator:

    def __init__(self):
        with open("charuco_config.json") as config_file:
            self.charuco_config = json.load(config_file)
        self.charuco_config["dictionary"] = cv2.aruco.Dictionary_get(cv2.aruco.DICT_7X7_50)
        self.bridge = CvBridge()
        self.charuco_board = self.create_charuco_board(self.charuco_config)
        self.params = cv2.aruco.DetectorParameters_create()
        rospy.Subscriber("/camera/color/image_raw", Image, self.image_callback)
        rospy.Subscriber("camera/color/camera_info", CameraInfo, self.calibration_callback)
        self.pose_publisher = rospy.Publisher("/pose_estimation", EstimatedPose, queue_size=1)
        self.rate = rospy.Rate(30)

    def create_charuco_board(self, config):
        '''Creates and returns a charuco board with the given configuration'''
        return cv2.aruco.CharucoBoard_create(config["squaresX"], config["squaresY"], config["squareLength"], config["markerLength"], config["dictionary"])

    def charuco_pose_estimation(self, cv_image):
        '''Does the pose estimation using the charuco board (chessboard + aruco marker) in the given configuration'''
        corners, ids, _ = cv2.aruco.detectMarkers(cv_image, self.charuco_config["dictionary"], parameters=self.params)
        if ids is not None:
            _, charuco_corners, charuco_ids = cv2.aruco.interpolateCornersCharuco(corners, ids, cv_image, self.charuco_board, minMarkers=1)
            cv2.aruco.drawDetectedCornersCharuco(cv_image, charuco_corners, charuco_ids)
            retval, rotation_vector, translation_vector = cv2.aruco.estimatePoseCharucoBoard(charuco_corners, charuco_ids, self.charuco_board, self.camera_matrix, self.distortion_coefficients, None, None)
            if retval == True:
                cv2.aruco.drawAxis(cv_image, self.camera_matrix, self.distortion_coefficients, rotation_vector, translation_vector, 0.03)
                cv2.imshow("Charuco", cv_image)
                return translation_vector, rotation_vector
            else:
                cv2.imshow("Charuco", cv_image)
                return numpy.zeros(3), numpy.zeros(3)
        else:
            cv2.imshow("Charuco, cv_image")
            return numpy.zeros(3), numpy.zeros(3)

    def image_callback(self, ros_image):
        '''Callback function for the subscription of the ROS topic /camera/color/image_raw (sensor_msgs Image)'''
        cv_image = self.bridge.imgmsg_to_cv2(ros_image, "bgr8")
        tvec, rvec = self.charuco_pose_estimation(cv_image)
        self.publish_pose(tvec, rvec)
        cv2.waitKey(1)

    def calibration_callback(self, data):
        '''Sets the calibration parameters - camera_matrix and distortion_coefficients - by reading the ROS topic /camera/color/cameraInfo'''
        self.camera_matrix = numpy.array(data.K).reshape(3,3)
        self.distortion_coefficients = numpy.array(data.D).reshape(5,)

    def publish_pose(self, tvec, rvec):
        '''Publishes the estimated pose from the charuco board to a ROS topic'''
        command = EstimatedPose()
        command.tx = tvec[0]
        command.ty = tvec[1]
        command.tz = tvec[2]
        command.rx = rvec[0]
        command.ry = rvec[1]
        command.rz = rvec[2]
        self.pose_publisher.publish(command)

if __name__ == "__main__":
    rospy.init_node("charuco_estimator", anonymous=True)
    PoseEstimator()
    rospy.spin()