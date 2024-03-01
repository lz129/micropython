include("$(PORT_DIR)/boards/manifest.py")

require("bundle-networking")

# mqtt_as
freeze("$(MPY_DIR)/extmod/mqtt_as", "mqtt_as.py")

# Bluetooth
require("aioble")
require("ssd1306")
require("dht")
require("ds18x20")
require("neopixel")
require("onewire")
require("umqtt.robust")
require("umqtt.simple")
require("upysh")

package("primitives", base_path="$(MPY_DIR)/lib/micropython-async/v3")
package("threadsafe", base_path="$(MPY_DIR)/lib/micropython-async/v3")
