**0: Information**

    This application monitors your system / server
    
    Application create snapshots of the state of the system: 
    - Overall CPU load;
    - Overall memory usage;
    - Overall virtual memory usage;
    - IO information;
    - Network information.

    App save all snapshots on log file

**1: Launch** 

    Тo start the application enter in the console `python ststus_monitor.py`
    
**2: Configuration**

    To change the settings you need to open the configuration file in any text editor 
    `vi ./config.py`
    
    Set time interval in seconds for snapshots:
        
        'interval': '60'
        
    possible values: 1 ... n | 1, 10, 20, 300 & etc
       
    
    Change output log:
    
        'output': 'log'
     
     output formats: name.txt, name.log, name.xml & etc