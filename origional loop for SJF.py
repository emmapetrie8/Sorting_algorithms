        
        #looping through the list of processes and picking the one with the shortest service time
        #i is a process in the processes list
        for i in self.processes:
            if i.service_time < min_time:
                min_time = process.service_time
                #sets process to the shortest job first process in the list of processes
                process = i
                
        process.process_state = ProcessStates.READY
        return process