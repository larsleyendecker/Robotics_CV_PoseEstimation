// Auto-generated. Do not edit!

// (in-package realsense2_camera.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class EstimatedPose {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.tx = null;
      this.ty = null;
      this.tz = null;
      this.rx = null;
      this.ry = null;
      this.rz = null;
    }
    else {
      if (initObj.hasOwnProperty('tx')) {
        this.tx = initObj.tx
      }
      else {
        this.tx = 0.0;
      }
      if (initObj.hasOwnProperty('ty')) {
        this.ty = initObj.ty
      }
      else {
        this.ty = 0.0;
      }
      if (initObj.hasOwnProperty('tz')) {
        this.tz = initObj.tz
      }
      else {
        this.tz = 0.0;
      }
      if (initObj.hasOwnProperty('rx')) {
        this.rx = initObj.rx
      }
      else {
        this.rx = 0.0;
      }
      if (initObj.hasOwnProperty('ry')) {
        this.ry = initObj.ry
      }
      else {
        this.ry = 0.0;
      }
      if (initObj.hasOwnProperty('rz')) {
        this.rz = initObj.rz
      }
      else {
        this.rz = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type EstimatedPose
    // Serialize message field [tx]
    bufferOffset = _serializer.float64(obj.tx, buffer, bufferOffset);
    // Serialize message field [ty]
    bufferOffset = _serializer.float64(obj.ty, buffer, bufferOffset);
    // Serialize message field [tz]
    bufferOffset = _serializer.float64(obj.tz, buffer, bufferOffset);
    // Serialize message field [rx]
    bufferOffset = _serializer.float64(obj.rx, buffer, bufferOffset);
    // Serialize message field [ry]
    bufferOffset = _serializer.float64(obj.ry, buffer, bufferOffset);
    // Serialize message field [rz]
    bufferOffset = _serializer.float64(obj.rz, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type EstimatedPose
    let len;
    let data = new EstimatedPose(null);
    // Deserialize message field [tx]
    data.tx = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [ty]
    data.ty = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [tz]
    data.tz = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [rx]
    data.rx = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [ry]
    data.ry = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [rz]
    data.rz = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 48;
  }

  static datatype() {
    // Returns string type for a message object
    return 'realsense2_camera/EstimatedPose';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'e46dd9c8f4990ebb7cf2458b8e07e095';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float64 tx
    float64 ty
    float64 tz
    float64 rx
    float64 ry
    float64 rz 
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new EstimatedPose(null);
    if (msg.tx !== undefined) {
      resolved.tx = msg.tx;
    }
    else {
      resolved.tx = 0.0
    }

    if (msg.ty !== undefined) {
      resolved.ty = msg.ty;
    }
    else {
      resolved.ty = 0.0
    }

    if (msg.tz !== undefined) {
      resolved.tz = msg.tz;
    }
    else {
      resolved.tz = 0.0
    }

    if (msg.rx !== undefined) {
      resolved.rx = msg.rx;
    }
    else {
      resolved.rx = 0.0
    }

    if (msg.ry !== undefined) {
      resolved.ry = msg.ry;
    }
    else {
      resolved.ry = 0.0
    }

    if (msg.rz !== undefined) {
      resolved.rz = msg.rz;
    }
    else {
      resolved.rz = 0.0
    }

    return resolved;
    }
};

module.exports = EstimatedPose;
