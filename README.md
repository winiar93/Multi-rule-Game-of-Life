# Multi-rule-Game-of-Life
Example implementation of strategy and factory design patterns in Game of Life.

## Rules

### Standard Rule
* A live cell with fewer than two live neighbors dies.
* A live cell with two or three live neighbors lives on to the next generation.
* A live cell with more than three live neighbors dies.
* A dead cell with exactly three live neighbors becomes a live cell.

## Day and Night Rule
* A live cell with three, four, six, seven or eight live neighbors lives.
* A dead cell with three six, seven eight or live neighbors becomes a live cell.

## Setup
Create virtual environment
```bash
python -m venv venv
```
Activate virtual environment

```bash
source venv/bin/activate
```

Install all requirements
```bash
pip install -r requirements.txt
```


## Usage
Run the script with the desired rule set as a command-line argument. If no argument is provided, the standard rule is used by default.

```bash
python game_of_life.py [rule]
```

Available game `rules`:
* `standard`
* `dayandnight`

## Available interactions

- Mouse Click: Place new cell or remove single cell.
- Space: Pause/Resume the simulation.
- Enter: Generate a random grid.