#AnimatedGIF
### - a Python class for animating GIFs in tkinter using threads
A very simple class (subclass of tkinter.Label) that displays an animated GIF in 
a label and runs the animation in a separate thread. Written in Python3 but should work
for Python2 as well (untested).

This allows using animated GIFs together with a normal tkinter mainloop() without blocking.
Perfect for showing small animated "please wait"/"working"/"downloading" icons while doing other tasks.

######Example usage:

```python

    from AnimatedGIF import *
  
    lbl_with_my_gif = AnimatedGIF(parent, 'my_logo.gif', 0.04)  # (tkinter.parent, filename, delay between frames)
  	lbl_with_my_gif.pack()  # Packing the label with the animated gif (grid works just as well)
  	lbl_with_my_gif.start()  # Spawn thread which updates animation
  	
  		...
    
    rotating_logo.stop()  # Setting stop flag, which ends the animation
```

I made this after seeing a whole lot of questions on StackExchange on how to do this, but no real working solutions that allows
for usage together with mainloop(), which I guess a lot of people, myself included, need.

If you test this with Python2, let me know if it works ;)

##Known issues

If you get the `"RuntimeError: main thread is not in main loop"` error, you're experiencing a [known problem with Tkinter] (http://stackoverflow.com/questions/14694408/runtimeerror-main-thread-is-not-in-main-loop). Unfortunately, Tkinter is not really thread safe. You can replace Tkinter with [mtTkinter](http://tkinter.unpythonic.net/wiki/mtTkinter), but in my experience, whether or not this becomes a problem waries from case to case. It seems that if your gif animation thread makes the main Tkinter thread time out, this error occurs.

There is a slightly more complex solution though, which involves [running all UI code in the main thread, and let the writers write to a Queue object](http://effbot.org/zone/tkinter-threads.htm). Though this clearly works and solves the problem, it also means that, unless you are using threads for other tasks, you would have to rewrite your entire program just to include animated GIFs. That might be a tiny bit overkill to say the least...

##Future work

Obviously, the Tkinter error is a big issue in many cases, so an alternative implementation is needed. Suggestions are welcome.
