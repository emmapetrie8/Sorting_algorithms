#Emma Petrie and Lauren Breckenridge
#lab 7
from os import times
from des import SchedulerDES
from event import Event, EventTypes
from process import *

"""
non-preemptive scheduling
executes processes in order of arrival
"""
class FCFS(SchedulerDES):
    def scheduler_func(self, cur_event):
        #new process passed in
        #gets the process_id of the current event and returns the process
        process = self.processes[cur_event.process_id]
        return process

    def dispatcher_func(self, cur_process):
        #gets the next process to run and runs it
        #executes until process is done
        cur_process.process_state = ProcessStates.RUNNING
        running_time = cur_process.remaining_time
        cur_process.run_for(running_time, self.time)
        cur_process.process_state = ProcessStates.TERMINATED
        #return event when terminated
        return Event(process_id=cur_process.process_id, event_type=EventTypes.PROC_CPU_DONE, event_time=self.time+running_time)

"""
#shortest job first
#executes the process with the shortest service_time first
#non-preemptive
"""
class SJF(SchedulerDES):
    def scheduler_func(self, cur_event):
        #initialise the maximum_process_time variable as 0, will be updated later
        maximum_process_time = 0
        #looping through each of the processes and if the remaining time is >= the maximum process time and its ready to execute
        #updates the maximum_process_time variable to be equal to the process p's remaining time
        for p in self.processes:
            if p.remaining_time >= maximum_process_time and p.process_state == ProcessStates.READY:
                maximum_process_time = p.remaining_time

        #looping through each of the processes and if the remaining time is < the minimum process time and its ready to execute
        #the minimum_process_time variable is updated to equal the process p's remaining time
        minimum_process_time = maximum_process_time
        for p in self.processes:
            if p.remaining_time < minimum_process_time and p.process_state == ProcessStates.READY:
                minimum_process_time = p.remaining_time

        #loops through all the processes and if the remaining time is equal to the minimum_process_time then the process is returned 
        #and sent to the dispatcher
        for p in self.processes:
            if p.remaining_time == minimum_process_time:
                return p

    def dispatcher_func(self, cur_process):
        #executes untill process is done
        cur_process.process_state = ProcessStates.RUNNING
        running_time = cur_process.remaining_time
        cur_process.run_for(running_time, self.time)
        cur_process.process_state = ProcessStates.TERMINATED
        #return event when terminated
        return Event(process_id=cur_process.process_id, event_type=EventTypes.PROC_CPU_DONE, event_time=self.time+running_time)

"""
#round robin scheduling
#all processes get fair share of the CPU
#preemptive
"""
class RR(SchedulerDES):
    def scheduler_func(self, cur_event):
        #new process passed in
        #gets the process_id of the current event and returns the process        
        process = self.processes[cur_event.process_id]
        return process

    def dispatcher_func(self, cur_process):
        #makes the process ready to run
        cur_process.process_state = ProcessStates.RUNNING
        #runs the process for the lowest time parameter (either quantum or the service time)
        if cur_process.remaining_time > self.quantum:
            actually_run_for = cur_process.run_for(self.quantum, self.time)
            #put the current processes running state back to ready
            cur_process.process_state = ProcessStates.READY
            return Event(process_id=cur_process.process_id, event_type=EventTypes.PROC_CPU_REQ, event_time=self.time+actually_run_for)
        else:
            #runs the process for the remaining time and terminates it before returning it 
            actually_run_for = cur_process.run_for(cur_process.remaining_time, self.time)
            cur_process.process_state = ProcessStates.TERMINATED
            return Event(process_id=cur_process.process_id, event_type=EventTypes.PROC_CPU_DONE, event_time=self.time+actually_run_for)

"""
shortest remaining time first scheduling
the process with the shortest remaining execution time is executed first
preemptive
"""
class SRTF(SchedulerDES):
    def scheduler_func(self, cur_event):
        #initialise the maximum_process_time variable as 0, will be updated later
        maximum_process_time = 0
        #looping through each of the processes and if the remaining time is >= the maximum process time and its ready to execute
        #updates the maximum_process_time variable to be equal to the process p's remaining time
        for p in self.processes:
            if p.remaining_time >= maximum_process_time and p.process_state == ProcessStates.READY:
                maximum_process_time = p.remaining_time

        #looping through each of the processes and if the remaining time is < the minimum process time and its ready to execute
        #the minimum_process_time variable is updated to equal the process p's remaining time
        minimum_process_time = maximum_process_time
        for p in self.processes:
            if p.remaining_time < minimum_process_time and p.process_state == ProcessStates.READY:
                minimum_process_time = p.remaining_time

        #loops through all the processes and if the remaining time is equal to the minimum_process_time then the process is returned 
        #and sent to the dispatcher
        for p in self.processes:
            if p.remaining_time == minimum_process_time:
                return p

    def dispatcher_func(self, cur_process):
        #starts running the process
        cur_process.process_state = ProcessStates.RUNNING
        #gets the arrival time of the next process
        t = self.next_event_time() 
        #calculates a duration to run the process for before the next arrival
        duration = t - self.time
        execution_time = cur_process.run_for(duration , self.time)
        #if remaining time is zero, the process has finished running and is terminated and returned
        if cur_process.remaining_time == 0:
            cur_process.process_state = ProcessStates.TERMINATED
            return Event(process_id=cur_process.process_id, event_type=EventTypes.PROC_CPU_DONE, event_time=self.time+execution_time)
        else:
            #process is set to ready and returned to the list as still has some execution time to go
            cur_process.process_state = ProcessStates.READY
            return Event(process_id=cur_process.process_id, event_type=EventTypes.PROC_CPU_REQ, event_time=self.time+execution_time)
