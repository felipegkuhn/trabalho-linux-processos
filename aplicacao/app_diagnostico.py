import time
import threading
import os

def tarefa_cpu():
    print(f"[Thread CPU] Iniciada na Thread ID: {threading.get_native_id()}")
    while True:
        x = 0
        for i in range(1000000):
            x += i
        time.sleep(0.1)

def tarefa_io():
    print(f"[Thread IO] Iniciada na Thread ID: {threading.get_native_id()}")
    while True:
        time.sleep(2)

if __name__ == "__main__":
    print("==================================================")
    print(f"Aplicacao de Diagnostico Iniciada!")
    print(f"PID do Processo: {os.getpid()}")
    print(f"PPID (Processo Pai): {os.getppid()}")
    print("==================================================")
    
    t1 = threading.Thread(target=tarefa_cpu, name="Thread-CPU")
    t2 = threading.Thread(target=tarefa_io, name="Thread-IO")
    
    t1.daemon = True
    t2.daemon = True
    
    t1.start()
    t2.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nEncerrando aplicacao...")
