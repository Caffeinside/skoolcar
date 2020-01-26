import click

from skool_car.infrastructure.ServoMotorController import ServoMotorController
from skool_car.utils import setup_logger

logger = setup_logger()


@click.group()
def main():
    pass


@main.command(name='calibrate-car')
@click.argument('channel', type=click.Choice(['0', '1']))
@click.option('--address', type=click.STRING, default='0x40',
              help="the i2c address you'd like to calibrate [default 0x40]")
def calibrate_car(channel, address):
    """
    Script to calibrate steering or throttle of the car. Please specify a channel you'd like to calibrate [0-15]
    """
    address = int(address, 16)
    logger.info(f'Init PCA9685 on channel {channel} address {address} default bus')
    servo_motor_controller = ServoMotorController(int(channel), address=address)
    while True:
        try:
            pwm_freq = input("'Enter a PWM setting to test ('q' for quit) (0-1500):'")
            if pwm_freq.lower() == 'q':
                break
            pmw = int(pwm_freq)
            servo_motor_controller.run(pmw)
        except KeyboardInterrupt:
            logger.info("KeyboardInterrupt received, exit.")
            break
        except Exception as err:
            logger.error(err)


if __name__ == '__main__':
    main()
