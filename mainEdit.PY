
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
	Combobox(frame, 'x', mainVersions.global_vars()['bolt_diameter_options'], 'Bolt diameter:')
	#Entry(frame,'diameter','Hole diameter:')
	Combobox(frame,'y',mainVersions.global_vars()['hole_type_options'],'Hole type:')
	Checkbox(frame, 'z', 'Matchable:')



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