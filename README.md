## **Kai Python Package**

#### KAI Gesture Controller

<img src="https://thenextbigproject.com/wp-content/uploads/2020/10/kai-red-band.jpeg" width="50%" >

#### InMoov Right Hand

<img src="https://thenextbigproject.com/wp-content/uploads/2020/10/right-hand-5-finger.jpeg" width="50%" >

More details and Updates on the project MYRO - Using KAI, refer: https://thenextbigproject.com/myro-2-0/

#### **Setup**

Run the following commands to initialise the project directory

```
python3 setup.py build
python3 setup.py install
```

#### **Module Initialisation**

a. Make sure the **moduleId** and **moduleSecret** are defined correcty in your program.

```python
moduleID = "moduleName"     # Name can be anything
moduleSecret = "qwerty"
```
 
b. Connect to the KaiSDK Websocket.
```python
module = WebSocketModule()
success = module.connect(moduleID, moduleSecret)
```

#### **Accessing Data**

#### **Set Capabilities**

```python
module.setCapabilities(module.DefaultKai, KaiCapabilities.AccelerometerData | KaiCapabilities.GyroscopeData | KaiCapabilities.PYRData)
```

#### **Set Listeners**

```python
def accelerometerEv(ev):
    print(ev.accelerometer.x)
    print(ev.accelerometer.y)
    print(ev.accelerometer.z)

module.DefaultKai.register_event_listener(Events.AccelerometerEvent, accelerometerEv)
```

#### **Unset Capabilities**

```python
module.unsetCapabilities(module.DefaultKai, KaiCapabilities.AccelerometerData | KaiCapabilities.GyroscopeData | KaiCapabilities.PYRData)
```

#### **Closing the Module**

```python
module.close()
```

Run the example file using the following command
```
python3 gesture.py
```
