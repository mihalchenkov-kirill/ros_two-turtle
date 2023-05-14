# Установка ROS Melodic на Ubuntu 18.04
- Установите Ubuntu:18.04
- Добавьте ключи и источники ROS в Вашу систему:
    - ```sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'```
- Установите ключи:
    - ```sudo apt install curl```
    - ```curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -```
- Установите ROS Melodic:
    - ```sudo apt update```
    - ```sudo apt install ros-melodic-desktop-full```
- Инициализируйте ROS:
    - ```echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc```
    - ```source ~/.bashrc```
- Установите инструментарий для работы с пакетами:
    - ```sudo apt install python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential```
- Инициализируйте rosdep:
	- ```sudo rosdep init```
	- ```rosdep update```

# 1
