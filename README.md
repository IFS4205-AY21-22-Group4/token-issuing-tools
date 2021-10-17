# Tools for token issuing

### discover.py

This is used to view nearby bluetooth devices.

Prerequisites:
 - Python
 - Bleak

To install Bleak:
```
pip install bleak
```

To run script:
```
python discover.py
```

1. Enter 1 to view all devices and 2 to view devices with "IFS4205" in the name
    ```
    (1) Display all nearby devices
    (2) Display only IFS4205 devices
    ```
1. Copy address required after identifying the device
    ```
    (copy)            address              name
    ========================================================
    (E9FCCD620A49)    E9:FC:CD:62:0A:49    IFS4205-E9FCCD
    ```