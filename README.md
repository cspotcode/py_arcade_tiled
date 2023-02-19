Decorators and functions to help you describe a class in Python, then place instances of it in the Tiled editor.

- Takes decoratored python classes, and emits Tiled "custom types" configuration.
- Emits Tiled "templates" to enable quick drag-and-drop of objects.
- When loading a Tiled map, returns instances of your classes, with custom fields populated.

*Caveats: example tiled files are incomplete, I copy-pasted them from another project. The example does not run. This is a sketch of the API, it is not functional.*

## Workflow

- Declare a class for every type of object you want to be placed in the map editor.  [example/objects.py](example/objects.py)
- Create a `TiledLoader` that knows about all those classes: [example/configure_tiled.py](example/configure_tiled.py)
- Run `write_tiled_configuration` to write/update Tiled project files, teaching Tiled about your classes.
- Edit a map in Tiled, dragging-and-dropping the templates that have been automatically created for you.
- In game startup code, run `loader.load_map()` to load the map.

