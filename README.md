# sw_competition_aws

# 🚗 DeepRacer + Adaptive AUTOSAR Integration

This project is part of the 2025 Embedded Software Contest (임베디드SW경진대회), Autonomous Racing Track by Daehyeon Lee, Seohyun Park, Yeonju Gwen from AESLAB of TU Korea

## 🔧 Project Overview
ROS2-based sensor processing and AI inference combined with Adaptive AUTOSAR AA module for vehicle control.

### 🔗 Architecture Overview
1. Camera/LiDAR → ROS2 (Python)
2. Inference (TensorFlow model or rule-based)
3. ROS2 → Adaptive AUTOSAR AA (C++)
4. Control → `/cmd_vel` to AWS DeepRacer

## 🛠 Technologies Used
- ROS2 Foxy
- TensorFlow (AWS DeepRacer pretrained model)
- Python 3.8
- Adaptive AUTOSAR R20-11
- C++14
- popcornSAR (planned)

## 📁 Repository Structure
```bash
deepracer-autosar-race/
├── ros2_ws/              # ROS2 inference node
├── autosar_aa/           # Adaptive AUTOSAR C++ Application
├── docs/                 # Reports and documentation
├── scripts/              # Optional setup helpers

![aws1](https://github.com/user-attachments/assets/4b383946-e030-4538-a964-7eca2073c8e7)


## 🏁 Getting Started

```bash
# Clone & build ROS2 node
cd ros2_ws
colcon build
source install/setup.bash

# Run inference node
ros2 run inference_node inference_node
```

