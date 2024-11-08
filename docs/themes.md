# Themes
## settings.xml

```xml title="settings.xml" linenums="1"
--8<-- "settings.xml"
```
Each theme uses settings.xml to determine various functionality aspects of the theme, such as what HUD layout it should use, or what colour the special gauge is. A default settings.xml should look like this:
``` xml
<hud style=””/>
```

* Alters HUD placement in-game to closest match any of the following options.
* DX, Legacy, SA1, SA2, Heroes, Shadow, 06, Unleashed, Colours, Colors, Generations, Forces, Frontiers, Classic

``` xml
<heroes spinner=””/>
```

*  Set to 1 to enable separate spinners for each team member

``` xml
<round transition=””/> 
```

* Set to 1 to enable the round transitional image from heroes

``` xml
<logo style=””/> 
```

* Set to 1 to enable the R8 logo fly-in animation

``` xml
<victory timer=””/> 
```

* (CURRENTLY NOT FUNCTIONAL)

``` xml
<author is=””/> 
```

* Write down the creator of the theme here

``` xml
<bubbles on=”” amount=”” chance=”” speed=””/> 
```

* See SA2 theme for details

``` xml
<scrolling on=”” speed=”” alpha=””/> 
```

* See SA2 theme for details

``` xml
<gauge r=”” g=”” b=”” fr=”” fg=”” fb=””/>
``` 

 * Set the normal and full gauge colours

``` xml
<sounds life-pause=”” loop-spin=””/> 
```

* Pauses music on life gain or loop the spin sound

``` xml
<background x=”” y=””/>
``` 

* Sets the background resolution

Feel free to look at any base game theme’s settings xml and folder structure to figure out how they function. Remember in-game you can type `themedata` into the console to reload the theme’s settings without having to exit the game.
