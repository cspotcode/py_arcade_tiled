from __future__ import annotations

from typing import Optional, Tuple, Annotated as A

from arcade import color
from arcade import Sprite
import arcade_tiled.decorators as tiled
from pyglet.math import Vec2

# Will appear in Tiled as a drag-and-droppable rectangle shape
@tiled.template(rectangle=True)
@tiled.object
class Wall:

    position: A[Vec2, tiled.position]
    rotation: A[Vec2, tiled.rotation]
    scale: A[Vec2, tiled.scale]
    color: A[str, tiled.custom]

    @tiled.init
    def setup(self):
        """
        Called after all objects are loaded.
        Can do validation, other wiring, whatever you want to happen *after* the map has been loaded.
        """
        pass

# Will appear as a drag-and-droppable object with this image
@tiled.template(image="spawn_point.png")
class SpawnPoint:

    # We can make it easier; no need to wrap in `A[Vec2, ...]`
    position: tiled.position

    initial_spawn_for_player: A[Optional[int], tiled.custom]

# You can also annotate subclasses of Sprite
# These will be instantiated as you'd expect: you get a sprite with the same image, position, etc that you see in
# Tiled.  Very similar to the way things work today with `custom_class`, expect you can have multiple classes
# in a single layer.
@tiled.template(image="spike_trap.png")
@tiled.object
class SpikeTrap(Sprite):
    damage: A[int, tiled.custom]
