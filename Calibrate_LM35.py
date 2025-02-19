from machine import ADC, Pin
import time

# Konstanta
ADC_MAX = 4095  # Resolusi 12-bit ESP32
V_REF = 5  # Tegangan referensi ESP32

# Inisialisasi ADC
analogInputPin = ADC(Pin(34))  
analogInputPin.atten(ADC.ATTN_11DB)  # Mengatur agar bisa membaca hingga 3.3V

while True:
    # Membaca nilai ADC (0 - 4095)
    analogValue = analogInputPin.read()
    
    # Konversi ke tegangan (Volt)
    sensor_voltage = (analogValue / ADC_MAX) * V_REF
    
    # Konversi ke suhu LM35 (10mV per 1°C)
    temperature = sensor_voltage * 100  # Karena 1V = 100°C
    
    # Menampilkan hasil
    print(f"ADC Value: {analogValue}, Voltage: {sensor_voltage:.3f}V, Temperature: {temperature:.2f}°C")
    
    time.sleep(0.1)