# Sorting_algorithms
## Sorting algorithms program for networks and operating systems essentials course
The sorting algorithms used were:
* First come first served (FCFS)
* Shortest job first (SJF)
* Round robin (RR)
* Shortest remaining time first (SRTF)

Each algorithm was ran using three different seed values, which increased each time in order to get a variety of results for comparison

## results from testing
#### Seed: 1797410758
**Average turnaround time** <br />
From the outputs, it is seen that the Shortest remaining time first (SRTF) has the lowest average turnaround time and first come first served (SCFS) has the highest. <br />
**Average waiting time** <br />
From the outputs, it is seen that the Shortest remaining time first (SRTF) has the lowest average wait time and first come first served (SCFS) has the highest. <br />
**conclusion**
The shortest remaining time first (SRTF) scheduler was the most efficient overall from this seed by numerous seconds, it is really effective as it is constantly checking the new arrivals for their remaining time and running the one with the shortest remaining time.
The least effective here was the First come first served (FCFS), it is typically slower as it fully executes in arrival time, process #2 increased the average waiting time and turnaround time with its 8.5 second execution time. <br />
<img width="780" alt="Screenshot 2022-05-29 at 22 48 56" src="https://user-images.githubusercontent.com/97540217/170892598-da10d85b-3c01-4735-8410-b8994f897cfe.png">  <br />

#### Seed: 2688744162 <br />
**Average turnaround time** <br />
From the outputs, it is seen that the Shortest remaining time first (SRTF), had the lowest average turnaround time, however SJF was very close to the average time (just 0.053... milliseconds difference), and (Round Robin (RR)) has the highest. <br />
**Average waiting time** <br />
From the outputs, it is seen that the Shortest remaining time first (SRTF) had the lowest average waiting time, and again SJF was very close (just 0.053... milliseconds difference), and (Round Robin (RR)) has the highest. <br />
**conclusion**
Overall, the most effective scheduler was the Shortest remaining time first (SRTF), from the seeds the process would have changed quite frequently when a new process arrived, therefore the scheduler would have finished a few of the processes before all 10 had arrived.
Shortest job first was only milliseconds behind, possibly because it waits for all the processes to arrive first, so it can find the process with the shortest time.<br />
The least effective here was the round robin (RR) as it is constantly switching the process getting executed, which extends the wait time as 9 processes are always waiting for their turn.<br />
<img width="725" alt="Screenshot 2022-05-29 at 22 51 53" src="https://user-images.githubusercontent.com/97540217/170892673-2496d5be-4902-4044-a88d-eb45a0faf48e.png"> <br />

#### seed: 3399474557 <br />
**Average turnaround time **<br />
From the outputs, it is seen that the (Shortest remaining time first (SRTF)) has the lowest average turnaround time and (First come first served (FCFS)) has the highest. <br />
**Average waiting time** <br />
From the outputs, it is seen that the Shortest remaining time first (SRTF) has the lowest average wait time and first come first served (FCFS) has the highest. <br />
**Conclusion**
Overall, the most effective scheduler was the shortest remaining time first (SRTF) as it is really effective in switching processes when there is one with a lower remaining time. The non-Preemptive version, shortest job first (SJF), was the next efficient, however was 2 seconds slower regarding the average turnaround times and waiting times. The least effective being First come first served (FCFS), which is significantly slower than the other schedulers. <br />
<img width="791" alt="Screenshot 2022-05-29 at 22 54 14" src="https://user-images.githubusercontent.com/97540217/170892743-3243c49e-a6aa-45fd-8d7f-d6136ce9fa08.png"> <br />

## Overall Conclusion
#### findings from the testing <br />
As the seeds increase, the results show a fluctuation in the average waiting and turnaround times for each scheduler. The seed 2688744162 gives an increase in the average waiting and turnaround times for each scheduler from the first seed (1797410758), then the final seed (3399474557) sees a decrease in the average times for all the schedulers. For testing purposes, we ran with a slightly higher seed than 3399474557, and again the average times decreased, then with a slightly more increased one they increased. The pattern appears to be an increase then degrease in the average waiting and turnaround times.
Overall, the quickest scheduler is Shortest Remaining Time First (SRTF) and the slowest was First Come First Served (FCFS). On average, the pre-emptive schedulers were more efficient. The results were as we expected, with the pre-emptive scheduler shortest remaining time first running quickest in all the tests.


