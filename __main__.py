from lab6 import call
import time

if __name__ == '__main__':
    start_time = time.time()

    call.knn_for_six_lab()

    print("\nEnd time: ", time.time() - start_time)
