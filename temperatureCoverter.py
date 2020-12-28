from breezypythongui import EasyFrame

class TemperatureConverter(EasyFrame):
    """A temperature conversion program."""

    def __init__(self):
        """Sets up the window and widgets."""
        EasyFrame.__init__(self, "Temperature Converter")
        
        # Define the labels Celsius and Fahrenheit
        self.addLabel(text = "Celsius", row = 0, column = 0)
        self.addLabel(text = "Fahrenheit", row = 0, column = 1)

        # Define the fields for Celsius and Fahrenheit with the required data
        self.celsiusField = self.addFloatField(value = 0.0, row = 1, column = 0)
        self.fahrenheitField = self.addFloatField(value = 32.0, row = 1, column = 1)

        # Add commands button with attributes
        celsiusToFahrenheit = self.addButton(text = ">>>>", row = 2, column = 0, 
        command = self.computeFahr)
        fahrenheitToCelsius = self.addButton(text = "<<<<", row = 2, column = 1, 
        command = self.computeCelsius)

    # The controller methods
    def computeFahr(self):
        """Inputs the Celsius degrees
        and outputs the Fahrenheit degrees."""
        celsiusTemp = self.celsiusField.getNumber()
        celsiusToFahr = (celsiusTemp * (9/5)) + 32
        self.fahrenheitField.setNumber(celsiusToFahr)

    def computeCelsius(self):
        """Inputs the Fahrenheit degrees
        and outputs the Celsius degrees."""
        fahrenheitTemp = self.fahrenheitField.getNumber()
        fahrToCelsius = (fahrenheitTemp - 32) * (5/9)
        self.celsiusField.setNumber(fahrToCelsius)
        

def main():
    """Instantiate and pop up the window."""
    TemperatureConverter().mainloop()

if __name__ == "__main__":
    main()
