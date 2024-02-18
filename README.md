# Minecraft Dungeons Sorter
A tool for sorting a Minecraft Dungeons inventory by item type, then alphabetically.

## Dependencies
Requires Python 3 to be installed.

## Usage
> [!WARNING]
> Your Minecraft Dungeons save file must be decrypted first. Use [DungeonTools](https://github.com/HellPie/DungeonTools) to do this.

Open a terminal and run the following commands: 
```
git clone https://github.com/058f9cf1/minecraft_dungeons_sorter.git
cd minecraft_dungeons_sorter/src/
python main.py <path/to/savefile>
```
>[!NOTE]
>If no save file is specified, the program will search for a decrypted save file in `%USERPROFILE%\Saved Games\Mojang Studios\Dungeons`.

A new decrypted save file with the inventory sorted will be created in the same location as the unsorted one. Re-encrypt this new save file then remove "_sorted" from the file name.
