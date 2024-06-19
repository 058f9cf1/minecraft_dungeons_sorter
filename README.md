# Minecraft Dungeons Sorter
A tool for sorting a Minecraft Dungeons inventory by item type, then alphabetically.

## Dependencies
Requires Python 3 to be installed.

## Installation
Open a terminal and run the following command (requires git to be installed): 
```
git clone https://github.com/058f9cf1/minecraft_dungeons_sorter.git
```
Alternatively, download the repo as a zip and unzip it.

## Usage
> [!WARNING]
> Your Minecraft Dungeons save file must first be decrypted. Use [DungeonTools](https://github.com/HellPie/DungeonTools) to do this.

Open a terminal and run the following commands: 
```
cd minecraft_dungeons_sorter/src/
python main.py <path/to/savefile>
```
>[!NOTE]
>If no save file is specified, the program will search for a decrypted save file in `%USERPROFILE%\Saved Games\Mojang Studios\Dungeons`.

A new decrypted save file with the sorted inventory will be created in the same location as the unsorted one. Re-encrypt this new save file then remove "_sorted" from the file name.
