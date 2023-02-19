from .configure_tiled import loader
from .objects import SpawnPoint, SpikeTrap

map = loader.load_map("map-name")

# Get list[SpawnPoint]
# All fields have been parsed from the map and set on the instances
spawn_points = map.get_all(SpawnPoint)

spike_traps = map.get_all(SpikeTrap)