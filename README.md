# Alarm Clock

The exe file present here is a windows compatible desktop app. One needs visual studio redistributable to run it.
To run it on your pc, simply download exe file and the music file and keep them is same folder and run it.

The code is given in the file clock.py, one song is also mentioned and this song(or another song if you want to change) and the exe file need to be in same folder to work.
We have used tkinter for gui, playsound for ringing the alarm and datetime modules.

The app has a running 24-hr format clock on top and below it we can set the alarm and press ok. The system will count till that time and ring the alarm at that time. After 
completely ringing the alarm, it resumes back the clock and you can set the next alarm. While alarm is on, the label below shows "Alarm set" and the loading dots. If you enter 
invalid time it shows "Enter correctly". We have a cancel button for cancelling the alarm.

You can also change the alarm song by specifying its full name(with extension) in the text field adjacent to ok button, the song must be in the same folder as the exe file.
By default "alone_marshmello.mp3" file is used.
