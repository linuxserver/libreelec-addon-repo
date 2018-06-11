
import subprocess
import xbmc
import xbmcaddon


class Monitor(xbmc.Monitor):

   def __init__(self, *args, **kwargs):
      xbmc.Monitor.__init__(self)
      self.id = xbmcaddon.Addon().getAddonInfo('id')

   def onSettingsChanged(self):
      subprocess.call(['systemctl', 'restart', self.id])

E_password = xbmcaddon.Addon().getSetting('E_pass')
if E_password == "":
   xbmcaddon.Addon().openSettings('id')

if __name__ == '__main__':
   Monitor().waitForAbort()
