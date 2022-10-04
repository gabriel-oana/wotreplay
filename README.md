<span><img src="https://img.shields.io/github/workflow/status/gabriel-oana/wotreplay/Tests">
<img src="https://img.shields.io/github/languages/top/gabriel-oana/wotreplay">
<img src="https://img.shields.io/pypi/pyversions/wotreplay">
<img src="https://img.shields.io/pypi/v/wotreplay">
<img src="https://img.shields.io/badge/linting-pylint-green">
[![Downloads](https://pepy.tech/badge/wotreplay)](https://pepy.tech/project/wotreplay)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)
<img src="https://img.shields.io/pypi/dm/wotreplay?label=pypi%20downloads">
[![codecov](https://codecov.io/gh/gabriel-oana/wotreplay/branch/main/graph/badge.svg?token=08F8TY2J77)](https://codecov.io/gh/gabriel-oana/wotreplay)
</span>

# World of Tanks - Replay data extract

### 1. Description
The package can extract only the metrics data from World of Tanks replays. 
It does not access any data such as tank positions or chat. 

Data can be extracted only from replays in which the player has waited until the end of the battle. If the player has 
quit the battle after dying and the battle was not ended, then only the battle metadata is available (which does not 
contain any battle performance / credits / xp data).

The replays should be set to be "all" collected and not "last" one recorded. 

All data extracted can be saved to a local sqlite database. 
### 2. Usage
```shell
pip install wotreplay
```

The package provides the possibility of exploring the data contained within one replay or process all replays in a 
directory and store the data in a local database.

```python
from wotreplay import ReplayData
replay = ReplayData(file_path='path_to_replay/replay_file.wotreplay',
                     db_path='', db_name='', load=False)

print(replay.battle_metadata)
print(replay.battle_performance)
print(replay.common)
print(replay.battle_frags)
print(replay.battle_economy)
print(replay.battle_xp)
```

Process all the replay files and store the results in the database

```python
from wotreplay import ProcessReplays

ProcessReplays.process_all(replay_dir='/path/to/replay/dir', 
                           db_path='path/where/to/save/the/database', 
                           db_name='wotreplay')
```
This will process the replays sequentially. 

<u>Note:</u> Once a replay has been processed and added to the database, it will not be processed again to avoid data 
duplication.

### 3. Compatibility
The replays from the following client versions have been tested. 

| Client Version        | Passed    |                      
| ---                   | ---       |
| 0.9.21                | True      |
| 0.9.22                | True      |
| 1.0.0                 | True      |
| 1.0.1                 | True      |
| 1.0.2                 | True      |
| 1.1.0                 | True      |
| 1.2.0                 | True      |
| 1.3.0                 | True      |
| 1.4.0                 | True      |
| 1.4.1                 | True      |
| 1.5.0                 | True      |
| 1.5.1                 | True      |
| 1.6.1                 | True      |
| 1.7.0                 | True      |
| 1.7.1                 | True      |
| 1.8.0                 | True      |
| 1.9.0                 | True      |

No replays before 0.9.21 have been tested due to lack of replays available. 

### 4. Data Taxonomy
Examples of data retrieved: 

* Battle metadata: [Battle Metadata Fields](https://github.com/gabriel-oana/wotreplay/blob/main/taxonomy/battle_metadata.json)
* Battle performance: [Battle Performance Fields](https://github.com/gabriel-oana/wotreplay/blob/main/taxonomy/battle_performance.json)
* Common: [Common Data Fields](https://github.com/gabriel-oana/wotreplay/blob/main/taxonomy/common.json)
* Battle frags: [Battle Frags Fields](https://github.com/gabriel-oana/wotreplay/blob/main/taxonomy/battle_frags.json)
* Battle economy: [Battle Economy Fields](https://github.com/gabriel-oana/wotreplay/blob/main/taxonomy/battle_economy.json)
* Battle xp: [Battle XP Fields](https://github.com/gabriel-oana/wotreplay/blob/main/taxonomy/battle_xp.json)

### 5.Access and rights
If you are using this on any online tools please give the appropriate credit.    

### 6.To Do
The extraction of data from replays is more or less complete. 
There are a few features to be created in the future to create the aliases of tank names and maps. 

### 7. Development

### 5. Development
To further develop this package please follow the instructions below

```shell

# Install the virtual environments and packages
python3 -m virtualenv .venv
source .venv/bin/activate
pip3 install -r requirements.txt

# Run test suite
# Tests contain unittests, coverage and linting
tox
```
