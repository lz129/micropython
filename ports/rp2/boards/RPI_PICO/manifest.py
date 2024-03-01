include("$(PORT_DIR)/boards/manifest.py")

require("bundle-networking")

require("ssd1306")
require("dht")
require("ds18x20")
require("neopixel")
require("onewire")
require("upysh")

package("primitives", base_path="$(MPY_DIR)/lib/micropython-async/v3")
package("threadsafe", base_path="$(MPY_DIR)/lib/micropython-async/v3")
