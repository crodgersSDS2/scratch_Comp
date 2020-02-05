from sds2.componentmetamorphoses import ComponentMetamorphoses
from metamorphoses import Version, Attr
import param
import copy
import job


class_arg = {
'material': None,
'point1': None,
'type': 'Standard round',
'matchable':True,
'materialface': 'Web NS',
'shouldbevalid': True,
'referenceoffsetx': 0,
'referenceoffsety': 0,
'spacingx': 3,
'spacingy' : 3,
'grouprotation' :0,
'locate' : 'Center',
'columns' : 2,
'rows': 2,
'bolttype': 'AUTO',
'plugtype': 'No Plug',
'boltdiameter': .75,
'diameter': None,
'bothsides': True,
'showwindow': True
}

class mainVersions(ComponentMetamorphoses):
  versions = {}
  versions[0] = Version(
    Attr('x', class_arg['boltdiameter']),
    Attr('y', class_arg['diameter']),
    Attr('z',class_arg['type']),
    )
def LatestVersionNumber():
    return len(Versions) -1

def LatestVersion():
    return Versions[-1]

def SetupVersion():
    return job.GetRefreshedJobPluginOption(None,None)

def CurrentVersionDict(*args, **kwargs):
  jObj = job.GetRefreshedJobPluginOption(None, None)
  d = copy.deepcopy(LatestVersion())
  for k, v in LatestVersion().iteritems():
        d[k] = getattr(jObj, k) if hasattr(jObj, k) else v
  d.update(args, **kwargs)
  
  return d

def global_vars():
  d = {
  'hole_type_options': ['Standard round','Option 2', 'Option 3'],
  'yes_and_no': ['Yes','No'],
  'material_face_options': ['Web NS','Option 2', 'Option 3'],
  'locate_options': ['left', 'right', 'center'],
  'bolt_type_options': ['AUTO','Option 2', 'Option 3'],
  'bolt_diameter_options': [.75,.50, .25],
  'plug_type_options': ['No plug','Option 2', 'Option 3']
  }
  return d
