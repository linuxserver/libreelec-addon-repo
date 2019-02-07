
import subprocess
import xbmc
import xbmcaddon
import os.path


class Monitor(xbmc.Monitor):

   def __init__(self, *args, **kwargs):
      xbmc.Monitor.__init__(self)
      self.id = xbmcaddon.Addon().getAddonInfo('id')
      V_configfolder = xbmcaddon.Addon().getSetting('V_config')
      if not os.path.isfile('%s/custom.cnf' % (V_configfolder)):
         xbmcaddon.Addon().openSettings('id')

   def onSettingsChanged(self):
      subprocess.call(['systemctl', 'restart', self.id])

if __name__ == '__main__':
   Monitor().waitForAbort()
