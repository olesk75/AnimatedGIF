""" AnimatedGIF - a

Copyright (c) 2016 Ole Jakob Skjelten <olesk@pvv.org>

Released under the terms of the GNU General Public License, version 3
(https://gnu.org/licenses/gpl.html)

"""
from threading import Thread
import tkinter as tk
import time


class AnimatedGif(tk.Label):
	"""
	Class to show animated GIF file in a label
	:root: Tk parent
	:gif_file: path and filename of animated gif
	:delay: delay in seconds (or parts of seconds) between each frame

	Use start() method to begin animation, and set the stop flag to stop it
	"""
	def __init__(self, root, gif_file, delay=0.04):
		tk.Label.__init__(self, root)
		self.root = root
		self.gif_file = gif_file
		self.delay = delay  # Animation delay - try low floats, like 0.04
		self.gif = tk.PhotoImage(file=gif_file)

		self._num = 0
		self.animation_thread = Thread()
		self.stop = False  # Thread exit request flag

	def start(self):
		self.animation_thread = Thread(target=self._animate).start()

	def _animate(self):
		while self.stop is False:
			try:
				time.sleep(self.delay)
				self.gif = tk.PhotoImage(file=self.gif_file, format='gif -index {}'.format(self._num))
				self.configure(image=self.gif)
				#self.image = self.gif  # We anchor image object to avoid grabage collection removing it

				self._num += 1
			except tk.TclError:
				self._num = 0