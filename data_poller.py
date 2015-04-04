from models import DB_PATH
from random import uniform
import time, dataset, datetime

SIMUL = True

if SIMUL:
    print "Simulated"

db = dataset.connect(DB_PATH)

# get a reference to the table 'user'
temp_table = db['ac_env_temp']

polling_interval = 30*60.0 # (100 requests in 3600 seconds)

poll_i = 0

def poll_ac_env_temp_sensor():
    global poll_i 
    poll_i+=1
    temp_sensor_value = uniform(8,10)
    poll_i = temp_table.insert(dict(
        poll_date=str(datetime.datetime.now()), 
        data=temp_sensor_value,
        simulated_data = SIMUL
    ))
    print ' >> poll no.', poll_i, "ac env temp: {:3.4f} degrees.".format(temp_sensor_value)


if __name__ == '__main__':
    running= True
    while running:
        start = time.clock()
        poll_ac_env_temp_sensor()
        work_duration = time.clock() - start
        time.sleep( polling_interval - work_duration )
