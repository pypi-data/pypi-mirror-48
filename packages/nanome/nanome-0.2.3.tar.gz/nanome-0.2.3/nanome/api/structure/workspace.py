from nanome._internal._structure._workspace import _Workspace
from nanome.util import Logs

class Workspace(_Workspace):
    def __init__(self):
        _Workspace.__init__(self)
        self._transform = Workspace.Transform(self)

    @property
    def complexes(self):
        return self._complexes
    @complexes.setter
    def complexes(self, value):
        self._complexes = value

    #region fields
    @property
    def position(self):
        return self._position
    @position.setter
    def position(self, value):
        self._position = value

    @property
    def rotation(self):
        return self._rotation
    @rotation.setter
    def rotation(self, value):
        self._rotation = value

    @property
    def scale(self):
        return self._scale
    @scale.setter
    def scale(self, value):
        self._scale = value
    #endregion

    #region deprecated
    @property
    @Logs.deprecated()
    def transform(self):
        return self._transform

    class Transform(object):
        def __init__(self, parent):
            self.parent = parent

        @property
        def position(self):
            return self.parent.position
        @position.setter
        def position(self, value):
            self.parent.position = value

        @property
        def rotation(self):
            return self.parent.rotation
        @rotation.setter
        def rotation(self, value):
            self.parent.rotation = value

        @property
        def scale(self):
            return self.parent.scale
        @scale.setter
        def scale(self, value):
            self.parent.scale = value
    #endregion
_Workspace._create = Workspace
