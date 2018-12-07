#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Worker:

    def __init__(self):
        self.current_job = None
        self.last_job = None
        self.time_left = 0

    def work_on(self, job, secs):
        if self.current_job is not None:
            raise Exception("Oops")

        # should really check types of job and secs
        self.current_job = job
        self.time_left = secs

    def is_idle(self):
        return self.current_job is None

    def work(self):
        if self.current_job is not None and self.time_left > 0:
            self.time_left -= 1

            if self.time_left == 0:
                self.last_job = self.current_job
                self.current_job = None

                return self.last_job

        return None
