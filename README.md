# AnimatedGIF
### - a Python class for animating GIFs in tkinter 
A very simple class (subclass of tkinter.Label) that displays an animated GIF in 
a label and either runs the animation in a separate thread or using tkinter's `after()`. Written in Python3 but should work
for Python2 as well (untested).

This allows using animated GIFs together with a normal tkinter mainloop() without blocking, but with caveats (see below)
Perfect for showing small animated "please wait"/"working"/"downloading" icons while doing other tasks.

*I recommend trying the non-threaded approach first. If you have stuttering in your animation, try the threaded approach*
###### Example usage (no threads):

```python

    from AnimatedGIF import *
  
    lbl_with_my_gif = AnimatedGif(parent, 'my_logo.gif', 0.04)  # (tkinter.parent, filename, delay between frames)
    lbl_with_my_gif.pack()  # Packing the label with the animated gif (grid works just as well)
    lbl_with_my_gif.start()  # Shows gif at first frame and we are ready to go
  		...
    lbl_with_my_gif.stop()  # Setting stop flag, which ends the update loop (animation)
```

###### Example usage (threading - but not recommended see below):

```python

    from AnimatedGIF import *
  
    lbl_with_my_gif = AnimatedGif(parent, 'my_logo.gif', 0.04)  # (tkinter.parent, filename, delay between frames)
    lbl_with_my_gif.pack()  # Packing the label with the animated gif (grid works just as well)
    lbl_with_my_gif.start_thread()  # Spawn thread which updates animation
  		...
    lbl_with_my_gif.stop_thread()  # Setting stop flag, which ends the animation
```

I made this after seeing a whole lot of questions on StackExchange on how to do this, but no real working solutions that allows
for usage together with mainloop(), which I guess a lot of people, myself included, need.

If you test this with Python2, let me know if it works ;)

## Known issues

If you are using the threaded aproach and get the `"RuntimeError: main thread is not in main loop"` error, you're experiencing a [known problem with tkinter](http://stackoverflow.com/questions/14694408/runtimeerror-main-thread-is-not-in-main-loop). Unfortunately, tkinter is not really thread safe. You can replace tkinter with [mtTkinter](http://tkinter.unpythonic.net/wiki/mtTkinter), but in my experience, whether or not this becomes a problem varies from case to case. It seems that if your GIF animation thread makes the main tkinter thread time out, this error occurs. This isn't really unique to Tkinter, but more a general issues with gui frameworks in Python.

The "correct" way of using this class is to run a `update()` and `update_idletasks()` loop while the task you are waiting for run in a thread. This usually works better than putting the animation in a thread, at least if the task isn't making updates to the window.

Of course, the simple way of doing it is using the non-threaded `stop` and `start` methods, which uses an "after()-loop", but in some cases, especially where the program is busy, the animation can get very choppy, as `after()` does not guarantee timely execution. Which is fine in some cases and not in others. Use either approach as you see fit.

## License

AnimateGIF is released under the MIT license (https://opensource.org/licenses/MIT)
