import logging, time

import multiprocessing as mp


class Task:
    def __init__(self, section):
        self.section = section
    
    def __call__(self):
        while not self.section.is_constructed():
            self.section.build()
            time.sleep(0.2)



class Consumer(mp.Process):
    def __init__(self, task_queue, output_q, consumer_number):        
        mp.Process.__init__(self)
        self.task_queue = task_queue
        self.output_q = output_q
        self.consumer_number = consumer_number
    
    def run(self):
        while True:
            next_task = self.task_queue.get()
            next_task()
            self.output_q.put(next_task)
            self.task_queue.task_done()
            logging.debug(f"Consumer {self.consumer_number} built Profile {next_task.section.profile_number} - Section {next_task.section.section_position}. Workdays - {next_task.section.day}")