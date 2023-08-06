import subprocess
from pibot.leds import check_leds

from time import sleep
from pibot.nano import Nano
from pibot.lcd import LCD

def startup():
    lcd = LCD(fontsize=16)
    leds.init_leds()

    #check LEDs
    check_leds()

    # show TU-Chemnitz logo on screen
    lcd.view_image("/home/pi/.resources/tu.pgm", 1)

    sleep(2)
    # show TU-Chemnitz text on screen
    lcd.view_image("/home/pi/.resources/tutext.pgm", 1)

    sleep(2)
    # show Roboschool logo on screen
    lcd.view_image("/home/pi/.resources/roboschool.pgm", 1)

    sleep(2)
    # show PiBot logo on screen
    lcd.view_image("/home/pi/.resources/pibot.pgm", 1)

    # check LEDs
    check_leds()

    # getting IP
    cmd = "hostname -I | cut -d\' \' -f1"
    ip = (subprocess.check_output(cmd, shell=True)).decode("utf-8")

    # getting voltage
    nano = Nano()
    voltage = nano.get_battery_voltage()

    text = "IP: " + str(ip), "Battery: {} mV".format(voltage)
    lcd.print(text)
    sleep(2)
