# Base class
class Device:
    def __init__(self, name):
        self.name = name
        self.status = False  # False = off, True = on

    def turn_on(self):
        self.status = True

    def turn_off(self):
        self.status = False

    def operate(self):
        raise NotImplementedError("Subclass must override operate()")

    def __str__(self):
        return f"{self.name}: {'ON' if self.status else 'OFF'}"

# Light class
class Light(Device):
    def operate(self):
        if self.status:
            return f"{self.name} is glowing 🌟"
        else:
            return f"{self.name} is turned off"

# Fan class
class Fan(Device):
    def operate(self):
        if self.status:
            return f"{self.name} is spinning 🌀"
        else:
            return f"{self.name} is off"

# AC class
class AC(Device):
    def operate(self):
        if self.status:
            return f"{self.name} is cooling ❄️"
        else:
            return f"{self.name} is off"

# SmartHub class with composition
class SmartHub:
    def __init__(self):
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)

    def control_all(self, action='on'):
        for device in self.devices:
            if action == 'on':
                device.turn_on()
            elif action == 'off':
                device.turn_off()

    def show_status(self):
        print("📡 Smart Hub Device Status:")
        for device in self.devices:
            print(device.operate())

# Create devices
light1 = Light("Living Room Light")
fan1 = Fan("Bedroom Fan")
ac1 = AC("Main Hall AC")

# Create smart hub
hub = SmartHub()

# Add devices to hub
hub.add_device(light1)
hub.add_device(fan1)
hub.add_device(ac1)

# Turn on all devices
hub.control_all('on')

# Show status
hub.show_status()

print("\nTurning off only AC...\n")
ac1.turn_off()

# Show updated status
hub.show_status()
