import xbmc, xbmcaddon, xbmcgui, xbmcplugin,os
import shutil
import subprocess
import glob
import urllib2,urllib
import re
import resources.lib.utils as utils
import extract
import downloader
import time
import os
import errno

def main(name,url,description):
    path = xbmc.translatePath(os.path.join('special://home/addons','packages'))
    dp = xbmcgui.DialogProgress()
    dp.create("Iain's Update Tool","Downloading update ",'', 'Please Wait')
    lib=os.path.join(path, name+'.zip')
    try:
       os.remove(lib)
    except:
       pass
    downloader.download(url, lib, dp)
    addonfolder = xbmc.translatePath(os.path.join('special://','home'))
    time.sleep(2)
    dp.update(0,"Extracting archive")
    print '======================================='
    print addonfolder
    print '======================================='
    extract.all(lib,addonfolder,dp)


if __name__ == "__main__":
    main()
