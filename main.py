#CUSTOM LIBRARIES
import mainEdit as Edit
from mainVersions import mainVersions
import sys
#SDS LIBRARIES
from Designable.ProcessableComponent import ProcessableComponent as DPC
from sds2.utility.gadget_protocol import GadgetComponent as GC
#from kwargmixin.kwargmixin import KWArgMixin as KM
from Point3D import Point3D as P3D
import model
#mem1.Type (mem1.type) returns "Beam" or "Column" or "Vertical Brace" or "Horizontal Brc" or "Joist" or "Girt" or "Purlin" or "Misc" or "Stair" or "Custom" (read-only)
member_Types = ['joist','beam','column','verticle brace','horizontal brace','girt','purlin','misc','stair','custom']
mem = ['somethin']
@mainVersions
class Main_Comp(GC, DPC):
    def _init_(self, **kwargs):
        DPC._init_(self, **kwargs)
        mainVersions.init_factory()(self, **kwargs)
        #componentedit.MemberEditMethods._init_(self, **kwargs)
        #KM._init_(self, **kwargs)
    def IsAllowedOnMember(self, mn):
        #membertype = model.member(mn).custom_member_type.lower()
        #mem.append(membertype)
        sys.stdout.write(mn)
        sys.stdout.write(model.member(mn).custom_member_type.lower())
        mem[0] = model.member(mn).custom_member_type.lower()
        sys.stdout.write(' '+mem[0]+' ')
        return True
    @classmethod
    def Factory(cls, host, member_universe):
        mainClass = cls()
        mainClass.x = 4
        return mainClass
    def SetReferencePointForMemberUI(self, mn):
        self.ref_point = Point3D(0.,0.,0.)
    def Add(self, mn):
        return True
    @staticmethod #without this you need a third param
    def CreateCustomMultiEditableUI(model, gadget_factory):
        Edit.build_ui(model, gadget_factory, mem[0])
    def DesignForMember(self, mn):
        return True