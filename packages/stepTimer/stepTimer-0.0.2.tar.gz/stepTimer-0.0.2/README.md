# stepTimer

small utility to measure time left after n step of a n equally long tasks, the time withing to tasks and the total time.
The utility is a bit buggy though... please contribute :)

```python
from stepTimer import Timer

timer = timer(nsteps = 1000)

# get the time after 200 steps. this is the total time from the beginning of the task
timer.elapsed(self, step = 200) #=> 2:30:55 in H:M:S

# function to preaty print time
timer.printTime(self, <certain ammount of secods>)  #=> 2:30:55 in H:M:S

# total amount of time elapsed since timer was instantiated
elapsedTot() #=> 2:30:55 in H:M:S

# time left to the compleation of 1000 steps, the total time is calculated as nsteps*average time withing each step.
left(self, step = 300) #=> 5:30:55 in H:M:S
```