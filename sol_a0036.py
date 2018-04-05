#fht_temp - Fahrenheit temperature to be converted to Celsius.

def convert_fahrenheit_to_celsius(fth_temp):
    converter =float(5/9.0*(fth_temp-32))
    return converter

print(convert_fahrenheit_to_celsius(32))
