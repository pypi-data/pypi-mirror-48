# Python Dota 2 GSI

`dota2gsi` is a Python 3 module for interacting with Dota 2 GameState Integration.

## Installation

```console
pip3 install dota2gsi
```

### Enabling GameState Integration

To enable gamestate reporting, copy the config file `gamestate_integration_py.cfg` to `steamapps\common\dota 2 beta\game\dota\cfg\gamestate_integration\`.

```conf
"Python Dota 2 GSI Integration"
{
	"uri"       "http://localhost:56969"
	"timeout" 	"5.0"
	"buffer"  	"0.1"
	"throttle" 	"0.1"
	"heartbeat" "30.0"
	"data"
	{
		"provider"     "1"
		"map"          "1" 
		"player"       "1"
		"hero"         "1"
		"abilities"    "1"
		"items"        "1"
	}
}
```

The DotA 2 GSI is not officially released yet. For more information, see the [CS:GO Game State Integration](https://developer.valvesoftware.com/wiki/Counter-Strike:_Global_Offensive_Game_State_Integration). 

## Usage

1. Import the script

    ```python
    import dotaGSI
    ```

1. Create the listening server
    ```python
    server = dotaGSI.Server(ip='0.0.0.0', port=56969)
    ```

1. (Optional) Add functions to be called for every new state

    ```python
    def example_handler(last_state, state):
        """ Called for every new state """
        print("new state:", state)

    server.on_update(example_handler)
    ```

1. (Optional) Add functions to be called when events are triggered
    ```python
    def print_ability(state, ability):
        """ Called on every ability cast """
        print("Spell cast:", ability.get('name'))

    server.on_ability_cast(print_ability)
    ```

1. Start the listening server
    ```python
    server.start()
    ```

## Examples

### `health.py`
Prints the player's current health value.

```python
import dotaGSI

def handle_state(last_state, state):
    # Use nested gets to safely extract data from the state
    hero_name = state.get('hero', {}).get('name')
    health_percent = state.get('hero', {}).get('health_percent')
    max_health = state.get('hero', {}).get('max_health')
    # If the attributes exist, print them
    if health_percent and max_health:
        health = int(max_health * health_percent/100)
        print(f"{hero_name}'s current health: {health}/{max_health}")

server = dotaGSI.Server(port=56969)
server.on_update(handle_state)
server.start()
```
Output:

```console
npc_dota_hero_shadow_demon's current health: 1480/1480
```

### `on_spell.py`
Calls two functions each time a spell is cast by the player

```python
import dotaGSI

def print_ability(state, ability):
    print("Spell cast:", ability.get('name'), 
          "level:",      ability.get('level'), 
          "cooldown:",   ability.get('cooldown'),
          "mana left:",  state.get('hero', {}).get('mana'))
          
def other_ability_handler(state, ability):
    if ability.get('ultimate'):
        time = state.get('map', {}).get('game_time')
        print("Ultimate cast at", time, "seconds")

server = dotaGSI.Server(port=56969)
server.on_ability_cast(print_ability)
server.on_ability_cast(other_ability_handler)
server.start()
```

Output:

```console
Spell cast: shadow_demon_soul_catcher level: 4 cooldown: 20 mana left: 565
Spell cast: shadow_demon_shadow_poison level: 4 cooldown: 3 mana left: 516
Spell cast: shadow_demon_demonic_purge level: 1 cooldown: 60 mana left: 321
Ultimate cast at 48 seconds
```


