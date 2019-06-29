#!/usr/bin/env python
import psutil
import sched
import time
import json

from config import settings


class snapshots(object):
    """SYSTEM MONITOR"""

    def pc_meter(self):
        """PC metrics"""

        ss = sched.scheduler(time.time, time.sleep)
        time_steps = int(settings['interval'])

        print("SNAPSHOT: TIMESTAMP")
        print("CPU load             -", psutil.cpu_percent(interval=1), "%")
        print("Physical memory used -", psutil.disk_usage('/'))
        print("Virtual memory used  -", psutil.virtual_memory()[2], "%")
        print("IO information       -", psutil.Process().io_counters())
        print("Network information  -", psutil.net_io_counters(pernic=True))

        ss.enter(time_steps, 1, snapshots.pc_meter, (ss, ))
        ss.run()

    def builder(self):
        """Main code"""

        outpfile = settings['output']
        with open(outpfile + ".json", "w", encoding="utf-8") as outfile:
            json.dump({"CPU load": psutil.cpu_percent(interval=1),
                       "Physical memory used": psutil.disk_usage('/'),
                       "Virtual memory used": psutil.virtual_memory()[2],
                       "IO information": psutil.Process().io_counters(),
                       "Network information": psutil.net_io_counters(pernic=True)},
                      outfile, ensure_ascii=False, indent=2)

        print(snapshot.pc_meter())


snapshot = snapshots()
print(snapshot.builder())

