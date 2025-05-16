import krpc
import serial

# Connexion à KSP via kRPC
conn = krpc.connect(name='Arduino Throttle Control')
vessel = conn.space_center.active_vessel

# Configuration du port série (adapté au port de votre Arduino)
serial_port = 'COM3'  # Remplacez par le port série de votre Arduino
baud_rate = 9600
arduino = serial.Serial(serial_port, baud_rate)

try:
    while True:
        if arduino.in_waiting > 0:
            # Lire la valeur envoyée par l'Arduino
            line = arduino.readline().decode('utf-8').strip()
            try:
                throttle = float(line)  # Convertir en float
                throttle = max(0.0, min(1.0, throttle))  # Clamping entre 0.0 et 1.0
                
                # Ajuster la puissance des moteurs dans KSP
                vessel.control.throttle = throttle
                print(f'Throttle set to: {throttle}')
            except ValueError:
                print(f'Invalid input from Arduino: {line}')
except KeyboardInterrupt:
    print("Stopped by user.")
finally:
    arduino.close()
