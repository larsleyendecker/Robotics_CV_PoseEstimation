;; Auto-generated. Do not edit!


(when (boundp 'realsense2_camera::Pose)
  (if (not (find-package "REALSENSE2_CAMERA"))
    (make-package "REALSENSE2_CAMERA"))
  (shadow 'Pose (find-package "REALSENSE2_CAMERA")))
(unless (find-package "REALSENSE2_CAMERA::POSE")
  (make-package "REALSENSE2_CAMERA::POSE"))

(in-package "ROS")
;;//! \htmlinclude Pose.msg.html


(defclass realsense2_camera::Pose
  :super ros::object
  :slots (_tx _ty _tz _rx _ry _rz ))

(defmethod realsense2_camera::Pose
  (:init
   (&key
    ((:tx __tx) 0.0)
    ((:ty __ty) 0.0)
    ((:tz __tz) 0.0)
    ((:rx __rx) 0.0)
    ((:ry __ry) 0.0)
    ((:rz __rz) 0.0)
    )
   (send-super :init)
   (setq _tx (float __tx))
   (setq _ty (float __ty))
   (setq _tz (float __tz))
   (setq _rx (float __rx))
   (setq _ry (float __ry))
   (setq _rz (float __rz))
   self)
  (:tx
   (&optional __tx)
   (if __tx (setq _tx __tx)) _tx)
  (:ty
   (&optional __ty)
   (if __ty (setq _ty __ty)) _ty)
  (:tz
   (&optional __tz)
   (if __tz (setq _tz __tz)) _tz)
  (:rx
   (&optional __rx)
   (if __rx (setq _rx __rx)) _rx)
  (:ry
   (&optional __ry)
   (if __ry (setq _ry __ry)) _ry)
  (:rz
   (&optional __rz)
   (if __rz (setq _rz __rz)) _rz)
  (:serialization-length
   ()
   (+
    ;; float64 _tx
    8
    ;; float64 _ty
    8
    ;; float64 _tz
    8
    ;; float64 _rx
    8
    ;; float64 _ry
    8
    ;; float64 _rz
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _tx
       (sys::poke _tx (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _ty
       (sys::poke _ty (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _tz
       (sys::poke _tz (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _rx
       (sys::poke _rx (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _ry
       (sys::poke _ry (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _rz
       (sys::poke _rz (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _tx
     (setq _tx (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _ty
     (setq _ty (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _tz
     (setq _tz (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _rx
     (setq _rx (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _ry
     (setq _ry (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _rz
     (setq _rz (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get realsense2_camera::Pose :md5sum-) "e46dd9c8f4990ebb7cf2458b8e07e095")
(setf (get realsense2_camera::Pose :datatype-) "realsense2_camera/Pose")
(setf (get realsense2_camera::Pose :definition-)
      "float64 tx
float64 ty
float64 tz
float64 rx
float64 ry
float64 rz 


")



(provide :realsense2_camera/Pose "e46dd9c8f4990ebb7cf2458b8e07e095")


