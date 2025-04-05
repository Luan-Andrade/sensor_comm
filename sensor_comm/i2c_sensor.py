import rclpy
from rclpy.node import Node
import smbus2
import time
from std_msgs.msg import Float32

class I2CSensor(Node):
    def __init__(self):
        super().__init__('i2c_sensor')
        self.publisher_temp = self.create_publisher(Float32, 'temperature', 10)
        self.publisher_humidity = self.create_publisher(Float32, 'humidity', 10)
        self.bus = smbus2.SMBus(1)  # I2C-1
        self.addr = 0x76  # Endereço do BME280

        self.timer = self.create_timer(1.0, self.read_sensor)
    
    def read_sensor(self):
        try:
            # Lendo dados brutos (exemplo simplificado)
            data = self.bus.read_i2c_block_data(self.addr, 0x88, 6)
            temp = data[0] + (data[1] << 8)
            humidity = data[3] + (data[4] << 8)

            # Publicando no ROS 2
            temp_msg = Float32()
            temp_msg.data = temp / 100.0  # Conversão para Celsius
            self.publisher_temp.publish(temp_msg)

            humidity_msg = Float32()
            humidity_msg.data = humidity / 100.0  # Conversão para %
            self.publisher_humidity.publish(humidity_msg)

            self.get_logger().info(f'Temperatura: {temp_msg.data}°C, Umidade: {humidity_msg.data}%')

        except Exception as e:
            self.get_logger().error(f'Erro ao ler o sensor I2C: {e}')

def main(args=None):
    rclpy.init(args=args)
    node = I2CSensor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
