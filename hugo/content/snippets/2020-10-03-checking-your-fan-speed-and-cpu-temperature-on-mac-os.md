+++
title = "Checking Your Fan Speed and CPU Temperature on Mac OS (2020)"
date = 2020-10-03T15:46:00
+++

I've seen people monitor their CPU temperature and today my laptop was running hot, so I wanted to do so myself. Googling "check laptop temperature mac" gives projects you can download. I didn't want to have to trust someone else's tool or mess around with someone else's code, and I knew there must be a system call that gives me sensor stats, so I kept looking.

Indeed, there's a command you can run to get your processor temperatures and fan speeds.

`sudo powermetrics --samplers smc`

To narrow down the stats you see further, you can grep for e.g. "Fan:", "CPU die temperature:", or "GPU die temperature:".

```bash
sudo powermetrics --samplers smc | grep "Fan:"
sudo powermetrics --samplers smc | grep "CPU die temperature:"
sudo powermetrics --samplers smc | grep "GPU die temperature:"
```

Use egrep if you want all three:

```bash
sudo powermetrics --samplers smc | egrep 'temp|Fan'
```

Now, why does [mmhmm](https://www.mmhmm.app/) make my machine run so hot?
