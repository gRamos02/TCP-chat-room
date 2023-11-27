import threading
import time

def funcuno(a):
    x=0
    while x<a:
        print(x)
        x+=1
        time.sleep(1) 
    
def funcdos(a):
    x=a
    while x>0:
        print(x)
        x-=1
        time.sleep(1) 

if __name__ == '__main__':
    print('iniciando...')
    t1 = threading.Thread(target=funcuno, args=(5,))
    t2 = threading.Thread(target=funcdos, args=(5,))

    t1.start()
    t2.start()


    t1.join()
    t2.join()

    if t1.is_alive():
        print('proceso vivo...')
        time.sleep(1)
    else:
        print('proceso muerto...')


    print('terminado')