""" AnimatedGIF - a

Copyright (c) 2016 Ole Jakob Skjelten <olesk@pvv.org>

Released under the terms of the GNU General Public License, version 3
(https://gnu.org/licenses/gpl.html)

"""
from threading import Thread
import time
try:
	# for Python2
	import Tkinter as tk
except ImportError:
	# for Python3
	import tkinter as tk


class AnimatedGif(tk.Label):
	"""
	Class to show animated GIF file in a label
	Use start() method to begin animation, and set the stop flag to stop it
	"""
	def __init__(self, root, gif_file, delay=0.04):
		"""
		:param root: tk.parent
		:param gif_file: filename (and path) of animated gif
		:param delay: delay between frames in the gif animation (float)
		"""
		tk.Label.__init__(self, root)
		self.gif_file = gif_file
		self.delay = delay  # Animation delay - try low floats, like 0.04

		self._num = 0
		self.animation_thread = Thread()
		self.stop = False  # Thread exit request flag

	def start(self):
		self.animation_thread = Thread(target=self._animate).start()

	def stop(self):
		self.stop = True

	def _animate(self):
		while self.stop is False:
			try:
				time.sleep(self.delay)
				self.gif = tk.PhotoImage(file=self.gif_file, format='gif -index {}'.format(self._num))
				self.configure(image=self.gif)
				self._num += 1
			except tk.TclError:
				self._num = 0
