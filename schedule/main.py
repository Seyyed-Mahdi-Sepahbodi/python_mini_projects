
class Scheduler:
    
    def __init__(self):
        self.jobs = []    

    def every(self, interval=1):
        job = Job(interval)
        self.jobs.append(job)
        return job



class Job:
    
    def __init__(self, interval):
        self.interval = interval
        self.job_function = None
        self.last_run = None
        self.next_run = None
        self.time_unit = None
        self.time_period = None    