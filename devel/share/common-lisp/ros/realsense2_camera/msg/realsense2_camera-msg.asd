
(cl:in-package :asdf)

(defsystem "realsense2_camera-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "EstimatedPose" :depends-on ("_package_EstimatedPose"))
    (:file "_package_EstimatedPose" :depends-on ("_package"))
    (:file "Extrinsics" :depends-on ("_package_Extrinsics"))
    (:file "_package_Extrinsics" :depends-on ("_package"))
    (:file "IMUInfo" :depends-on ("_package_IMUInfo"))
    (:file "_package_IMUInfo" :depends-on ("_package"))
  ))