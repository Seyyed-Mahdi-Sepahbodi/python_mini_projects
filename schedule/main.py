from functools import partial, update_wrapper
import datetime


class ScheduleError(Exception):
    pass


class ScheduleValueError(ScheduleError):
    pass


class IntervalError(ScheduleValueError):
    pass


class Scheduler:
    
    def __init__(self):
        self.jobs = []    

    def every(self, interval=1):
        job = Job(interval)
        self.jobs.append(job)
        return job

    def run_pending(self):
        all_jobs = (job for job in self.jobs if job.should_run)
        for job in sorted(all_jobs):
            job.run()


class Job:
    
    def __init__(self, interval):
        self.interval = interval
        self.job_function = None
        self.last_run = None
        self.next_run = None
        self.time_unit = None
        self.time_period = None

    def __lt__(self, other):
        return self.next_run < other.next_run

    @property
    def second(self):
        if self.interval != 1:
            raise IntervalError('You should use seconds instead of second!')
        return self.seconds

    @property
    def seconds(self):
        self.time_unit = 'seconds'
        return self

    @property
    def minute(self):
        if self.interval != 1:
            raise IntervalError('You should use minutes instead of minute!')
        return self.minutes

    @property
    def minutes(self):
        self.time_unit = 'minutes'
        return self

    @property
    def hour(self):
        if self.interval != 1:
            raise IntervalError('You should use hours instead of hour!')
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
        if self.time_unit not in ('seconds', 'minutes'):
            raise ValueError('Invalid time unit value!')
        self.time_period = datetime.timedelta(**{self.time_unit:self.interval})
        self.next_run = datetime.datetime.now() + self.time_period

    def run(self):
        result = self.job_function()
        self.last_run = datetime.datetime.now()
        self._schedule_next_run()
        return result

    @property
    def should_run(self):
        return datetime.datetime.now() >= self.next_run


default_scheduler = Scheduler()

def every(interval=1):
    return default_scheduler.every(interval)

def run_pending():
    return default_scheduler.run_pending()
