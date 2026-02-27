#Hacer un programa que muestre un cronometro, indicando las horas, minutos y segundos.
print('Cronómetro')

import time
import msvcrt

print("Cronómetro iniciado (presiona Enter para detener)\n")

for hora in range(24):
    for minuto in range(60):
        for segundo in range(60):

            print(f"{hora:02d}:{minuto:02d}:{segundo:02d}")
            time.sleep(1)

            if msvcrt.kbhit():  # Detecta si presionas algo
                if msvcrt.getch() == b'\r':  # Si es Enter
                    print("\nCronómetro detenido.")
                    exit()
print("Fin")