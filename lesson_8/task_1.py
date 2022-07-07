import time


class TrafficLight:
    __color = ['красный', 'жёлтый', 'зелёный']

    def running(self):
        while True:
            print(TrafficLight.__color[0])
            time.sleep(7)
            print(TrafficLight.__color[1])
            time.sleep(7)
            print(TrafficLight.__color[2])
            time.sleep(4)

if __name__ == '__main__':
    test = TrafficLight()
    test.running()
