#CUSTOM LIBRARIES
import mainEdit as Edit
from mainVersions import mainVersions
from designMainMaterial import design_material
#SDS LIBRARIES
import sys
import Designable.Proxies
from Component import PrepareComponentForMember 
from Designable.ProcessableComponent import ProcessableComponent as DPC
from MemberBase import GetMemberLink
from sds2.utility.gadget_protocol import GadgetComponent as GC
#from kwargmixin.kwargmixin import KWArgMixin as KM
from Point3D import Point3D as P3D
import model
#mem1.Type (mem1.type) returns "Beam" or "Column" or "Vertical Brace" or "Horizontal Brc" or "Joist" or "Girt" or "Purlin" or "Misc" or "Stair" or "Custom" (read-only)
member_Types = ['joist','beam','column','verticle brace','horizontal brace','girt','purlin','misc','stair','custom']
@mainVersions
class Main_Comp(GC, DPC):
    titleStr = 'A Main Component'
    Materials = design_material
    def _init_(self, **kwargs):
        DPC._init_(self, **kwargs)
        mainVersions.init_factory()(self, **kwargs)
        #componentedit.MemberEditMethods._init_(self, **kwargs)
        KM._init_(self, **kwargs)
    @property
    def HostXform(self):
        var = GetMemberLink(self.member_number, False, False).GetXform()
        return var
    @property
    def Width(self):
        return self.HostDepth - (2 * self.HostFlangeThick)
    @property
    def HostFlangeThick(self):
        return Shape(
            model.member(self.member_number).section_size
        ).FlangeThickness
    @property
    def Point1(self):
        var = (
            self.GetReferencePoint() +
            -self.HostXform.GetBasisVectorY()
        )
        return var

    def IsAllowedOnMember(self, mn):
        return model.member(mn).member_type == model.Beam
    @classmethod
    def Factory(cls, host, member_universe):
        mainClass = cls()
        PrepareComponentForMember(mainClass, host)
        mainClass.SetReferencePoint(ref_point)
        return mainClass
    def SetReferencePointForMemberUI(self, mn):
        self.ref_point = P3D(0.25,0.25,0.25)#x,y,z
        return self.ref_point #x,y,z

    def Add(self, mn):
        PrepareComponentForMember(self, mn)
        return self.SetReferencePointForMemberUI(mn)
    @staticmethod #without this you need a third param
    def CreateCustomMultiEditableUI(model, gadget_factory):
        Edit.build_ui(model, gadget_factory)
    def DesignForMember(self, mn):
        self.RegisterDesignProxy(self.Materials())
        return True