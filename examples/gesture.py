from KaiSDK.WebSocketModule import WebSocketModule
from KaiSDK.DataTypes import KaiCapabilities
import KaiSDK.Events as Events


def gestureEvent(ev):
    print(ev.gesture)


def accelerometerEv(ev):
    print("Acce")
    print(ev.accelerometer)
    print(ev.accelerometer.x)
    print(ev.accelerometer.y)
    print(ev.accelerometer.z)


def fingerShortcutEv(ev):
    print(ev.fingers)


def gyroScopeEv(ev):
    print(ev.gyroscope)


moduleID = "TEST"
moduleSecret = "qwerty"

module = WebSocketModule()
success = module.connect(moduleID, moduleSecret)

if not success:
    print("Unable to authenticate with Kai SDK")
    exit(1)

module.setCapabilities(module.DefaultKai, KaiCapabilities.AccelerometerData | KaiCapabilities.GestureData |
                       KaiCapabilities.LinearFlickData |
                       KaiCapabilities.FingerShortcutData |
                       KaiCapabilities.PYRData |
                       KaiCapabilities.QuaternionData |
                       KaiCapabilities.GyroscopeData |
                       KaiCapabilities.MagnetometerData)

# module.AnyKai.register_event_listener(Events.AccelerometerEvent, accelerometerEv)
module.DefaultKai.register_event_listener(Events.AccelerometerEvent, accelerometerEv)
module.AnyKai.register_event_listener(Events.GestureEvent, gestureEvent)
module.AnyKai.register_event_listener(Events.FingerShortcutEvent, fingerShortcutEv)
module.DefaultKai.register_event_listener(Events.GyroscopeEvent, gyroScopeEv)
