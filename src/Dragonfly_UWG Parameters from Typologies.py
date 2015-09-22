# Urban Weather Generator Parameters from Building Typologies
#
# Dragonfly: A Plugin for Climate Data Generation (GPL) started by Chris Mackey
# 
# This file is part of Dragonfly.
# 
# Copyright (c) 2015, Chris Mackey <Chris@MackeyArchitecture.com> 
# Dragonfly is free software; you can redistribute it and/or modify 
# it under the terms of the GNU General Public License as published 
# by the Free Software Foundation; either version 3 of the License, 
# or (at your option) any later version. 
# 
# Dragonfly is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of 
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the 
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with Dragonfly; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>


"""
Use this component to generate paremeters for an Urban Weather Generator model using urban typologies and the ratios of each typology within the urban area.  These building typologies can generated with either the "Dragonfly_Building Typology from HBZone" or the "Dragonfly_Building Typology from Parameters" component.
_
The ouput of this component can be plugged into the 'Dragonfly_Run Urban Weather Generator' component in order to morph a rural/airport weather file to reflect the urban conditions input to this component.
-
Provided by Dragonfly 0.0.01
    Args:
        _buildingTypologies: One or more building typologies from either the "Dragonfly_Building Typology from HBZone" or the "Dragonfly_Building Typology from Parameters" component.
        typologyRatios_: A list of numbers that sum to 1 and represent the fraction of the buildings in the urban area occupied by each of the connected typologies now.  Note that the length of this list must match the number of typologies connected to the input above and that the order of this list should align with the order that you have connected typologies to the input above.  If no values are input here, it will be assumed that each of the typologies occupies an equal amount of the built space in the urban area.
        _buildingBreps: A list of closed solids that represent the buildings of the urban area for which UWGParamters are being created.  Note that each solid should represent one building and buildings should NOT be broken up floor-by-floor as they are for zones in the "Dragonfly_UWG Parameters from HBZones" component.
        _treeBrepsOrCoverage: Either a list of breps that represent the trees of the urban area that is being modeled or a number between 0 and 1 that represents that fraction of tree coverage in the urban area.  If breps are input, they will be projected to the ground plane to compute the area of tree coverage as seen from above.
        _pavementBrep: A list of breps that represent the paved portion of the urban area.  Note that this input brep should just reflect the surface of the terrain and should not be a solid.  Also note that this surface should be coninuous beneath the ground of the HBZones and should only be interrupted in grassy areas where the user intends to connect up such grassy surfaces to the "grassBrep_" input below.  The limits of this surface will be used to determine the density of the urban area so including a surface that extends well beyond the area where the HBZones are will cause the simulation to inacurately model the density.
        grassBrep_: Either a list of breps that represent the grass surfaces of the urban area or a number between 0 and 1 that represents that fraction of the _pavementBrep that is covered in grass.
        --------------------: ...
        vegetationPar_: An optional list of Vegetation Parameters from the "Dragonfly_Vegetation Parameters" component.  If no vegetation parameters are input here, the UWG will attempt to determine the months in which vegetation is active by looking at the average monthly temperatures in the EPW file.
        pavementPar_: Optional Pavement Parameters from the "Dragonfly_Pavement Parameters" component.
        nonBldgAnthroHeat_: An number that represents the anthropogenic heat generated in the urban canyon in Watts per square meter of pavement (W/m2).  This is specifcally the heat that DOES NOT originate from buildings and mostly includes heat originating from automobiles, street lighting, and human metabolism.  Typical values are 10 W/m2 for a commercial area in Singapore, 4 W/m2 for a residential area in Singapore, 8 W/m2 for a typical part of Toulouse, France. Values are available for some cities by Sailor: http://onlinelibrary.wiley.com/doi/10.1002/joc.2106/abstract
    Returns:
        UWGParameters: A list of parameters that can be plugged into the "Dragonfly_Run Urban Weather Generator" component.
"""

ghenv.Component.Name = "Dragonfly_UWG Parameters from Typologies"
ghenv.Component.NickName = 'UWGParFromTypology'
ghenv.Component.Message = 'VER 0.0.01\nSEP_21_2015'
ghenv.Component.Category = "Dragonfly"
ghenv.Component.SubCategory = "2 | GenerateUrbanClimate"
#compatibleLBVersion = VER 0.0.59\nFEB_01_2015
try: ghenv.Component.AdditionalHelpFromDocStrings = "2"
except: pass
