from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'sensor_comm'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')), #Adicione esta linha
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='luan',
    maintainer_email='luan@todo.todo',
    description='TODO: Package description',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        	'i2c_sensor = sensor_comm.i2c_sensor:main',
        	'uart_sensor = sensor_comm.uart_sensor:main',
        ],
    },
)
