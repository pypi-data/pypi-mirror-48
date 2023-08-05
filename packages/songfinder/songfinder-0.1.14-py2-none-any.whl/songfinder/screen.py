# -*- coding: utf-8 -*-
from __future__ import division

import copy
import warnings
import sys
import Tkinter as tk
import screeninfo

from songfinder import commandLine
from songfinder import exception
from songfinder import globalvar

class Screen(object):
	def __init__(self, w=720, h=480, pw=0, ph=0, full=None):
		if not full:
			self.full = ''.join([str(w), 'x', str(h), '+', str(pw), '+', str(ph)])
		else:
			self.full = full
		self._setScreen()

	def _setScreen(self):
		list_fois = self.full.split('x')
		if len(list_fois) != 2:
			warnings.warn('Erreur de lecture de la resolution de l''ecran, '
					'le format des donnees n''est pas valide : "%s". '
					'Le format valide est : "wxh+pw+ph'%self.full)
			self._defaultScreen()
		else:
			list_plus = list_fois[1].split('+')
			if len(list_plus) != 3:
				warnings.warn('Erreur de lecture de la position de l''ecran, '
										'le format des donnees n''est pas valide : "%s". '
										'Le format valide est : "wxh+pw+ph'%self.full)
				self._defaultScreen()
			else:
				try:
					self.w = int(float(list_fois[0]))
					self.h = int(float(list_plus[0]))
					self.pw = int(float(list_plus[1]))
					self.ph = int(float(list_plus[2]))
				except ValueError:
					warnings.warn("Erreur de lecture des donnees de l'ecran")
					self._defaultScreen()

	def _defaultScreen(self):
		self.w = 720
		self.h = 480
		self.pw = 0
		self.ph = 0

	def set_w(self, new_w):
		try:
			self.w = int(new_w)
			self.set_full()
		except ValueError:
			warnings.warn('Error while converting resolution/position to int:\nnew_w')

	def set_h(self, new_h):
		try:
			self.h = int(new_h)
			self.set_full()
		except ValueError:
			warnings.warn('Error while converting resolution/position to int:\nnew_h')

	def set_wp(self, new_wp):
		try:
			self.wp = int(new_wp)
			self.set_full()
		except ValueError:
			warnings.warn('Error while converting resolution/position to int:\nnew_wp')

	def set_hp(self, new_hp):
		try:
			self.hp = int(new_hp)
			self.set_full()
		except ValueError:
			warnings.warn('Error while converting resolution/position to int:\nnew_hp')

	def set_full(self):
		self.full = ''.join([str(self.w), 'x', str(self.h), '+', str(self.pw), '+', str(self.ph)])

	@property
	def ratio(self):
		if self.h != 0:
			ratio = self.w/self.h
		else:
			ratio = 1
		return ratio

	def __str__(self):
		self.set_full()
		return self.full

	def __repr__(self):
		self.set_full()
		return self.full

class Screens(object):
	def __init__(self):
		self._screens = []
		self._maxScreens = sys.maxsize

	def __getitem__(self, index):
		if len(self._screens) == 0:
			self.update()
		if index >= len(self._screens):
			raise Exception('You asked for screen number %d but '
				'only %d screens are available.'%(index, len(self._screens)))
		return self._screens[index]

	def __len__(self):
		if len(self._screens) == 0:
			self.update()
		return len(self._screens)

	@property
	def maxScreens(self):
		return self._maxScreens

	@maxScreens.setter
	def maxScreens(self, value):
		if self._maxScreens != value:
			self._maxScreens = value
			self.update()

	def update(self):
		del self._screens[:]
		monitors = screeninfo.get_monitors()
		if len(monitors) > 0:
			for monitor in monitors:
				if len(self._screens) == 0:
					ratio = 0.9
				else:
					ratio = 1
				self._add(Screen(monitor.width, monitor.height, \
							monitor.x, monitor.y), ratio=ratio)
		else:
			warnings.warn('Screeninfo did not output any screen infos')
			if globalvar.myOs == 'windows':
				self._getWindowsScreens()
			elif globalvar.myOs == 'ubuntu':
				if not self._getLinuxScreens():
					self._getByTopLevelScreens()
			elif globalvar.myOs == 'darwin':
				xrandr = commandLine.MyCommand('xrandr')
				try:
					xrandr.checkCommand()
				except exception.CommandLineError:
					self._getMacOsScreens()
				else:
					self._getLinuxScreens()
			else:
				warnings.warn("No screen found, OS is not supported.")
				self._getLinuxScreens()

			if len(self._screens) > self._maxScreens:
				del self._screens[self._maxScreens:]

		print("Using %d screens: "%len(self._screens))
		for screenCouple in self._screens:
			print('	Full: %s, Usable: %s'\
				%(str(screenCouple[0]), str(screenCouple[1])))

	def _getWindowsScreens(self):
		test = tk.Toplevel()
		test.wm_attributes('-alpha', 0)
		test.withdraw()
		test.update_idletasks()
		test.state('zoomed')
		test.withdraw()
		ww1 = test.winfo_width()
		hh1 = test.winfo_height()
		test.overrideredirect(1)
		test.state('zoomed')
		test.withdraw()
		w1 = test.winfo_width()
		h1 = test.winfo_height()
		posw1 = test.winfo_x()
		posh1 = test.winfo_y()
		test.state('normal')
		test.withdraw()
		self._add(Screen(w1, h1, posw1, posh1), \
				usableScreen=Screen(ww1, hh1, posw1, posh1))
		# Scan for second screen
		test.overrideredirect(1)
		for decal in [[w, h] for w in [w1, w1//2, -w1//8] for h in [h1//2, h1, -h1//8]]:
			test.geometry("%dx%d+%d+%d"%(w1//8, h1//8, decal[0], decal[1]))
			test.update_idletasks()
			test.state('zoomed')
			test.withdraw()
			if test.winfo_x() != posw1 or test.winfo_y() != posh1:
				newW = test.winfo_width()
				newH = test.winfo_height()
				newPosW = test.winfo_x()
				newPosH = test.winfo_y()
				self._add(Screen(newW, newH, newPosW, newPosH))
			test.state('normal')
			test.withdraw()
		test.destroy()
		return True

	def _add(self, screen, usableScreen=None, ratio=1):
		if usableScreen:
			self._screens.append((screen, usableScreen))
		else:
			self._screens.append((screen, \
				Screen(screen.w*ratio, screen.h*ratio, \
					screen.pw, screen.ph)))

	def _getMacOsScreens(self):
		if not self._getWindowServerScreens():
			if not self._getSystemProfilerScreens():
				self._getByTopLevelScreens()

	def _getWindowServerScreens(self):
		read = commandLine.MyCommand('defaults read')
		try:
			read.checkCommand()
		except exception.CommandLineError:
			return False
		code, out, err = xrandr.run(['/Library/Preferences/com.apple.windowserver.plist'])
		print out
		if code != 0:
			warnings.warn("Erreur de detection des ecrans\nError %s\n%s"%(str(code), err))
			return False
		return False

	def _getSystemProfilerScreens(self):
		systemProfiler = commandLine.MyCommand('system_profiler')
		try:
			systemProfiler.checkCommand()
		except exception.CommandLineError:
			return False
		keyWord = 'Resolution:'
		code, out, err = xrandr.run(['SPDisplaysDataType', '|', 'grep', keyWord])
		if code != 0:
			warnings.warn("Erreur de detection des ecrans\nError %s\n%s"%(str(code), err))
			return False
		widthOffset = 0
		heightOffset = 0
		for line in out.split('\n'):
			if len(self._screens) == 0:
				ratio = 0.9
			else:
				ratio = 1
			deb = line.find(keyWord) + len(keyWord)
			end = line.find('+', deb)
			width = line[deb:end].strip(' ')
			height = line[end+1:].strip(' ')
			self._add(Screen(w=width, h=height, pw=widthOffset, ph=heightOffset), ratio=ratio)
			widthOffset = width
		return False

	def _getByTopLevelScreens(self):
		print 'aa'
		test = tk.Toplevel()
		test.wm_attributes('-alpha', 0)
		test.withdraw()
		test.update_idletasks()

		posw1 = test.winfo_x()
		posh1 = test.winfo_y()
		scrW = test.winfo_screenwidth()
		scrH = test.winfo_screenheight()
		test.destroy()
		if scrW > 31*scrH//9:
			scrW = scrW//2
		elif scrW < 5*scrH//4:
			scrH = scrH//2
		self._add(Screen(scrW, scrH), ratio=0.9)
		return True

	def _getLinuxScreens(self):
		xrandr = commandLine.MyCommand('xrandr')
		try:
			xrandr.checkCommand()
		except exception.CommandLineError:
			self._getByTopLevelScreens()
		else:
			code, out, err = xrandr.run(['|', 'grep \*', '|', "cut -d' ' -f4"])
			if code != 0:
				warnings.warn("Erreur de detection des ecrans\nError %s\n%s"%(str(code), err))
				return False
			liste_res = out.strip('\n').splitlines()
			if '' in liste_res:
				liste_res.remove('')
			if not liste_res:
				liste_res = []
				code, out, err = xrandr.run(['|', 'grep connected'])
				if code != 0:
					warnings.warn("Erreur de detection des ecrans\nError %s\n%s"%(str(code), err))
					return False
				line_res = out.replace('\n', '')
				deb = line_res.find('connected')
				fin = line_res.find('+', deb+1)
				deb = line_res.rfind(' ', 0, fin)
				liste_res.append(line_res[deb+1: fin])

			code, out, err = xrandr.run()
			if code != 0:
				warnings.warn("Erreur de detection des ecrans: Error %s"%str(code) + "\n" + err)
				return False
			deb = 0
			liste_respos = []
			for res in liste_res:
				deb = out.find(res + '+', deb)
				fin = out.find(' ', deb)
				if len(self._screens) == 0:
					ratio = 0.9
				else:
					ratio = 1
				self._add(Screen(full=out[deb:fin]), ratio=ratio)
				deb = fin + 1
		return True

def get_size(fen_w, fen_h, screen, ratio):
	new_fen_w = min(fen_w, screen.w*(ratio-1)//ratio)
	new_fen_h = min(fen_h, screen.h)
	new_posw = screen.w//ratio-fen_w//ratio
	return ''.join( [str(new_fen_w), 'x', str(new_fen_h) ] )

def get_new_size(image, width, height):
	im_w, im_h = image.size
	aspect_ratio = im_w/im_h
	new_im_w = min(width, height*aspect_ratio)
	new_im_h = new_im_w//aspect_ratio
	return int(new_im_w), int(new_im_h)

def choose_orient(screen, ratio, decal_w, decal_h):
	use_w = screen.w-decal_w
	use_h = screen.h-decal_h
	use_ratio = use_w/use_h
	if use_ratio < ratio:
		return tk.TOP
	else:
		return tk.LEFT

def getRatio(ratio, default=None):
	try:
		a, b = ratio.split('/')
		value = round(int(a)/int(b), 3)
	except (ValueError, AttributeError):
		if default:
			value = default
		else:
			value = 16/9
	return value
