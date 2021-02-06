class Mqtt:
    ADDRESS = '192.168.0.164'
    PORT = 1883
    USERNAME = 'karol'
    PASSWORD = 'klapeczki'
    TOPIC = 'microphones/master_bedroom/bed'
    ERROR_TOPIC = 'errors/microphones/master_bedroom/bed/'
    STATE_TOPIC = TOPIC + 'state'


class Messages:
    TURN_OFF = 'turn_off'
    TURN_ON = 'turn_on'
    STATE = 'state'
