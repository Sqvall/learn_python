from abc import ABC


# NOT COMPLETE!


class Observer(ABC):
    def update(self, temp, humidity, pressure):
        pass


class Subject(ABC):
    def register_observer(self, obj: Observer):
        pass

    def remove_observer(self, obj: Observer):
        pass

    def notify_observers(self):
        pass


class DisplayElement(ABC):
    def display(self):
        pass


class CurrentConditionsDisplay(Observer, DisplayElement):

    def __init__(self, weather_data: Subject):
        self.weather_data = weather_data
        weather_data.register_observer(self)
        self.temperature = None
        self.humidity = None

    def update(self, temp, humidity, pressure):
        self.temperature = temp
        self.humidity = humidity
        self.display()

    def display(self):
        print(f"Current conditions: {self.temperature} F degrees and {self.humidity} % humidity")


class WeatherData(Subject):
    observers = None

    def __init__(self):
        self.observers = []
        self.temperature = None
        self.humidity = None
        self.pressure = None

    def register_observer(self, obj: Observer):
        self.observers.append(obj)

    def remove_observer(self, obj: Observer):
        self.observers.remove(obj)

    def notify_observers(self):
        for i in self.observers:
            i.update(self.temperature, self.humidity, self.pressure)

    def measurements_changed(self):
        self.notify_observers()

    def set_measurements(self, temp, humidity, pressure):
        self.temperature = temp
        self.humidity = humidity
        self.pressure = pressure
        self.measurements_changed()


if __name__ == '__main__':
    weather_data = WeatherData()
    current_display = CurrentConditionsDisplay(weather_data)
    weather_data.set_measurements(80, 65, 30)
    weather_data.set_measurements(82, 70, 29)
    weather_data.set_measurements(78, 90, 28)
