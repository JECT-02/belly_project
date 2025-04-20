from src.belly import Belly
import time

start_time = time.time()
for _ in range(1000):
    belly = Belly()
    belly.comer(1000)
    belly.esperar(10)
    assert belly.esta_gruñendo()
print(f"Tiempo total: {time.time() - start_time} segundos")