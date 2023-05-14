# Презентация работы

![https://imgur.com/a8efdsT]


# Клонирование готового репозитория и запуск проекта

Клонируем репозиторий:

```git clone https://github.com/mihalchenkov-kirill/ros_two-turtle.git```

Переходим в репозиторий:

```cd ros_two-turtle```

Инициализируем среду:

```rm -rf build```

```catkin_make```

```source devel/setup.bash```

Запускаем лаун-файл:

```roslaunch turtle_follower turtle_follower.launch```

Если не работает то:

```roslaunch src/turtle_follower/launch/turtle_follower.launch```

# Установка ROS Melodic на Ubuntu:18.04

1. Установите последнюю версию Ubuntu: 18.04 или 20.04.
2. Добавьте ключи и источники ROS в Вашу систему:

	```sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'```

3. Установите ключи:

	```sudo apt install curl```
	
	```curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -```

4. Установите ROS Melodic:

	```sudo apt update```

	```sudo apt install ros-melodic-desktop-full```

5. Инициализируйте ROS:

	```echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc```

	```source ~/.bashrc```

6. Установите инструментарий для работы с пакетами:

	```sudo apt install python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential```

7. Инициализируйте rosdep:

	```sudo rosdep init```
	
	```rosdep update```
