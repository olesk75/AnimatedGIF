AnimatedGIF - a class for showing animated GIFs
========================

A very simple class (subclass of tkinter.Label) that displays an animated GIF in 
a label and runs the animation in a separate thread. Written in Python 3.4, but should 
work for all 3.x version, and 2.x with a minor rewrite.

This allows using animated GIFs together with a normal mainloop() without blocking.

Example usage

```python

    from AnimatedGIF import *
  
    rotating_logo = AnimatedGIF(parent, 'my_logo.gif', 0.04)  # (tkinter.parent, filename, delay between frames)
  	rotating_logo.pack(fill=tk.BOTH)  # Packing the label with the animated gif (grid works just as well)
  	rotating_logo.start()  # Spawn thread which updates animation
  	
  		...
    
    rotating_logo.stop = True  # Setting stop flag, which ends the animation
```

I made this after seeing a whole lot of questions on how to do this, but no real working solutions that allows
for usage together with mainloop(), which I guess a lot of people, myself included, need.
