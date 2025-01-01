# Animating in Fragmotion
 


With a little bit of reading, you can start animating in 20 minutes, or less! Let's begin by opening Fragmotion!

- Depending on your screen size, and customizations some interface options may look different.


NOTE: This guide uses game files to teach the sheer basics of animation in Fragmotion, be sure to make a backup of any file you modify, or you will need to redownload the game. The animation process is the same when making actual mods. This guide does NOT teach you how to create a proper mod, please reference (Insert mod XML guide here). Enjoy!

### Camera, Common Interface Options

In the middle of the screen you will see a Grid, let's call this a "Field". It's where we will see your character on screen!
Pressing right click allows you to rotate the camera, if you right click in middle it'll rotate kind of how you expect it to. 
If you right click the outside however it will rotate in a different way, kind of like a plane rotates.
If you middle click the screen you are able to move around when dragging your mouse.

![A1](img/A1.png)

- Right click to Rotate
- Middle Click to Move


See those yellow people at the top?
Selecting 3D let's you view a character as if it were in the game.
The other yellow "people" are for different views feel free to click on them, and see what they do.

![A2](img/A2.png)

- Yellow People control Camera Angles
- 3D is similar to the in game Camera
- Left, Right, Top, Bottom, Forward, and Backward are for Bio, and Victory Animations

Say you accidentally bring up a bunch of yellow dots, these are called "Vertices". You can enable, or disable them via the Green dots at the top of your interface.

![A12](img/A12.png)

- The Green dots are Vertices
- Vertices represent the triangles that make up your character
- You can turn them off with the FOUR green dots at the top

If you have blue dots, you can disable them via the Skull next to the green dots. These are your characters "Skeleton".

![A13](img/A13.png)

Now that you know these common buttons, let's open a character!

### Setting up a Character (Model)

If you want to edit a character, File > Open > Sonic World DX > Data > Characters > 3 letter name > Model > model.b3d.

![A51](img/A51.png) ![A52](img/A52.png) ![A53](img/A53.png)
![A54](img/A54.png) ![A55](img/A55.png) ![A56](img/A56.png)

So here we've opened Shadow the Hedgehog.
The character will be blacked out if using a model from SWDX.

![A3](img/A3.png)

- B3D Files are a "lossy" format used by Blitz3D, i.e SWDX.
- You can also open FBX 2009, OBJ, DAE, and UGH files among many others
- When modifying your character alway save as .UGH, save as .B3D when you're done
- All characters are blacked out because of "Reference Maps" which create layers on a character that show up Black in fragmotion
- MODEL.b3d = In game Model
- BIO.b3d = Character Select Model

On the right, there's a section called "Model". Click on that.
You'll see the Model,Smoothing Groups, Textures, and Materials menu.

![A4](img/A4.png)

You can expand Materials with the little plus button to the left, and a material object the same way.
Click on a grey box.

![A5](img/A5.png)
![A6](img/A6.png)

Example of Materials

![A7](img/A7.png)

Under properties you will see "Texture Layer" and "Type". Select Bumpmap under the type. Your material will change from a LIGHT grey box to a 3D grey box. You should see some color on the model now!

![A9](img/A9.png)
![A10](img/A10.png)
![A11](img/A11.png)

Now that we can see our character, let's set up our Interface, and Tools!

### Setting up the interface

Let's go to the "Tools" menu, and select "Show Tree"

![A14](img/A14.png)

For now you can select "Hide" since we aren't using the Tools

![A15](img/A15.png)

While were here you can grab the "PADDED" bar that's grey, and drag the tool menu to the far left of your screen to expand your view of it, and make the workspace easier to use. You are able to drag any workspace to any location on your screen, but for the purposes of this tutorial I use the left side for "TOOLS"

Feel free to customize it to your liking.

![A16](img/A16.png)
![A17](img/A17.png)

- We setup our Tool Tree
- Selected Hide so we don't activate anything
- Changed our UI to better fit our needs

### Basic Animating interface

Let's move on to something, more interesting.
You can click on the Animations tab to view animations.

![A18](img/A18.png)

There is a media player on the bottom of the screen.
It will play the animation forward, backward, or frame by frame
a frame being a single image.

![A19](img/A19.png)


Example here, of Frame 8 , or Image 8 of Shadow walking.

![A20](img/A20.png)

This bar will show you the MAX number of frames in this "Animation", which is essentially just a video, in the RED box.
The GREEN box is where the animation starts, and the WHITE is your current frame, or image
Let's look at the blue lines again, it might hurt your eyes, or look hideous, but they are important to the way Animating works within SWDX.
![A21](img/A21.png)

So at the top "Show Skeleton"

![A22](img/A22.png)

Then double click your first animation, the "IDLE".
This weird menu with a lot of scary dots will show up.
These are called keyframes, and they aren't really important to us yet, but will be later.
On the left of this scary box you can see Skeleton's bones spread out in a "Tree".

![A23](img/A23.png)
![A24](img/A24.png)

If you click on any of the parts of the skeleton, say the neck, you'll see a red dot, which is the bone they define as "NECK" in your "FIELD", it has some green tree branches.
These are all of the bones attached to the Neck.
So when Shadows Neck moves, these bones move with it.
You can see that when you play the animation.

![A25](img/A25.png)

- You have a Media player that can control the "Animation"
- WHITE box shows the CURRENT image
- GREEN box shows the FIRST image
- RED box shows the LAST image
- "Animations" are really just "images" that you put together to make a "Video"
- These "Videos" play in the game under certain names like "IDLE"
- You can open a box that shows you your "images" by double-clicking an "Animation", The Keyframe Editor
- The Keyframe Editor shows you a list of your bones that you can select
- Selected bones show up in the "Field" as RED dots, connected bones show up as GREEN dots



### Explaining Skeletal Animation Widget

Let's go back to Tools. If you scroll down you'll see "Skeletal Animation".
This is how we are going to modify our animations, or even create new ones
You will click on the "Skeletal Anim Widget".

![A26](img/A26.png)

This circle will show up, you can drag it by left clicking the transparent area.
So you're able to move it out of the work space as I have here.
You have 6 tools on this "Widget", the "Bone Select" tool, which allows you to select a blue circle, or "Bone". 

![A27](img/A27.png)

The "Translate" tool, which allows you to move a bone in any direction.
You just select translate, and it's as simple as holding left click, and dragging!

![A28](img/A28.png)



Then you have the "Rotate" tool, which as it suggests allows you to rotate a bone

![A29](img/A29.png)


We skip the Rotate key local tool, it isn't important for what we're learning currently.
The "scale key" tool allows you to change the size of an object!
Currently our directions are unlocked so when testing this out you may be confused as to why it's so wonky.
We also skip inverse kinematics, I ACTUALLY have no clue what that does, feel free to mess with it though.


![A30](img/A30.png)

See these colors, they represent your X, Y, Z which are your Cardinal Directions.

![A31](img/A31.png)

Select the _L ttool, and colorful lines will show up representing X, Y, Z.
We call these "Axis".

![A32](img/A32.png)



Mousing over the colors on your triangle you can see we have of course X Y Z, and it says "restrict" which means movement of said object will only occur on those "Axis"
The yellow represents "Free" movement in any direction then the other colors are essential diagnal movement.

When animating in SWDX we usually use Red, Blue, and Green. Yellow itself isn't very accurate.
NOW everytime you swap tools it will remember the LAST used color you've chosen
for that tool. I've locked translate(movement) ,now I'm going to move shadows nose on the red axis as an example then swap to rotate.

![A33](img/A33.png)
You can see that when swapping to Rotate, it reverts to Yellow, free movement.
Your previous tools XYZ restriction does not transfer to a new tool.
However when swapping back your tools will remember their last used restriction.
![A34](img/A34.png)

Okay now that we've covered the Widget, and it's many useful toolbelt like applications, let's look at our Tool properties!

I currently have the "Translation" tool selected.
Here you see "Keyframe Translation Tool".
Yours may look slightly different then mine due to some bugs with my version.
You can ignore your XYZ coordinate, these are used in more advanced placement options for the character. Feel free to mess around if you would like.

Applyto allows you to select where an "Image" or "Frame" edit you make goes
You can open it's dropdown menu. Current frame is the image you are on now, frames before is everything before your image, after is everything after it's a bit self explanatory. Loop will be whatever the green, and red box say at the bottom on the player. Then All frames is every image, this is useful for when you want a characters eyes to always be open, you just make the edit on "All frames".

![A35](img/A35.png)

The last real property that matters is AffectChildren, and a property called Uniform which isn't shown here.

Affect Children will allow the red bone you have selected to move other bones that are connected via the Green tree branches we saw before. This is useful to have on so you don't have to rotate every single bone, it does have instances where turning it off can be useful however, for instance moving a kneecap by itself.

Uniform keeps everything at the same scale when stretching pieces out. That way stuff doesn't look wonky like it did when I scaled Shadow's head earlier.



![A36](img/A36.png)

- Skeletal Animation Tool is our main Animation Tool
- Translate Moves an Object, Rotate rotates an object, and Scale can make it bigger, or smaller.
- RED represents Y, BLUE represents X, and GREEN represents Z, you can lock tools to "Axis"
- Tools remember their locks
- Applyto property allows you to select which frame your modifications affect
- Uniform property changes whether your scale is Uniform, or not
- AfffectChildren property changes whether the GREEN bones move with a RED bone, or not.



### Keyframes

So you've been messing around while reading this, how do we retain the actions, or animations you've been making?

For this we go back to the "Keyframe Editor" by double clicking your animation.

You'll see a Red Line, it's currently on "Image" 1 for me or column 1
On the left you'll see these green boxes that represent rotation, translation, and scale which we messed around with earlier. Anything I do to this "Image" will create a new yellow bubble on column 1 beside rotation, translation, or scale besides whatever bone I have selected.

![A37](img/A37.png)



I've used right-click + Hold, and Drag to make a box around ALL of these bubbles, then I'm going to delete them using my DEL key on the keyboard. Any bubble that is BLUE is selected. Now I'm going to press play, and my neck no longer moves between "Images"!

![A38](img/A38.png)



![A39](img/A39.png)
Image 2 the head no longer flips back, but his nose does plop back down.

Let's make shadows head to fully rotate for some nightmare fuel!
![A40](img/A40.png)

I'm going to move to the last frame with my red line, by left clicking on the number bar at the top of the screen, you can also move frames with the arrows at the bottom of the play bar, or by dragging the little bar on the timeline.


![A41](img/A41.png)

Let's finally learn more about the Keyframe Editor.
We call the Yellow Bubbles, Keyframes.
Now let's look towards the top of the Keyframe Window.

You'll see some Keys,the first 2 keys let you set your model to their default values, i.e tposing. The last 2 let you create either a single bubble, or a line of bubbles
via left clicking empty space.

There are also two double arrows, the one without red lines let you slide individual bubbles.
The one with red lines, moves all of your bubbles.

![A42](img/A42.png)

So here I've created some bubbles on the final frame using the red dot Key.
I'm going to click the double arrow WITHOUT the red sides. We're swapping over to this mode so we don't keep making bubbles. 

![A43](img/A43.png)

Now we move to frame 9 of our idle.

![A44](img/A44.png)

Here you can see I have moved shadows head on this "Image", or "Frame", a bubble has shown up under the 9th frame of the keyframe editor in the rotation section.

![A45](img/A45.png)

You'll notice that the image is moving by itself without you actually creating any new keyframes as we move along the frames,this is called interpolation. The program determines the path of the characters where all these bubbles are empty. It essentially fills in the blanks for you!


![A46](img/A46.gif)

This doesn't quite get the head to rotate, but it does show how keyframes work. These are the basic essentials needed to animate in fragmotion, for a full rotation we're going to move to the middle of frame 9, and 17. I've gone ahead and rotated Shadows head creating a new keyframe.


![A47](img/A47.png)

Now the animation has filled itself out!

![A48](img/A48.gif)


It's important that every animation have atleast a keyframe in the first image, and the last image,if not your animations can actually merge into each other.

One last thing of note This top bone that has empty keyframes, will always be deleted when you export your character.

DO NOT animate on this bone you will lose your animation.

If you want to rotate a character in a circle, please try, and use their Hips!

![A49](img/A49.png)

This is how animating works in fragmotion! It's super easy, and simple to do :)

- You can select bubbles using LEFT, or RIGHT click
- Empty bubbles automatically fill themselves in when playing an animation they're just invisible
- Interpolation, and Keyframes are your most powerful tools when animating



### Final Steps

When you're done you can goto File> Export, and see your handiwork in game, be sure to backup the original model.b3d, and to save as a Blitz Basic 3D Files (.b3d).

- MODEL.b3d = In game Model
- BIO.b3d = Character Select Model

BOOM we're in game!

![A50](img/A50.gif)


