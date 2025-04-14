#Inference_node.py

import rclpy
from rclpy.node import Node
import tensorflow as tf
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

class InferenceNode(Node):
    def __init__(self):
        super().__init__('inference_node')
        self.bridge = CvBridge()

        # 모델 로딩 (export된 SavedModel 폴더)
        self.model = tf.saved_model.load("/home/ubuntu/model/saved_model")

        self.subscription = self.create_subscription(
            Image,
            '/camera/image_raw',
            self.image_callback,
            10
        )

    def image_callback(self, msg):
        cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='rgb8')
        input_tensor = self.preprocess(cv_image)

        # 추론
        action = self.model(input_tensor)
        self.get_logger().info(f"Inference 결과: {action}")

    def preprocess(self, image):
        image_resized = tf.image.resize(image, [120, 160])  # 입력 사이즈 맞춤
        input_tensor = tf.expand_dims(image_resized / 255.0, axis=0)  # 정규화
        return tf.convert_to_tensor(input_tensor, dtype=tf.float32)

def main(args=None):
    rclpy.init(args=args)
    node = InferenceNode()
    rclpy.spin(node)
    rclpy.shutdown()
