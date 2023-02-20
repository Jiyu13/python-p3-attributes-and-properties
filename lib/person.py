#!/usr/bin/env python3

approved_jobs = ["Admin", "Customer Service", "Human Resources", "ITC", "Production", "Legal", "Finance", "Sales", "General Management", "Research & Development", "Marketing", "Purchasing"]

class Person:
    
    def __ini__(self, name="", job=""):
        self._name = name
        self._job = job

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if type(name) == str and 1 <= len(name) <= 25:
            self._name = name.title()
        else:
            print("Name must be string between 1 and 25 characters.")

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, job):
        if job in approved_jobs:
            self._job = job
        
        else: with
            print("Job must be in list of approved jobs.")
