#!/usr/bin/python
from xml.dom.minidom import parse
import xml.dom.minidom
import sys, os

script_dir = os.path.dirname(__file__)
resources_dir = os.path.join(script_dir, 'resources/')

# Open XML document using minidom parser
DOMTree = xml.dom.minidom.parse(resources_dir+"config.xml")

def getMenuGroups():
    settings = DOMTree.documentElement
    menu = settings.getElementsByTagName("menu")
    return settings.getElementsByTagName("menuGroup")

# Menu Group Elements
def getMG_elements(lvl, name):
    menu_groups = getMenuGroups()
    for mg in menu_groups:
        if (mg.getAttribute("lvl") == lvl) & (mg.getAttribute("name") == name):
            return mg.getElementsByTagName("menuElement")

def getLvlStyle(lvl, name):
    menu_groups = getMenuGroups()
    for mg in menu_groups:
        if (mg.getAttribute("lvl") == lvl) & (mg.getAttribute("name") == name):
            return mg.getAttribute('style')

# Menu Element by Tag Name
def getME_byTagName(menuElement, tagName):
    if len(menuElement.getElementsByTagName(tagName))>0:
        if len(menuElement.getElementsByTagName(tagName)[0].childNodes)>0:
            return menuElement.getElementsByTagName(tagName)[0].childNodes[0].data
    return ""

# Menu Element Id Number
def getId(menuElement):
    return menuElement.getAttribute("id")

def getName(menuElement):
    return getME_byTagName(menuElement, 'name')

def getIcon(menuElement):
    return getME_byTagName(menuElement, 'icon')

def getIconStyle(menuElement):
    if len(menuElement.getElementsByTagName('icon'))>0:
        return menuElement.getElementsByTagName('icon')[0].getAttribute('style')
    return ""

def getDescription(menuElement):
    return getME_byTagName(menuElement, 'description')

def getCmd(menuElement):
    if len(menuElement.getElementsByTagName(tagName))>0:
        if len(menuElement.getElementsByTagName(tagName)[0].childNodes)>0:
            return menuElement.getElementsByTagName(tagName)[0].childNodes[0]
    return Null


#print("menuStyle:"+getLvlStyle("0", ""))
#for me in getMG_elements("0", ""):
#    print("ID: %s" % getId(me))
#    print("NOME: %s" % getName(me))
#    print("ICON: %s" % getIcon(me)+"("+getIconStyle(me)+")")
#    print("DESCR: %s" % getDescription(me))
