from functools import partial, update_wrapper
import datetime

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

    @property
    def second(self):
        assert self.interval == 1
        return self.seconds

    @property
    def seconds(self):
        self.time_unit = 'seconds'
        return self

    @property
    def minute(self):
        assert self.interval == 1
        return self.minutes

    @property
    def minutes(self):
        self.time_unit = 'minutes'
        return self

    @property
    def hour(self):
        assert self.interval == 1
        return self.hours

    @property
    def hours(self):
        self.time_unit = 'hours'
        return self

    def do(self, job_function, *args, **kwargs):
        self.job_function = partial(job_function, *args, **kwargs)
        update_wrapper(self.job_function, job_function)
        self._schedule_next_run()
        return self

    def _schedule_next_run(self):
        assert self.time_unit in ('seconds', 'minutes')
        self.time_period = datetime.timedelta(**{self.time_unit:self.interval})
        self.next_run = datetime.datetime.now() + self.time_period
