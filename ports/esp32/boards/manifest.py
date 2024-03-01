freeze("$(PORT_DIR)/modules")
include("$(MPY_DIR)/extmod/asyncio")

# mqtt_as
freeze("$(MPY_DIR)/extmod/mqtt_as", "mqtt_as.py")

# drivers
require("ssd1306")

require("aioble")

# Useful networking-related packages.
require("bundle-networking")

# Require some micropython-lib modules.
require("aioespnow")
require("dht")
require("ds18x20")
require("neopixel")
require("onewire")
require("umqtt.robust")
require("umqtt.simple")
require("upysh")

package("primitives", base_path="$(MPY_DIR)/lib/micropython-async/v3")
package("threadsafe", base_path="$(MPY_DIR)/lib/micropython-async/v3")

