import board
import busio
import adafruit_bme280
import adafruit_ccs811
import time

# Initialize I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Initialize BME280 sensor
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

# Initialize CCS811 sensor
ccs811 = adafruit_ccs811.CCS811(i2c)

# Function to read sensor data
def read_sensor_data():
    temperature = bme280.temperature
    humidity = bme280.humidity
    pressure = bme280.pressure
    co2 = ccs811.eco2
    tvoc = ccs811.tvoc
    return temperature, humidity, pressure, co2, tvoc

# Main loop
while True:
    temperature, humidity, pressure, co2, tvoc = read_sensor_data()
    print("Temperature: {} C".format(temperature))
    print("Humidity: {}%".format(humidity))
    print("Pressure: {} hPa".format(pressure))
    print("CO2: {} ppm".format(co2))
    print("TVOC: {} ppb".format(tvoc))
    time.sleep(1)
