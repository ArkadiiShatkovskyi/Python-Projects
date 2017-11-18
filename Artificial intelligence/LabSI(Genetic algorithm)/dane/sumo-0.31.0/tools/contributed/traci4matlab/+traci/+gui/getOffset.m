function offset = getOffset(viewID)
%getOffset Get the offset of the view.
%   offset = getOffset(VIEWID) Returns the x and y offset of the center of 
%   the current view. If no view ID is given, the function return the 
%   results for the default view.

%   Copyright 2016 Universidad Nacional de Colombia,
%   Politecnico Jaime Isaza Cadavid.
%   Authors: Andres Acosta, Jairo Espinosa, Jorge Espinosa.
%   $Id: getOffset.m 31 2016-09-28 15:16:56Z afacostag $

import traci.constants
if nargin < 1
    viewID = 'View #0';
end
offset = traci.gui.getUniversal(constants.VAR_VIEW_OFFSET, viewID);