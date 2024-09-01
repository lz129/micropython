# This list of package files doesn't include task.py because that's provided
# by the C module.
package(
    "mqtt_as",
    (
        "__init__.py",
        "clean.py",
        "mqtt_v5_properties.py",
        "range.py",
        "range_ex.py"
    ),
    base_path="..",
    opt=3,
)

# Backwards-compatible uasyncio module.
#module("uasyncio.py", opt=3)
