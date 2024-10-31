# PoE-Simple-Filters

Simple filters for Path of Exile, (without needing a 20k line file...).

Filter components are stored individually within [filters](filters/) as `.inc` files.
Each component must be all lowercase with underscores and numbers allowed.

## Create a new filter

To create a new filter:

1. Create your `.filter` file within this directory named whatever you'd like, (as long as it has a `.filter` suffix).
2. Add any requested filter component in the file in the format of `#filter_component_to_include`, (one per line).
3. Run `./generate_filters.py` to retrieve all filter components and add them to the file.

## Example filter file

Filename: `archer-with-armor-and-evasion.filter`

Hides incompatible armors/weapons and highlights high quality items.

```
#hide_armors_armor
#hide_armors_energy
#hide_armors_energy_armor
#hide_armors_energy_evasion
#hide_armors_evasion
#hide_outdated_flasks
#hide_weapons_magic_1hand
#hide_weapons_magic_2hand
#hide_weapons_melee_1hand
#hide_weapons_melee_2hand
#show_high_quality_items
```

## Adding new filter components

To add a new filter component to be reused between filters, just create a `.inc` file within [filters](filters/) 
and add the base filename in your `.filter` file.  Re-running `./generate_filters.py` will regenerate your filter
file with all requested components.

## Order matters

Path of Exile processes filters in the order they appear in the file, 
so if `show_high_quality_items` is at the top of your filter file,
that show directive will take precedence and will always show all rare items.

Example:

```
#show_high_quality_items
#hide_weapons_melee_1hand
```

`show_high_quality_items` sets 3-link swords to be displayed, so if that is before `hide_weapons_melee_1hand`,
swords will still show despite having the hide included, (the game stops processing item filters as soon as a match occurs).

To show all high quality items _except_ swords, the order matters.


## Default

Unlike other filter generators, there is no default action, so there is no need to include _each and every item_ in the game
just because the system includes a default hide for some reason.

Instead, it's easier to just hide what you don't want.
