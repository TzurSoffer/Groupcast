import time
import groupcast

class SlowWorker:
    def __init__(self, id):
        self.id = id
    def work(self):
        time.sleep(1)
        print(f"Done by {self.id}")

# Serial (slow)
b = time.time()
group = groupcast.Group(inputs=[1, 2, 3], class_=SlowWorker)
group.work()  #< Takes ~3 second
print(f"Finished serial execution in {time.time()-b:2f} seconds")

# Parallel (fast)
b = time.time()
group.changeExecutionMode(parallel=True)
group.work()  #< Takes ~1 second
print(f"Finished parallel execution in {time.time()-b:2f} seconds")