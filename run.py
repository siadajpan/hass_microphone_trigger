import logging
import os
import time
from datetime import datetime

from mqtt_utils.message_manager import MessageManager
from mqtt_utils.messages.mqtt_message import MQTTMessage

from hass_microphone_trigger.settings import settings

if __name__ == '__main__':
    now = datetime.now()
    datetime_str = now.strftime("%Y_%m_%d__%H_%M_%S")
    logs_path ='/home/karol/Projects/hass_microphone_trigger/logs'
    if not os.path.exists(logs_path):
        os.mkdir(logs_path)

    logging.basicConfig(filename=f'{logs_path}/{datetime_str}.log',
                        filemode='a',
                        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                        datefmt='%H:%M:%S',
                        level=logging.DEBUG)

    logging.info('Starting lights controller')

    logging.info('Starting mqtt client')

    logging.info('Starting message manager')
    messages = [MQTTMessage('topic')]
    message_manager = MessageManager(messages)
    message_manager.connect(settings.Mqtt.ADDRESS, settings.Mqtt.PORT)
    message_manager.start()
    try:
        while True:
            time.sleep(100)
    except KeyboardInterrupt:
        message_manager.stop()
