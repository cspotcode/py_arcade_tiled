# Run this script when you make python changes.
# It will update your Tiled project to match.

from arcade_tiled.loader import TiledLoader
from example.objects import SpawnPoint, SpikeTrap, Wall

loader = TiledLoader(classes=[
    Wall,
    SpawnPoint,
    SpikeTrap
])

if __name__ == "__main__":
    loader.write_tiled_configuration(project_dir="tiled_project")
