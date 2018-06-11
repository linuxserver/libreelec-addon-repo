import xbmc
import xbmcgui
from subprocess import call

call(["docker", "image", "prune", "-a", "-f"])
xbmcgui.Dialog().notification('Docker Image Updater', 'All unused docker images removed!', xbmcgui.NOTIFICATION_INFO, 5000)
