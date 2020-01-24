from Component import *
from PluginSetupTools import RegisterPluginSetup
from component_tools import RegisterComponentAddCommand
#import Commands
#import os.path

from main import Main_Comp
#mage1 = os.path.join( os.path.dirname( __file__ ), "images/default.png" )


#this adds it to the list of "select component type"
RegisterComponentType(Main_Comp, "Main Label ")
#RegisterPluginSetup(comp, None)

#con32 = Commands.Icon(image1)
#icon64 = Commands.Icon(image1)

RegisterComponentAddCommand(Main_Comp)#icons=Commands.IconSet((icon32, icon64))