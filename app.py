import streamlit as st
import pandas as pd



def length_converter():
    print("\nLength Converter")
    print("1. Meters to Kilometers")
    print("2. Kilometers to Meters")
    choice = input("Enter choice (1 or 2): ")

    if choice == '1':
        meters = float(input("Enter length in meters: "))
        print(f"{meters} meters = {meters / 1000} kilometers")
    elif choice == '2':
        km = float(input("Enter length in kilometers: "))
        print(f"{km} kilometers = {km * 1000} meters")
    else:
        print("Invalid input")

def temperature_converter():
    print("\nTemperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = input("Enter choice (1 or 2): ")

    if choice == '1':
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C = {fahrenheit}°F")
    elif choice == '2':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F = {celsius}°C")
    else:
        print("Invalid input")

def main():
    print("Unit Converter App")
    print("1. Length Converter")
    print("2. Temperature Converter")

    option = input("Choose a converter (1 or 2): ")

    if option == '1':
        length_converter()
    elif option == '2':
        temperature_converter()
    else:
        print("Invalid option selected")

if __name__ == "__main__":
    main()
