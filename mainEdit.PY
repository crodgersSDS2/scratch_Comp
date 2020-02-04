
#SDS libraries
from sds2.utility.gadget_protocol import SubdialogController as gp
import mainVersions
import sys
#dialog libraries
from dialog.label import Label
from dialog.combobox import Combobox
from dialog.entry import Entry
from dialog.checkbox import Checkbox
import model

def WindowPositionID():
    return 'd18cac09-5d00-45a9-aba8-cb369178f8ab'

def general_leaf(frame):
	Combobox(frame, 'boltdiameter', mainVersions.global_vars()['bolt_diameter_options'], 'Bolt diameter:')
	Entry(frame,'diameter','Hole diameter:')
	Combobox(frame,'type',mainVersions.global_vars()['hole_type_options'],'Hole type:')
	Checkbox(frame, 'matchable', 'Matchable:')
	Combobox(frame,'bolttype', mainVersions.global_vars()['bolt_type_options'], 'Preferred bolt type:')
	Checkbox(frame,'shouldbevalid', 'Valid for CNC downloading:')



def EditInGadget(model, title):
	controller = CE.StandaloneComponentEditController(CE.StandaloneComponentEditView(WindowPositionID(),title), StandaloneComponentEditUI(model, title))
	controller.CreateUI()
	controller.Run()


def build_ui(model, gadget_factory, mn = 'Beam'):
	controller = gp(model)
	gadget_factory.LoadSaveBanner(
		controller,
		general_leaf,
		'General Settings',
		'',
		'bannerid',
		'bannerform',
		[]
		)