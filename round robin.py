class RR(SchedulerDES):
    def scheduler_func(self, cur_event):
        #creating a variable for the shortest service time
        #from the current event's service time
        shortest_service_time = self.cur_event.service_time
        #loops through all processes 
        #if the service time is less than the shortest service time
        #then 
        for i in self.processes:
            if i._service_time < shortest_service_time:
                shortest_service_time = i._service_time
                process = i

        process.process_state = ProcessStates.READY
        return process

    def dispatcher_func(self, cur_process):
        pass