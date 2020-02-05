import copy
import math

from Designable.Proxies import Hole
from Layout3D import Layout3D
from mtrl_list import MtrlLocate
from Transform3D import Transform3D
from job import Job
from sds2 import obj
def design_material(self):
	atts = {
	'pt1' : self.Point1,#base_pt
	'BoltDiameter' : 0.75,#self.bolt_dia
	'BoltType' : 'AUTO',#self.bolt_grade
	'HoleType' : 'Standard round',#self.hole_type
	'Columns' : 2,#self.bolt_rows
	'Rows' : 2,#self.bolt_cols
	'Locate' : 'Above Right',
	'SpacingX' : 3,#self.bolt_rspc
	'SpacingY' : 3,#self.bolt_rspc
	'SlotRotation' : 90,
	'Matchable' : 'Yes',
	'ShowWindow' : 'Yes',
	#'typ_cnx' : 'Plate'
	'face' : 'Web NS',
	}

	proxy = Hole(**atts)
	proxy.SlotLength = proxy.calc_slot_length()
	proxy.Diameter = proxy.calc_hole_size()
	proxy.BothSides = 'Yes'
	proxy.Material = MtrlLocate('Locate material')

	return proxy

