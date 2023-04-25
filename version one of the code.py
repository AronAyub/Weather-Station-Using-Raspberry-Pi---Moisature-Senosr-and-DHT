#version one of the code 


import time
import board
import adafruit_dht

# Initialize the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT22(board.D4)

# You can pass DHT22 use_pulseio=False if you wouldn't like to use pulseio.
# This may be necessary on a Linux single board computer like the Raspberry Pi,
# but it will not work in CircuitPython.
# dhtDevice = adafruit_dht.DHT22(board.D18, use_pulseio=False),
CONNECTION_STRING = "connection string here="  
MSG_SND = '{{"temperature": {temperature},"humidity": {humidity}}}'  

while True:
    def iothub_client_init():
        client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
        return client 

    def iothub_client_telemetry_sample_run():
        try:
            # Print the values to the serial port
            temperature_c = dhtDevice.temperature
            humidity = dhtDevice.humidity
            # print("Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(temperature_f, temperature_c, humidity))
            client = iothub_client_init()
            print("Sending data to IoT Hub, press Ctrl-C to exit")
            while True:  
                msg_txt_formatted = MSG_SND.format(temperature_c=temperature, humidity=humidity)  
                message = Message(msg_txt_formatted)  
                print("Sending message: {}".format(message))  
                client.send_message(message)  
                print("Message successfully sent")  
                time.sleep(3) 
        except KeyboardInterrupt:
            print("IoTHubClient stopped")
    if __name__ == '__main__':  
        print("Press Ctrl-C to exit")  
        iothub_client_telemetry_sample_run()          
  