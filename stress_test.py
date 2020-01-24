import library.space.main as space
import library.vines.main as vines
from threading import Thread 
from multiprocessing import Process

Processes = []
import timeit

def main():
    coworking = space.coworking()
    reply = ''
    for package in coworking:
        reply = reply + '* **%s**, \n\nwhich costs ***%s***. \n\nThe Benfits are as follows: \n\n *%s* \n\n\n\n' % (str(package['package']), str(package['cost']), str(package['benefits']))
    print(reply)
if __name__ == "__main__":
    elapsed_time = timeit.timeit(main, number=1)/1
    for i in range(1000):
        print('Registered Thread %d' % i)
        Processes.append(Process(target=main()))
        
    for process in Processes :
        process.start()

    for process in Processes: 
        process.join()

    print(elapsed_time)