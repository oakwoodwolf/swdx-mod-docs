# Mods.xml

```xml title="mods.xml" linenums="1"
--8<-- "mods.xml"
```

This file is the file that tells the game where to look for mods to load. If it is missing, the game auto-generates a new one on startup. If you don't want to organize files, you can get away with not touching it, as they are all set to search in the Mods folder. The only modding that outright requires this folder is Voice Mods.

However, when you install many mods, it becomes hard to distinguish them, so you might want to organise them into folders.

You can edit them using any text editor, preferably a code editor such as [:material-microsoft-visual-studio-code: VSCode](https://code.visualstudio.com/).

## Stages

```xml
<stages folder=""/>
```

This line determines where it can look for stages. Since the folder is empty, it will find any extracted stage in the mods folder.
If you want to organize stages, you can create a new folder, name it whatever you want, and put the stages there. Then fill that folder in the field:

```xml
<stages folder="KodyCrimson"/>
<stages folder="Drox342"/>
<stages folder=""/>
```

A common use case is seperating them into folders by Stage author. You can have this line multiple times in the xmls, as long as the mods are all in that folder.
They will be loaded into the game in the order they will appear in the xml, so:

- It will load all of the stages in the `KodyCrimson` folder first, in alphabetical order.
- It will then load all of the stages in the `Drox342` folder, in alphabetical order.
- Finally, it will load all of the stages in the `Mods` folder, in alphabetical order.

This way of organisation works with every field except for Voice mods.

The maximum possible amount of stages loaded into the game is `996`, including official stages.

## Characters

```xml
<characters folder=""/>
```

This line determines where it can look for characters. Since the folder is empty, it will find any extracted character in the mods folder.
If you want to organize characters, you can create a new folder, name it whatever you want, and put the characters there. Then fill that folder in the field:

```xml
<characters folder="Legacy Character Pack"/>
<characters folder="Sonic 06 Character Pack"/>
<characters folder=""/>
```

A common use case is modpacks, if you download a character pack, and want to disable them, its easier to keep them in the same folder as each other:

- It will load all of the characters in the `KodyCrimson` folder first, in alphabetical order.
- It will then load all of the characters in the `Drox342` folder, in alphabetical order.
- Finally, it will load all of the characters in the `Mods` folder, in alphabetical order.

This way of organisation works with every field except for Voice mods.

The maximum possible amount of characters loaded into the game is `64`, excluding official characters.
Upcoming versions may increase that limit.

## Themes

```xml
<themes folder=""/>
```

This line determines where it can look for themes. Since the folder is empty, it will find any extracted theme in the mods folder.
If you want to organize themes, you can create a new folder, name it whatever you want, and put the themes there. Then fill that folder in the field:

```xml
<themes folder="My Themes"/>
```

You can also organise it into multiple folders like the previous two.

The maximum possible amount of themes loaded into the game is `8`, excluding official themes.
Upcoming versions may increase that limit.

There is a known bug in 1.2.7 that breaks scrolling for custom themes, select the number of the theme on the official theme, switch to custom, then select it, to pick any theme other than the first.

## Sound Mods

```xml
<sounds folder=""/>
```

This line determines where it can look for sounds. Since the folder is empty, it will find any extracted sound mods in the mods folder.
If you want to organize sound mods, you can create a new folder, name it whatever you want, and put the sound mods there. Then fill that folder in the field:

```xml
<sounds folder="Sound Packs"/>
```

If you have multiple, the priority of what sounds to mod is bottom-to-top.

Sound mods are rare, as usually theyre included with Stages and Theme mods. The game prioritises which modded sound to use in this order:

1. Stage
2. Sound Mod
3. Theme

Any stage that overwrites a sound will be the one you will hear, i.e. a unique crumbling platform sound in a stage. If the stage doesnt mod the sound, it moves down the chain, etc.

## Object Mods

```xml
<objects folder=""/>
```

This line determines where it can look for object mods. Since the folder is empty, it will find any extracted object mods in the mods folder.
If you want to organize object mods, you can create a new folder, name it whatever you want, and put the object mods there. Then fill that folder in the field:

```xml
<objects folder="Object Mods"/>
```

If you have multiple, the priority of what object to mod is bottom-to-top.

Sound mods are rare, as usually theyre included with Stages and Theme mods. The game prioritises which modded sound to use in this order:

1. Stage
2. Object Mod
3. Theme

Any stage that overwrites a mod will be the one you will hear, i.e. a classic spring in Green Hill. If the stage doesnt mod the object, it moves down the chain, etc.

## Costumes

```xml
<costumes folder=""/>
```

This line determines where it can look for costumes. Since the folder is empty, it will find any extracted costumes in the mods folder, provided it contains a `costumes.xml`.
If you want to organize costumes, you can create a new folder, name it whatever you want, and put the costumes there. Then fill that folder in the field:

```xml
<costumes folder="Stylized Sonic"/>
<costumes folder="Danganronpa Trigger Happy Havoc Pack/Costumes"/>
```

The organization is handled by the mod's `costumes.xml`. Many already come with one, but some exclude it and would need one to be created. Check [costumes.xml](index.md) for detailed information.

Like [Stages](#stages) and [Characters](#characters), it adds mods top-to-bottom, so if I check Sonic's Mod costumes, I will see Stylized Sonic on the first slot, and Naegi Sonic as the second slot.

The maximum possible amount of modded costumes loaded per-character is `10`
Upcoming versions may increase that limit.

## Voice Mods

```xml
<son folder=""/>
```

All the remaining lines that start with a 3-letter word are voice mod slots. These are not auto-detected, so if left blank, the vanilla voices are used.
If you want to modify a character's voice, you have to specify a folder with the character ID.

```xml
<son folder="Jason Griffith Sonic Voice"/>
```

This will load the voice mod with that name in the Mods directory. If you want to sort it into its own folder, you can type it as follows:

```xml
<son folder="4 Kids Voice Pack/Jason Griffith Sonic Voice"/>
```

Provided theres no other folders in `Jason Griffith Sonic Voice`, only the required `.ogg` files, The voice should load in-game.

