# SEIKA Mikrosystemtechnik GmbH - Software Module

**This python package allows you to communicate with your SEIKA sensor and make basic measurements.**

##Usage of SEIKA python module:
1. Donwload current version (e.g. with pip)
2. Type: `import seika` - submodules will be imported automatically
3. Choose the program and function you want to run (e.g. program *GetAngle* and function *read_sensor*: `seika.GetAngle.read_sensor()`

##Programs and functions
###GetAngle: 
- ``read_sensor(port,address)`` - returns continous angle readings from your sensor with address ``address`` connected to port ``port``
- ``read_sensor_to_file(filename,nreadings,port,address)`` - writes a pre-defined number (``nreadings``) of readings to your file with name ``filename``
- ``search_sensor(port)`` - searches for sensors and returns a list with addresses

