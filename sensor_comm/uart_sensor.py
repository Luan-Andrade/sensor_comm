import rclpy
from rclpy.node import Node
import serial
from std_msgs.msg import String

class UARTSensor(Node):
    def __init__(self):
        super().__init__('uart_sensor')
        self.publisher_ = self.create_publisher(String, 'uart_data', 10)
        
        # Configurar a porta UART
        self.serial_port = serial.Serial('/dev/THS1', baudrate=115200, timeout=1)

        self.timer = self.create_timer(0.5, self.read_uart)

    def read_uart(self):
        if self.serial_port is not None:
            try:
                if self.serial_port.in_waiting > 0:
                    data = self.serial_port.readline().decode().strip()
                    try:
                        temperatura = float(data)  # Converte a string para float (validação e manipulação)
                        msg = String()
                        msg.data = str(temperatura) # Publica a temperatura como string
                        self.publisher_.publish(msg)
                        self.get_logger().info(f'Temperatura recebida: {temperatura}')
                    except ValueError:
                        self.get_logger().error(f'Dados UART inválidos: {data}')
            except Exception as e:
                self.get_logger().error(f'Erro UART: {e}')

def main(args=None):
    rclpy.init(args=args)
    node = UARTSensor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
