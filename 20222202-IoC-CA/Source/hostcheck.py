from test_main import *

DellValues = ['c8:4b:d6:0a:77:2d', 'c0:25:a5:66:81:fc', 'a4:4c:c8:50:c3:6b']
if mac == "b8:27:eb:b4:81:6d":
    host_type = "Raspberry PI"
elif mac in DellValues:
    host_type = "Dell"
elif mac == "18:68:cb:45:1a:ae":
    host_type = "Hikvision"
elif mac == "bc:5f:f4:45:7c:1e":
    host_type = "ASRock"
else:
    host_type = "Unknown"