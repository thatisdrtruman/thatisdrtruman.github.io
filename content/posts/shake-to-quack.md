+++
title = 'Shake to Quack'
date = 2024-06-16T21:35:31+01:00
draft = false
tags = ['game', 'development', 'design', 'fun', 'app','mobile', 'update', 'web']
featured_image = "https://raw.githubusercontent.com/thatisdrtruman/shake_to_quack_html/master/Shake_To_Quack.144x144.png"
description = "Glu Glu! Is the Tokyo Disneyland Quack Stick too expensive? Here's the free alternative. Just press the white play button and watch it shake and quack."
categories = ['Design', 'App', 'Android', 'iOS', 'Internet', 'Web','Tech']
+++
{{< addtoany >}} 
🦆🦆

Play it here: https://thatisdrtruman.github.io/shake_to_quack_html/

For Android users, [Download](https://thatisdrtruman.github.io/shake_to_quack_html/Shake-To-Quack-v1.apk)

You can also see how I made 'Shake To Quack' with Godot 3.5.3 with C# Support.

https://github.com/thatisdrtruman/shake-to-quack

## How I decided to make it

One day on Tiktok, I came across a Tokyo Disneyland Glu Glu Quacking Stick for the theme park's Quacky City event, celebrating Donald Duck's 90th anniversary.

For a while, I wanted to make a game or an app on Godot and with C#, and I decided to prove myself I can code in C#, with an app version of the Stick.

1. I researched on Quack Stick videos to find the one that was most audibly clear, settling on: https://www.youtube.com/watch?v=vrXCYUOBNK4 (Tokyo Disneyland Haul: Donald Duck's Quacky City Merch! by Wandering with Manami: Tokyo Disney Travel Guide)

2. I found the yellow duck of the stick, cut out the duck with paint.net. Then for the icon, added shivelling lines.

3. Downloaded the audio version of the youtube video, open Audacity and spliced the 'Glu Glu' noises, export them to OGG. 

4. I set a new project called 'Shake To Quack' on Godot 3.5.3 with C#.

5. Placed the duck, and noise files into specified folders.

6. Added the disclaimer and the button to quack, setting the ManualTouchButton to support mobile and PC presses.

7. Name the OGG Files 1-5 so that the programme can run a random noise based on the sound file name.

8. Set the audio and sprite classes to their respective nodes.

9. Activated C# scripts for the sprite, and the button.

10. With AI and YouTube tutorials on Godot 3 C#, I learnt C# and Godot fundamentals to hear the quacking sounds and the shaking effect.

11. I then uploaded the raw C# version on Github.

12. For the Web Export, I had to read more tutorials, documentations and AI help to learn how to export to Github and set up Github Pages so that the programme can run.

At the time I developed the app, Godot 4 could not support web export and C#, so I settled for Godot 3.5.3. When Godot 4 supports web export and C#, I will migrate to Version 4.

13. Exported the C# app into HTML5, install npm, use uglify and gzip to compress the files, keeping the original and the compressed version.

For gzip, I used 7-Zip and archive the big files then used AI to help the HTML file to use the script to both support the big, original files and the smaller, compressed gzip files.

14. Rename the html files to index so that Github Pages can automatically load the app.

15. Put in source control commands to help upload the files onto a new repo, then setup Github Actions with a YAML file to automatically set up the static website when I make a new Git commit. Now I can do it on the terminal or on the Visual Studio Code's Source Control section.

16. Test the duck on my smartphone and on PC. Determined the duck was too far right to be suitable on smartphone.

17. So made a new version where the button moved down, and the duck moved to the left. Repeated step 13-16, and concluded I could see the duck.

18. Set up the Android export. Installing Android Studio, JDK, set up the environments, follow Godot's document, go into the JDK's binary directory, generate a debug and game keystore using keytool in the directory, place both keystores into the .android directory in my name, setup the name and passwords for both files.

19. Import both keystores' store location, set the user names and password for each and then exported the Android App.

20. Inserted the Android APK into the 'Shake To Quack HTML' repo, so now you can download it.

### That was a lot of words, but at least now you know how to make a Godot C# App, and export them.
