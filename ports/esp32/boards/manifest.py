freeze("$(PORT_DIR)/modules")
include("$(MPY_DIR)/extmod/asyncio")
#include("$(MPY_DIR)/extmod/micropython-mqtt")

#dd_library("micropython-mqtt", "$(MPY_DIR)/extmod/micropython-mqtt")

# Useful networking-related packages.
require("bundle-networking")

#equire("micropython-mqtt", library="micropython-mqtt")
package("mqtt_as", base_path="$(MPY_DIR)/extmod/micropython-mqtt")
package("primitives", base_path="$(MPY_DIR)/extmod/micropython-async/v3")
package("threadsafe", base_path="$(MPY_DIR)/extmod/micropython-async/v3")


# Require some micropython-lib modules.
require("aioespnow")
require("aioble")
require("dht")
require("ds18x20")
require("neopixel")
require("onewire")
require("ssd1306")
require("umqtt.robust")
require("umqtt.simple")
require("upysh")
