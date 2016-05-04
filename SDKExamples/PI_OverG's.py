from XPLMDefs import *
from XPLMDisplay import *
from XPLMGraphics import *
from XPLMDataAccess import *
from XPLMUtilities import*
from XPLMPlugin import *
class PythonInterface:

	def XPluginStart(self):
		self.Name = "Death by over G's"
		self.Sig = "RyleyHindman.python.Death by over G's"
		self.Desc = "A pythonScript"
		
		self.DrawWindowCB = self.DrawWindowCallback
		self.KeyCB = self.KeyCallback
		self.MouseClickCB = self.MouseClickCallback
		self.WindowID = XPLMCreateWindow(self, 50, 600, 300, 400, 1, self.DrawWindowCB, self.KeyCB, self.MouseClickCB, 0)
		
		self.GLoad = XPLMFindDataRef("sim/flightmodel/forces/g_nrml") 
				
		#XPLMRegisterFlightLoopCallback(self, self.FlightLoopCB, 1.0, 0)
		
		return self.Name, self.Sig, self.Desc
			
	def getDataref(self, datarefString):
		if (self.datarefs.get(datarefString) == None):
			self.datarefs[datarefString] = XPLMFindDataRef(datarefString)
		return self.datarefs.get(datarefString)
		
	
	def XPluginStop(self):
		XPLMDestroyWindow(self, self.WindowId)
		pass
	def XPluginEnable(self):
		return 1
		
	def XPluginDisable(self):
		pass
	
	def XPluginReceiveMessage(self, inFromWho, inMessage, inParam):
		pass
		
	"""def FlightLoopCallback(self, elapsedMe, elapsedSim, counter, refcon):
		pass"""
	
	def DrawWindowCallback(self, inWindowID, inRefcon):
		lLeft = []; lTop = []; lRight = []; lBottom = []
		XPLMGetWindowGeometry(inWindowID, lLeft, lTop, lRight, lBottom)
		left = int(lLeft[0]); top = int(lTop[0]); right = int(lRight[0]); bottom = int(lBottom[0])
		
		gResult = XPLMDrawTranslucentDarkBox(left, top, right, bottom)
		color = 1.0, 1.0, 1.0
		
		G-Load = XPLMGetDataf(self.Gload)
		if(G-Load >= 5):
			Desc = "Your passengers have blacked out"
		if(-4 < G-Load < 5):
			Desc = "You are surviving"
		if(-4 >= G-Load):
			Desc = "Your passengers have blacked out"
			
		gResult = XPLMDrawString(color, left + 5, top - 20, Desc, 0, xplmFont_Basic)
		
		pass
			
		
	def KeyCallback(self, inWindowID, inKey, inFlags, inVirtualKey, inRefcon, losingFocus):
		pass
	
	def MouseClickCallback(self, inWindowID, x, y, inMouse, inRefcon):
		pass	