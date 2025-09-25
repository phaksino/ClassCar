class Vehicle:
    """Base class for all vehicles"""
    
    def __init__(self, make, model, year, color):
        self._make = make
        self._model = model
        self._year = year
        self._color = color
        self._mileage = 0
        self._is_running = False
    
    # Encapsulation: Protected attributes with getter methods
    def get_make(self):
        return self._make
    
    def get_model(self):
        return self._model
    
    def get_year(self):
        return self._year
    
    def get_color(self):
        return self._color
    
    def get_mileage(self):
        return self._mileage
    
    # Public methods
    def start_engine(self):
        if not self._is_running:
            self._is_running = True
            return f"{self._make} {self._model} engine started! 🚀"
        return f"{self._make} {self._model} engine is already running!"
    
    def stop_engine(self):
        if self._is_running:
            self._is_running = False
            return f"{self._make} {self._model} engine stopped! 🛑"
        return f"{self._make} {self._model} engine is already off!"
    
    def drive(self, distance):
        if self._is_running:
            self._mileage += distance
            return f"Driving {distance} miles. Total mileage: {self._mileage} miles 🛣️"
        return "Start the engine first!"
    
    # Polymorphism: Method to be overridden by subclasses
    def display_info(self):
        return f"{self._year} {self._make} {self._model} - Color: {self._color} - Mileage: {self._mileage} miles"
    
    def honk(self):
        return "Beep beep! 🚗"


class Car(Vehicle):
    """Car class inheriting from Vehicle"""
    
    def __init__(self, make, model, year, color, fuel_type, doors=4):
        super().__init__(make, model, year, color)
        self._fuel_type = fuel_type
        self._doors = doors
        self._fuel_level = 100  # Percentage
        self._max_speed = 120   # mph
    
    # Additional getters for car-specific attributes
    def get_fuel_type(self):
        return self._fuel_type
    
    def get_doors(self):
        return self._doors
    
    def get_fuel_level(self):
        return self._fuel_level
    
    # Car-specific methods
    def refuel(self, amount=100):
        if amount > 0:
            self._fuel_level = min(100, self._fuel_level + amount)
            return f"Refueled! Fuel level: {self._fuel_level}% ⛽"
        return "Invalid fuel amount!"
    
    def check_fuel_consumption(self, distance):
        fuel_used = distance * 0.05  # Simulated fuel consumption
        if fuel_used <= self._fuel_level:
            self._fuel_level -= fuel_used
            return f"Fuel consumed: {fuel_used:.1f}%. Remaining: {self._fuel_level:.1f}%"
        return "Not enough fuel for this distance!"
    
    # Overriding parent method (Polymorphism)
    def drive(self, distance):
        if not self._is_running:
            return "Start the engine first!"
        
        fuel_needed = distance * 0.05
        if fuel_needed > self._fuel_level:
            return f"Not enough fuel! Need {fuel_needed:.1f}% but only have {self._fuel_level:.1f}%"
        
        result = super().drive(distance)
        fuel_info = self.check_fuel_consumption(distance)
        return f"{result}\n{fuel_info}"
    
    # Overriding display_info method
    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}\nFuel Type: {self._fuel_type} - Doors: {self._doors} - Fuel Level: {self._fuel_level}%"


class SportsCar(Car):
    """SportsCar class inheriting from Car"""
    
    def __init__(self, make, model, year, color, horsepower, turbo=False):
        super().__init__(make, model, year, color, "Premium", doors=2)
        self._horsepower = horsepower
        self._turbo = turbo
        self._max_speed = 200  # Override max speed
    
    # SportsCar specific methods
    def activate_turbo(self):
        if self._turbo:
            self._max_speed = 250
            return "Turbo activated! 🏎️💨 Max speed increased to 250 mph!"
        return "No turbo available on this model"
    
    def race_mode(self):
        if self._is_running:
            return f"Race mode engaged! {self._horsepower}HP ready to dominate! 🏁"
        return "Start the engine to activate race mode!"
    
    # Overriding honk method (Polymorphism)
    def honk(self):
        return "Sports car horn: VROOM VROOM! 🏎️"


# Demonstration program
def main():
    print("🚗 VEHICLE MANAGEMENT SYSTEM 🚗")
    print("=" * 40)
    
    # Create different vehicle objects
    regular_car = Car("Toyota", "Camry", 2023, "Blue", "Hybrid")
    sports_car = SportsCar("Ferrari", "488", 2024, "Red", 660, turbo=True)
    
    vehicles = [regular_car, sports_car]
    
    for i, vehicle in enumerate(vehicles, 1):
        print(f"\n--- Vehicle {i} ---")
        print(vehicle.display_info())
        
        # Demonstrate methods
        print(f"\nTesting {vehicle.get_make()} {vehicle.get_model()}:")
        print(vehicle.start_engine())
        print(vehicle.drive(50))
        print(vehicle.honk())
        
        # Car-specific features
        if isinstance(vehicle, Car):
            print(vehicle.refuel(30))
        
        # SportsCar-specific features
        if isinstance(vehicle, SportsCar):
            print(vehicle.activate_turbo())
            print(vehicle.race_mode())
        
        print(vehicle.stop_engine())
    
    # Demonstrate polymorphism
    print("\n" + "=" * 40)
    print("POLYMORPHISM DEMONSTRATION:")
    print("=" * 40)
    
    for vehicle in vehicles:
        print(f"\n{vehicle.get_make()} honk: {vehicle.honk()}")
        print(f"Display info:\n{vehicle.display_info()}")


if __name__ == "__main__":
    main()
