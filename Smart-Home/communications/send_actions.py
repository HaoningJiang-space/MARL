import serial

def send_actions(ser, parsed_actions):
    """Send a list of actions to the Arduino."""
    try:
        for action in parsed_actions:
            ser.write(action.encode('utf-8'))
            ser.write(b'\n')
            ser.flush()
        ser.close()
    except KeyboardInterrupt:
        ser.close()

def get_ser(port, baudrate):
    """Get a serial object."""
    ser = serial.Serial(port, baudrate)
    if ser.isOpen():
        print('Serial is open!')
    else:
        print('Serial is not open!')
    return ser

if __name__ == '__main__':
    ser = get_ser('/dev/ttyACM0', 9600)
    send_actions(ser, ['1', '2', '3', '4', '5'])