# base modules
include("$(PORT_DIR)/boards/manifest.py")

# asyncio
include("$(MPY_DIR)/extmod/asyncio")

# mqtt_as
freeze("$(MPY_DIR)/extmod/mqtt_as", "mqtt_as.py")

# drivers
require("ssd1306")

# micropython-lib: file utilities
require("upysh")

# micropython-lib: umqtt
require("umqtt.simple")
require("umqtt.robust")
