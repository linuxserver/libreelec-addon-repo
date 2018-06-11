import xbmc
import xbmcgui
from subprocess import call

call(["docker", "container", "prune", "-f"])
xbmcgui.Dialog().notification('Docker Image Updater', 'All stopped containers removed!', xbmcgui.NOTIFICATION_INFO, 5000)
