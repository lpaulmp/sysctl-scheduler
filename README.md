## sysctl-scheduler
Sysctl schedulers
Test sysctl options in vagran
t
### Requirement
- Install Vagrant 2
- Install ansible +2.2

### Setup the environment
The environment run ansible to install and upload scripts
```
vagrant up
```

### Scripts to test
To test and check the configurations, check that the port localhost:8080 is
returning a test html, then run the script which check time of curl and create
file `get_time` where stores the time of the request.
```
./check_curl.py
```
To stress the virtual machine, the a crontab run every minute a script to increase 
 the load average, this will create a scenario to applies tuning the linux kernel schedulers.

### Change linux scheduler options
Login to vagrant and tune scheduler options applying the follow script:
```
/opt/sched_tune
```
This will adjust the CFS parameters:
```
sched_latency_ns=100000
sched_wakeup_granularity_ns=500000
sched_min_granularity_ns=500000
```
The difference is not significant but helps in long terms since the request reduced 3.1% the time response, when the cpu is overload.
