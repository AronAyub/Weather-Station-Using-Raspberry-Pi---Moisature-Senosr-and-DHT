# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT
#The latest library 
import time
import board
import adafruit_dht

from azure.iot.device import IoTHubDeviceClient, Message 

# Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT22(board.D4)

# you can pass DHT22 use_pulseio=False if you wouldn't like to use pulseio.
# This may be necessary on a Linux single board computer like the Raspberry Pi,
# but it will not work in CircuitPython.
# dhtDevice = adafruit_dht.DHT22(board.D18, use_pulseio=False)

#IoT Hub connection String 
CONNECTION_STRING = "your connection string here"  
MSG_SND = '{{"temperature": {temperature},"humidity": {humidity}}}'  

# reading temperature and humidity 
while True:
    temperature = dhtDevice.temperature
    humidity = dhtDevice.humidity
    def iothub_client_init():
        client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
        return client  
    def iothub_client_telemetry_sample_run():
        try:
            client = iothub_client_init()
            print ( "Sending data to IoT Hub, press Ctrl-C to exit" )
            while True:
                msg_txt_formatted = MSG_SND.format(temperature=temperature, humidity=humidity)  
                message = Message(msg_txt_formatted)  
                print( "Sending message: {}".format(message) )  
                client.send_message(message)  
                print ( "Message successfully sent" )
                time.sleep(3) 
                # Errors happen fairly often, DHT's are hard to read, just keep going
        # except RuntimeError as error:
        #     print(error.args[0])
        #     time.sleep(2.0)
        #     continue
        except Exception as error:
            dhtDevice.exit()
            raise error
        except KeyboardInterrupt:  
            print ( "IoTHubClient stopped" )  
    if __name__ == '__main__':  
        print ( "Press Ctrl-C to exit" )  
        iothub_client_telemetry_sample_run()
