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
  
    rotating_logo = AnimatedGIF(parent, 'my_logo.gif', 0.04)  # (tkinter.parent, filename, delay between frames)
  	rotating_logo.pack()  # Packing the label with the animated gif (grid works just as well)
  	rotating_logo.start()  # Spawn thread which updates animation
  	
  		...
    
    rotating_logo.stop()  # Setting stop flag, which ends the animation
```

I made this after seeing a whole lot of questions on StackExchange on how to do this, but no real working solutions that allows
for usage together with mainloop(), which I guess a lot of people, myself included, need.

If you test this with Python2, let me know if it works ;)

##Known issues

If you get the `"RuntimeError: main thread is not in main loop"` error, you're experiencing a [known problem with Tkinter] (http://stackoverflow.com/questions/14694408/runtimeerror-main-thread-is-not-in-main-loop). Unfortunately, Tkinter is not really thread safe. You can replace Tkinter with [mtTkinter](http://tkinter.unpythonic.net/wiki/mtTkinter), but in my experience, whether or not this becomes a problem waries from case to case. It seems that if your gif animation thread makes the main Tkinter thread time out, this error occurs.

##Future work

Obviously, the Tkinter error is a big issue in many cases, so an alternative implementation is needed. Suggestions are welcome.
