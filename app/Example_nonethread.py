import time

#olah data 1 juta
class olah_data:
    def __init__(self, rentang):
        self.rentang = rentang
    
    def take(self):
        print("[1] take data from data to : {}".format(self.rentang))
        time.sleep(1)

    def sort(self):
        print("[2] sort data from data to : {}".format(self.rentang))
        time.sleep(1)

    def export(self):
        print("[3] export data from data to : {}".format(self.rentang))
        time.sleep(1)

    def run(self):
        self.take()
        self.sort()
        self.export()

if __name__ == '__main__':
    start = time.perf_counter()
    rentangs = [
        "1 - 100000",
        "100001 - 200000",
        "200001 - 300000",
        "300001 - 400000",
        "400001 - 500000",
        "500001 - 600000",
        "600001 - 700000",
        "700001 - 800000",
        "800001 - 900000",
        "900001 - 1000000",
    ]

    for rentang in rentangs:
        olah_data(rentang).run()
    finish = time.perf_counter()
    print("Total waktu = {} detik".format(finish-start))