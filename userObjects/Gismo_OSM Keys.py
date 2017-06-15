# OSM keys
#
# Gismo is a plugin for GIS environmental analysis (GPL) started by Djordje Spasic.
#
# This file is part of Gismo.
#
# Copyright (c) 2017, Djordje Spasic <djordjedspasic@gmail.com>
# Component icon based on free OSM icon from: <https://icons8.com/web-app/13398/osm>
#
# Gismo is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
#
# Gismo is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with this program. If not, see http://www.gnu.org/licenses/.
#
# The GPL-3.0+ license <http://spdx.org/licenses/GPL-3.0+>

"""
Use this component to generate a list of keys for the "requiredKeys_" input of "OSM shapes" component.
A list of keys depends on the chosen OSM object name (_OSMobjectName). Use "OSM Objects" dropdown list to generate the appropriate _OSMobjectName.
-
Provided by Gismo 0.0.2
    
    input:
        _OSMobjectName: OSM object name.
                        Use "OSM Objects" dropdown list to generate it.
    
    output:
        readMe!: ...
        requiredKeys: A list of keys for the chosen OSM object name (_OSMobjectName).
                      Supply it to the "requiredKeys_" input of "OSM shapes" component.
        OSMwebpage: Webpage containing detailed information about the chosen _OSMobjectName.
"""

ghenv.Component.Name = "Gismo_OSM Keys"
ghenv.Component.NickName = "OSMKeys"
ghenv.Component.Message = "VER 0.0.2\nJUN_15_2017"
ghenv.Component.IconDisplayMode = ghenv.Component.IconDisplayMode.application
ghenv.Component.Category = "Gismo"
ghenv.Component.SubCategory = "1 | OpenStreetMap"
#compatibleGismoVersion = VER 0.0.2\nJUN_15_2017
try: ghenv.Component.AdditionalHelpFromDocStrings = "2"
except: pass

import scriptcontext as sc
import Grasshopper
import System
import Rhino
import math


def main(OSMobjectName):
    
    # check _OSMobjectName
    if (len(OSMobjectName) == 0):
        requiredKeys_unique = []
        OSMwebpage = None
        validInputData = False
        printMsg = "Supply a name or names to \"_OSMobjectName\" input by using \"OSM Objects\" dropdown list."
        return requiredKeys_unique, OSMwebpage, validInputData, printMsg
    
    
    requiredKeys_dictionary = {
    """Commercial building""" :
    ["name",
    "name:en",
    "landuse",
    "office",
    "shop",
    "building",
    "addr:country",
    "addr:city",
    "addr:postcode",
    "addr:street",
    "addr:housenumber",
    "http://wiki.openstreetmap.org/wiki/Tag:building%3Dcommercial"]
    ,
    """Residential building""" :
    ["name",
    "name:en",
    "building",
    "addr:country",
    "addr:city",
    "addr:postcode",
    "addr:street",
    "addr:housenumber",
    "building:levels",
    "building:flats",
    "building:roof",
    "building:colour",
    "building:ruian:type",
    "roof:shape",
    "roof:colour",
    "roof:material",
    "ref:ruian:building",
    "source",
    "http://wiki.openstreetmap.org/wiki/Tag:building%3Dresidential"]
    ,
    """Office building""" :
    ["name",
    "name:en",
    "landuse",
    "office",
    "building",
    "addr:country",
    "addr:city",
    "addr:postcode",
    "addr:street",
    "addr:housenumber",
    "http://wiki.openstreetmap.org/wiki/Tag:building%3Doffice"]
    ,
    """Office administrative""" :
    ["name",
    "name:en",
    "office",
    "addr:country",
    "addr:city",
    "addr:postcode",
    "addr:street",
    "addr:housenumber",
    "phone",
    "opening_hours",
    "wheelchair",
    "operator",
    "http://wiki.openstreetmap.org/wiki/Tag:office%3Dadministrative"]
    ,
    """Office government""" :
    ["name",
    "name:en",
    "amenity",
    "office",
    "government",
    "admin_level",
    "addr:country",
    "addr:city",
    "addr:postcode",
    "addr:street",
    "addr:housenumber",
    "phone",
    "opening_hours",
    "wheelchair",
    "http://wiki.openstreetmap.org/wiki/Tag:office%3Dgovernment"]
    ,
    """Post office""" :
    ["name",
    "name:en",
    "amenity",
    "addr:country",
    "addr:city",
    "addr:postcode",
    "addr:street",
    "addr:housenumber",
    "contact",
    "phone",
    "website",
    "opening_hours",
    "wheelchair",
    "ref",
    "ref:FR:LaPoste",
    "atm",
    "change_machine",
    "operator",
    "http://wiki.openstreetmap.org/wiki/Tag:amenity%3Dpost_office"]
    ,
    """Hospital""" :
    ["name",
    "name:en",
    "amenity",
    "beds",
    "emergency",
    "addr:country",
    "addr:city",
    "addr:postcode",
    "addr:street",
    "addr:housenumber",
    "phone",
    "height",
    "building:levels",
    "min_height",
    "building",
    "entrance",
    "roof:shape",
    "start_date",
    "source",
    "http://wiki.openstreetmap.org/wiki/Tag:amenity%3Dhospital"]
    ,
    """Ambulance station""" :
    ["name",
    "name:en",
    "amenity",
    "beds",
    "emergency",
    "addr:country",
    "addr:city",
    "addr:postcode",
    "addr:street",
    "addr:housenumber",
    "phone",
    "height",
    "building:levels",
    "min_height",
    "building",
    "entrance",
    "source",
    "http://wiki.openstreetmap.org/wiki/Tag:emergency%3Dambulance_station"]
    ,
    """Pharmacy""" :
    ["name",
    "name:en",
    "amenity",
    "addr:country",
    "addr:city",
    "addr:postcode",
    "addr:street",
    "addr:housenumber",
    "phone",
    "website",
    "contact",
    "building",
    "brand",
    "opening_hours",
    "drive_through",
    "wheelchair",
    "dispensing",
    "shop",
    "vending",
    "operator",
    "source",
    "http://wiki.openstreetmap.org/wiki/Tag:amenity%3Dpharmacy"]
    ,
    """Police""" :
    ["name",
    "name:en",
    "amenity",
    "addr:country",
    "addr:city",
    "addr:postcode",
    "addr:street",
    "addr:housenumber",
    "contact",
    "phone",
    "website",
    "opening_hours",
    "wheelchair",
    "http://wiki.openstreetmap.org/wiki/Tag:amenity%3Dpolice"]
    ,
    """Fire station""" :
    ["name",
    "name:en",
    "amenity",
    "addr:country",
    "addr:city",
    "addr:postcode",
    "addr:street",
    "addr:housenumber",
    "contact",
    "phone",
    "operator",
    "http://wiki.openstreetmap.org/wiki/Tag:amenity%3Dfire_station"]
    ,
    """Museum""" :
    ["name",
    "name:en",
    "amenity",
    "tourism",
    "addr:country",
    "addr:city",
    "addr:postcode",
    "addr:street",
    "addr:housenumber",
    "phone",
    "opening_hours",
    "website",
    "entrance",
    "wheelchair",
    "subject",
    "shop",
    "operator",
    "http://wiki.openstreetmap.org/wiki/Tag:tourism%3Dmuseum"]
    ,
    """Theatre""" :
    ["name",
    "name:en",
    "amenity",
    "theatre:genre",
    "addr:country",
    "addr:city",
    "addr:postcode",
    "addr:street",
    "addr:housenumber",
    "phone",
    "website",
    "entrance",
    "wheelchair",
    "operator",
    "http://wiki.openstreetmap.org/wiki/Tag:amenity%3Dtheatre"]
    ,
    """Library""" :
    ["name",
    "name:en",
    "amenity",
    "tourism",
    "ref:isil",
    "addr:country",
    "addr:city",
    "addr:postcode",
    "addr:street",
    "addr:housenumber",
    "opening_hours",
    "shop",
    "entrance",
    "wheelchair",
    "operator",
    "http://wiki.openstreetmap.org/wiki/Tag:amenity%3Dlibrary"]
    ,
    """Book store""" :
    ["name",
    "name:en",
    "amenity",
    "shop",
    "addr:country",
    "addr:city",
    "addr:postcode",
    "addr:street",
    "addr:housenumber",
    "phone",
    "website",
    "opening_hours",
    "wheelchair",
    "brand",
    "books",
    "second_hand",
    "operator",
    "http://wiki.openstreetmap.org/wiki/Tag:shop%3Dbooks"]
    ,
    """College""" :
    ["name",
    "name:en",
    "amenity",
    "addr:country",
    "addr:city",
    "addr:postcode",
    "addr:street",
    "addr:housenumber",
    "phone",
    "website",
    "opening_hours",
    "entrance",
    "wheelchair",
    "operator",
    "http://wiki.openstreetmap.org/wiki/Tag:amenity%3Dcollege"]
    ,
    """University""" :
    ["name",
    "name:en",
    "amenity",
    "addr:country",
    "addr:city",
    "addr:postcode",
    "addr:street",
    "addr:housenumber",
    "phone",
    "website",
    "faculty",
    "department",
    "opening_hours",
    "entrance",
    "wheelchair",
    "landuse",
    "residential",
    "highway",
    "operator",
    "wiki.openstreetmap.org/wiki/Tag:amenity=university"]
    ,
    """School""" :
    ["name",
    "name:en",
    "amenity",
    "addr:country",
    "addr:city",
    "addr:postcode",
    "addr:street",
    "addr:housenumber",
    "phone",
    "website",
    "capacity",
    "isced:level",
    "fee",
    "religion",
    "denomination",
    "ref",
    "contact",
    "leisure",
    "landuse",
    "min_age",
    "max_age",
    "sport",
    "surface",
    "barrier",
    "entrance",
    "wheelchair",
    "operator",
    "http://wiki.openstreetmap.org/wiki/Tag:amenity%3Dschool"]
    ,
    """Kindergarten""" :
    ["name",
    "name:en",
    "amenity",
    "addr:country",
    "addr:city",
    "addr:postcode",
    "addr:street",
    "addr:housenumber",
    "phone",
    "website",
    "capacity",
    "isced:level",
    "fee",
    "religion",
    "denomination",
    "ref",
    "contact",
    "leisure",
    "landuse",
    "min_age",
    "max_age",
    "sport",
    "surface",
    "barrier",
    "entrance",
    "wheelchair",
    "access",
    "operator",
    "http://wiki.openstreetmap.org/wiki/Tag:amenity%3Dkindergarten"]
    ,
    # ------------
    """Playground""" :
    ["name",
    "name:en",
    "amenity",
    "leisure",
    "tourism",
    "opening_hours",
    "wheelchair",
    "natural",
    "barrier",
    "surface",
    "baby",
    "walking_disability",
    "sitting_disability",
    "blind",
    "min_age",
    "max_age",
    "centralkey",
    "access",
    "fee",
    "supervised",
    "operator",
    "http://wiki.openstreetmap.org/wiki/Tag:leisure%3Dplayground"]
    ,
    """Sports center""" :
    ["name",
    "name:en",
    "amenity",
    "leisure",
    "landuse",
    "sport",
    "address",
    "building",  # this is not a mistake!
    "operator",
    "http://wiki.openstreetmap.org/wiki/Tag:leisure%3Dsports_centre"]
    ,
    """Stadium""" :
    ["name",
    "name:en",
    "amenity",
    "leisure",
    "capacity",
    "sport",
    "addr:country",
    "addr:city",
    "addr:postcode",
    "addr:street",
    "addr:housenumber",
    "building",  # this is not a mistake!
    "entrance",
    "start_date",
    "owner",
    "operator",
    "http://wiki.openstreetmap.org/wiki/Tag:leisure%3Dstadium"]
    ,
    """Park""" :
    ["name",
    "name:en",
    "amenity",
    "leisure",
    "landuse",
    "boundary",
    "highway",
    "http://wiki.openstreetmap.org/wiki/Tag:leisure%3Dpark"]
    ,
    """Garden""" :
    ["name",
    "leisure",
    "garden:type",
    "garden:style",
    "access",
    "http://wiki.openstreetmap.org/wiki/Tag:leisure%3Dgarden"]
    ,
    """Camping site""" :
    ["name",
    "name:en",
    "fee",
    "opening_hours",
    "phone",
    "website",
    "addr:country",
    "addr:city",
    "addr:postcode",
    "addr:street",
    "addr:housenumber",
    "tents",
    "caravans",
    "openfire",
    "backcountry",
    "scout",
    "group_only",
    "impromptu",
    "camp_site",
    "drinking_water",
    "sanitary_dump_station",
    "internet_access",
    "internet_access:fee",
    "http://wiki.openstreetmap.org/wiki/Tag:tourism%3Dcamp_site"]
    ,
    """Forest""" :
    ["name",
    "name:en",
    "natural",
    "leaf_type",
    "leaf_cycle",
    "crop",
    "http://wiki.openstreetmap.org/wiki/Tag:landuse%3Dforest"]
    ,
    """Grassland""" :
    ["name",
    "name:en",
    "natural",
    "grassland",
    "landuse",
    "managed",
    "surface",
    "operator",
    "http://wiki.openstreetmap.org/wiki/Tag:natural%3Dgrassland"]
    ,
    """Waterway""" :
    ["name",
    "name:en",
    "ref",
    "waterway",
    "natural",
    "water",
    "landuse",
    "leisure",
    "destination",
    "distance",
    "ford",
    "seasonal",
    "tidal",
    "intermittent",
    "lock",
    "http://wiki.openstreetmap.org/wiki/Key:waterway"]
    ,
    """Coastline""" :
    ["name",
    "name:en",
    "natural",
    "landuse",
    "waterway",
    "harbour",
    "leisure",
    "amenity",
    "mooring",
    "man_made",
    "place",
    "sport",
    "seamark:type",
    "boundary",
    "source",
    "http://wiki.openstreetmap.org/wiki/Tag:natural%3Dcoastline"]
    ,
    # ------------
    """Cafe""" :
    ["name",
    "name:en",
    "amenity",
    "addr:country",
    "addr:city",
    "addr:postcode",
    "addr:street",
    "addr:housenumber",
    "phone",
    "website",
    "opening_hours",
    "internet_access",
    "wheelchair",
    "smoking",
    "self_service",
    "takeaway",
    "outdoor_seating",
    "cuisine",
    "diet",
    "breakfast",
    "lunch",
    "ice_cream",
    "operator",
    "http://wiki.openstreetmap.org/wiki/Tag:amenity%3Dcafe"]
    ,
    """Bar""" :
    ["name",
    "name:en",
    "amenity",
    "addr:country",
    "addr:city",
    "addr:postcode",
    "addr:street",
    "addr:housenumber",
    "contact",
    "phone",
    "internet_access",
    "opening_hours",
    "cuisine",
    "drink",
    "brewery",
    "microbrewery",
    "smoking",
    "wheelchair",
    "food",
    "cocktails",
    "beer_garden",
    "leisure",
    "outdoor_seating",
    "real_ale",
    "real_cider",
    "accommodation",
    "camra",
    "real_fire",
    "operator",
    "http://wiki.openstreetmap.org/wiki/Tag:amenity%3Dbar"]
    ,
    """Pub""" :  #(the same as for bar)
    ["name",
    "name:en",
    "amenity",
    "addr:country",
    "addr:city",
    "addr:postcode",
    "addr:street",
    "addr:housenumber",
    "contact",
    "phone",
    "internet_access",
    "opening_hours",
    "cuisine",
    "drink",
    "brewery",
    "microbrewery",
    "smoking",
    "wheelchair",
    "food",
    "cocktails",
    "beer_garden",
    "leisure",
    "outdoor_seating",
    "real_ale",
    "real_cider",
    "accommodation",
    "camra",
    "real_fire",
    "operator",
    "http://wiki.openstreetmap.org/wiki/Tag:amenity%3Dpub"]
    ,
    """Winery""" :
    ["name",
    "name:en",
    "amenity",
    "shop",
    "landuse",
    "addr:country",
    "addr:city",
    "addr:postcode",
    "addr:street",
    "addr:housenumber",
    "opening_hours",
    "entrance",
    "wheelchair",
    "operator",
    "http://wiki.openstreetmap.org/wiki/Tag:craft%3Dwinery"]
    ,
    """Restaurant""" :
    ["name",
    "name:en",
    "amenity",
    "addr:country",
    "addr:city",
    "addr:postcode",
    "addr:street",
    "addr:housenumber",
    "contact",
    "phone",
    "internet_access",
    "opening_hours",
    "stars",
    "cuisine",
    "leisure",
    "outdoor_seating",
    "cocktails",
    "diet",
    "opening_hours",
    "brewery",
    "microbrewery",
    "smoking",
    "wheelchair",
    "takeaway",
    "delivery",
    "drive_through",
    "reservation",
    "operator",
    "http://wiki.openstreetmap.org/wiki/Tag:amenity%3Drestaurant"]
    ,
    """Supermarket""" :
    ["name",
    "name:en",
    "amenity",
    "shop",
    "addr:country",
    "addr:city",
    "addr:postcode",
    "addr:street",
    "addr:housenumber",
    "phone",
    "website",
    "opening_hours",
    "wheelchair",
    "organic",
    "membership",
    "bulk_purchase",
    "operator",
    "http://wiki.openstreetmap.org/wiki/Tag:shop%3Dsupermarket"]
    ,
    """Public market""" :
    ["name",
    "name:en",
    "amenity",
    "shop",
    "addr:country",
    "addr:city",
    "addr:postcode",
    "addr:street",
    "addr:housenumber",
    "phone",
    "website",
    "opening_hours",
    "wheelchair",
    "building",  # this is not a mistake!
    "highway",
    "organic",
    "operator",
    "http://wiki.openstreetmap.org/wiki/Tag:amenity%3Dmarketplace"]
    ,
    """Mall""" :
    ["name",
    "name:en",
    "amenity",
    "shop",
    "addr:country",
    "addr:city",
    "addr:postcode",
    "addr:street",
    "addr:housenumber",
    "phone",
    "website",
    "opening_hours",
    "wheelchair",
    "building",  # this is not a mistake!
    "landuse",
    "operator",
    "http://wiki.openstreetmap.org/wiki/Tag:shop%3Dmall"]
    ,
    """Hostel""" :
    ["name",
    "name:en",
    "tourism",
    "stars",
    "rooms",
    "beds",
    "wheelchair",
    "addr:country",
    "addr:city",
    "addr:postcode",
    "addr:street",
    "addr:housenumber",
    "phone",
    "internet_access",
    "internet_access:fee",
    "smoking",
    "lacounty:ain",
    "lacounty:bld_id",
    "height",
    "building:levels",
    "min_height",
    "building",
    "ruian:building",
    "building:ruian:type",
    "building:units",
    "entrance",
    "website",
    "start_date",
    "ele",
    "operator",
    "source",
    "http://wiki.openstreetmap.org/wiki/Tag:tourism%3Dhostel"]
    ,
    """Hotel""" :  # (the same as hotel)
    ["name",
    "name:en",
    "tourism",
    "stars",
    "rooms",
    "beds",
    "wheelchair",
    "addr:country",
    "addr:city",
    "addr:postcode",
    "addr:street",
    "addr:housenumber",
    "phone",
    "internet_access",
    "internet_access:fee",
    "smoking",
    "lacounty:ain",
    "lacounty:bld_id",
    "height",
    "building:levels",
    "min_height",
    "building",
    "ruian:building",
    "building:ruian:type",
    "building:units",
    "entrance",
    "website",
    "start_date",
    "ele",
    "operator",
    "source",
    "http://wiki.openstreetmap.org/wiki/Tag:tourism%3Dhotel"]
    ,
    """Casino""" :
    ["name",
    "name:en",
    "amenity",
    "leisure",
    "addr:country",
    "addr:city",
    "addr:postcode",
    "addr:street",
    "addr:housenumber",
    "contact",
    "phone",
    "website",
    "internet_access",
    "opening_hours",
    "wheelchair",
    "smoking",
    "shop",
    "operator",
    "http://wiki.openstreetmap.org/wiki/Tag:amenity%3Dcasino"]
    ,
    # ------------
    """Road""" :
    ["name",
    "name:en",
    "ref",
    "alt_name",
    "old_name",
    "highway",
    "railway",
    "bridge",
    "tunnel",
    "layer",
    "tracktype",
    "access",
    "fee",
    "construction",
    "minspeed",
    "maxspeed",
    "maxheight",
    "maxwidth",
    "maxweight",
    "foot",
    "bicycle",
    "bus",
    "cycleway",
    "motorcar",
    "horse",
    "hov",
    "hgv",
    "surface",
    "tracktype",
    "width",
    "lit",
    "traffic_calming",
    "parking:condition",
    "parking:lane",
    "lanes",
    "lanes:forward",
    "lanes:backward",
    "oneway",
    "turn:lanes",
    "sidewalk",
    "crossing",
    "http://wiki.openstreetmap.org/wiki/Key:highway"]
    ,
    """Railway""" :
    ["name",
    "name:en",
    "railway",
    "gauge",
    "electrified",
    "frequency",
    "voltage",
    "usage",
    "service",
    "rack",
    "electrified",
    "gauge",
    "frequency",
    "voltage",
    "rack",
    "bridge",
    "tunnel",
    "http://wiki.openstreetmap.org/wiki/Key:railway"]
    ,
    """Footway""" :
    ["name",
    "name:en",
    "highway",
    "footway",
    "foot",
    "access",
    "lit",
    "wheelchair",
    "sidewalk",
    "bicycle",
    "layer",
    "surface",
    "smoothness",
    "incline",
    "width",
    "sac_scale",
    "trail_visibility",
    "kerb",
    "crossing",
    "crossing_ref",
    "http://wiki.openstreetmap.org/wiki/Tag:highway%3Dfootway"]
    ,
    """Steps""" :
    ["name", 
    "name:en", 
    "highway", 
    "incline", 
    "step_count", 
    "conveying", 
    "handrail", 
    "tactile_paving", 
    "surface", 
    "ramp", 
    "ramp:stroller", 
    "ramp:bicycle", 
    "ramp:wheelchair", 
    "ramp:luggage", 
    "wheelchair", 
    "level", 
    "width", 
    "http://wiki.openstreetmap.org/wiki/Tag:highway=steps?uselang=en-US"]
    ,
    """Pedestrian zone""" :
    ["name",
    "name:en",
    "highway",
    "sidewalk",
    "bicycle",
    "motorcar",
    "motorcycle",
    "layer",
    "surface",
    "smoothness",
    "incline",
    "width",
    "ref",
    "http://wiki.openstreetmap.org/wiki/Tag:highway%3Dpedestrian"]
    ,
    """Aeroway""" :  # airports/aerodromes, grass airplane take off strips...
    ["name",
    "name:en",
    "aeroway",
    "iata",
    "faa",
    "IFR",
    "icao",
    "addr:country",
    "addr:city",
    "addr:postcode",
    "addr:street",
    "addr:housenumber",
    "phone",
    "aerodrome:type",
    "variation",
    "ele",
    "operator",
    "http://wiki.openstreetmap.org/wiki/Tag:aeroway%3Daerodrome"]
    ,
    """Bicycle parking""" :
    ["name",
    "name:en",
    "amenity",
    "highway",
    "fee",
    "addr:country",
    "addr:city",
    "addr:postcode",
    "addr:street",
    "addr:housenumber",
    "covered",
    "access",
    "capacity",
    "bicycle_parking",
    "cyclestreets_id",
    "maxstay",
    "surveillance",
    "operator",
    "http://wiki.openstreetmap.org/wiki/Tag:amenity%3Dbicycle_parking"]
    ,
    """Bicycle rental""" :
    ["name",
    "name:en",
    "amenity",
    "addr:country",
    "addr:city",
    "addr:postcode",
    "addr:street",
    "addr:housenumber",
    "shop",
    "ref",
    "capacity",
    "network",
    "operator",
    "http://wiki.openstreetmap.org/wiki/Tag:amenity%3Dbicycle_rental"]
    ,
    """Fuel""" :  #(fuel station, filling station, petrol station, gas station and petrol garage)
    ["name",
    "name:en",
    "amenity",
    "addr:country",
    "addr:city",
    "addr:postcode",
    "addr:street",
    "addr:housenumber",
    "opening_hours",
    "wheelchair",
    "opening_hours",
    "payment:cash",
    "payment:mastercard",
    "payment:visa",
    "payment:diners_club",
    "payment:american_express",
    "payment:maestro",
    "payment:dkv",
    "payment:uta",
    "fuel:diesel",
    "fuel:octane_91",
    "fuel:octane_95",
    "fuel:octane_98",
    "fuel:e10",
    "fuel:lpg",
    "building",
    "highway",
    "access",
    "covered",
    "access",
    "shop",
    "sanitary_dump_station",
    "surface",
    "brand",
    "operator",
    "tenant",
    "http://wiki.openstreetmap.org/wiki/Tag:amenity%3Dfuel"]
    ,
    """Parking""" :  #(facility use by the public or by customers or other authorised users for the parking of cars, trucks, motorcycles, etc.)
    ["name",
    "name:en",
    "amenity",
    "parking",
    "tourism",
    "landuse",
    "addr:country",
    "addr:city",
    "addr:postcode",
    "addr:street",
    "addr:housenumber",
    "building",  # this is not a mistake!
    "park_ride",
    "parking:lane",
    "parking:condition",
    "ref",
    "access",
    "highway",
    "multi-storey",
    "underground",
    "rooftop",
    "sheds",
    "carports",
    "garage_boxes",
    "park_ride",
    "fee",
    "supervised",
    "capacity",
    "capacity:disabled",
    "capacity:parent",
    "capacity:charging",
    "maxstay",
    "maxheight",
    "opening_hours",
    "lit",
    "surface",
    "vending",
    "operator",
    "http://wiki.openstreetmap.org/wiki/Tag:amenity%3Dparking"]
    ,
    """Garage""" :
    ["name",
    "name:en",
    "amenity",
    "landuse",
    "addr:country",
    "addr:city",
    "addr:postcode",
    "addr:street",
    "addr:housenumber",
    "building",  # this is not a mistake!
    "highway",
    "multi-storey",
    "underground",
    "rooftop",
    "garage_boxes",
    "fee",
    "supervised",
    "capacity",
    "capacity:disabled",
    "capacity:parent",
    "capacity:charging",
    "maxstay",
    "maxheight",
    "opening_hours",
    "lit",
    "surface",
    "vending",
    "operator",
    "http://wiki.openstreetmap.org/wiki/Tag:landuse%3Dgarages"]
    ,
    """Subway entrances""" :
    ["name",
    "name:en",
    "addr:country",
    "addr:city",
    "addr:postcode",
    "addr:street",
    "addr:housenumber",
    "railway",
    "public_transport",
    "ref",
    "bicycle",
    "wheelchair",
    "barrier",
    "oneway",
    "http://wiki.openstreetmap.org/wiki/Tag:railway%3Dsubway_entrance"]
    ,
    # ------------
    """Construction area""" :
    ["name",
    "name:en",
    "landuse",
    "building",
    "construction",
    "end_date",
    "operator",
    "http://wiki.openstreetmap.org/wiki/Tag:landuse%3Dconstruction"]
    ,
    """Archaeological site""" :
    ["name",
    "name:en",
    "historic",
    "historic:civilization",
    "natural",
    "site_type",
    "fortification_type",
    "opening_hours",
    "wheelchair",
    "sprockhoff",
    "ref:mhs",
    "moved",
    "megalith_type",
    "field",
    "tomb",
    "http://wiki.openstreetmap.org/wiki/Tag:historic%3Darchaeological_site"]
    ,
    """Fountain""" :
    ["name",
    "name:en",
    "amenity",
    "natural",
    "man_made",
    "drinking_water",
    "lit",
    "http://wiki.openstreetmap.org/wiki/Tag:amenity%3Dfountain"]
    ,
    """Wind turbine""" :
    ["power",
    "name",
    "name:en",
    "ref",
    "branch",
    "height",
    "rotor:diameter",
    "start_date",
    "generator:type",
    "generator:source",
    "generator:plant",
    "generator:output:biogas",
    "generator:output:electricity",
    "generator:output:hot_water",
    "generator:output:hot_air",
    "generator:output:cold_water",
    "generator:output:cold_air",
    "generator:output:compress_air",
    "generator:output:stream",
    "generator:output:vacuum",
    "voltage",
    "frequency",
    "operator",
    "http://wiki.openstreetmap.org/wiki/Tag:power%3Dgenerator"]
    ,
    """Plant""" :
    ["power",
    "name",
    "name:en",
    "ref",
    "height",
    "start_date",
    "type",
    "landuse",
    "waterway",
    "plant:output:electricity",
    "plant:output:hot_water",
    "plant:output:hot_air",
    "plant:output:cold_water",
    "plant:output:cold_air",
    "plant:output:compress_air",
    "plant:output:stream",
    "plant:output:vacuum",
    "voltage",
    "frequency",
    "operator",
    "http://wiki.openstreetmap.org/wiki/Tag:power%3Dplant"]
    ,
    """Nuclear reactor""" :
    ["power",
    "name",
    "name:en",
    "ref",
    "branch",
    "height",
    "start_date",
    "generator:type",
    "generator:source",
    "generator:plant",
    "generator:output:biogas",
    "generator:output:electricity",
    "generator:output:hot_water",
    "generator:output:hot_air",
    "generator:output:cold_water",
    "generator:output:cold_air",
    "generator:output:compress_air",
    "generator:output:stream",
    "generator:output:vacuum",
    "voltage",
    "frequency",
    "operator",
    "http://wiki.openstreetmap.org/wiki/Tag:power%3Dgenerator"]
    ,
    # ------------
    """Internet access""" :
    ["name",
    "name:en",
    "amenity",
    "tourism",
    "addr:country",
    "addr:city",
    "addr:postcode",
    "addr:street",
    "addr:housenumber",
    "internet_access",
    "wifi",
    "http://wiki.openstreetmap.org/wiki/Key:internet_access"]
    ,
    """Toilet""" :
    ["name",
    "name:en",
    "toilets",
    "amenity",
    "addr:country",
    "addr:city",
    "addr:postcode",
    "addr:street",
    "addr:housenumber",
    "access",
    "description",
    "drinking_water",
    "fee",
    "indoor",
    "opening_hours",
    "supervised",
    "wheelchair",
    "diaper",
    "entrance",
    "female",
    "male",
    "unisex",
    "toilets:disposal",
    "composting",
    "man_made",
    "operator",
    "http://wiki.openstreetmap.org/wiki/Tag:amenity%3Dtoilets"]
    ,
    """Building""" :
    ["name",
    "name:en",
    "building",
    "amenity",
    "addr:country",
    "addr:city",
    "addr:postcode",
    "addr:street",
    "addr:housenumber",
    "height",
    "building:levels",
    "building:min_level",
    "building:part",
    "min_height",
    "roof:height",
    "roof:shape",
    "roof:angle",
    "roof:material",
    "roof:color",
    "roof:levels",
    "entrance",
    "access",
    "http://wiki.openstreetmap.org/wiki/Buildings"]
    ,
    """Tree""" :
    ["name",
    "name:en",
    "natural",
    "landuse",
    "leaf_type",
    "leaf_cycle",
    "height",
    "circumference",
    "diameter_crown",
    "type",
    "genus",
    "species",
    "species:en",
    "taxon",
    "sex",
    "denotation",
    "historic",
    "http://wiki.openstreetmap.org/wiki/Tag:natural%3Dtree"]
    ,
    """Color""" :
    ["name",
    "name:en",
    "building:colour",
    "roof:colour",
    "colour",
    "building:roof:colour",
    "building:facade:colour",
    "natural",
    "leisure",
    "http://wiki.openstreetmap.org/wiki/Key:colour"]
    }
    
    
    requiredKeys_all = []
    OSMwebpage = []
    for name in OSMobjectName:
        if requiredKeys_dictionary.has_key(name):
            requiredKeys_perName_unsliced = requiredKeys_dictionary[name]
            OSMwebpage_perName = requiredKeys_perName_unsliced[-1]
            requiredKeys_perName = requiredKeys_perName_unsliced[:-1]
            requiredKeys_all.extend(requiredKeys_perName)
            OSMwebpage.append(OSMwebpage_perName)
    
    requiredKeys_unique = list(set(requiredKeys_all))  # only pick unique keys
    requiredKeys_unique.sort()  # sort them alphabetically
    
    if (len(requiredKeys_unique) == 0):
        # "_OSMobjectName" does not exist in upper "requiredKeys_dictionary"
        requiredKeys_unique = []
        OSMwebpage = None
        validInputData = False
        printMsg = "Supplied \"_OSMobjectName\" does not exist among this component's data.\n" + \
                   "Try creating your own \"requiredKeys\" output manually by looking at:\n \n" + \
                   "http://taginfo.openstreetmap.org/keys"
        return requiredKeys_unique, OSMwebpage, validInputData, printMsg
    
    
    resultsCompletedMsg = "OSM keys component results successfully completed!\n \nInput data:\n \nOSMobjectName: %s" % OSMobjectName
    print resultsCompletedMsg
    
    validInputData = True
    printMsg = "ok"
    
    return requiredKeys_unique, OSMwebpage, validInputData, printMsg


level = Grasshopper.Kernel.GH_RuntimeMessageLevel.Warning
if sc.sticky.has_key("gismoGismo_released"):
    validVersionDate, printMsg = sc.sticky["gismo_check"].versionDate(ghenv.Component)
    if validVersionDate:
        requiredKeys, OSMwebpage, validInputData, printMsg = main(_OSMobjectName)
        if not validInputData:
            print printMsg
            ghenv.Component.AddRuntimeMessage(level, printMsg)
    else:
        print printMsg
        ghenv.Component.AddRuntimeMessage(level, printMsg)
else:
    printMsg = "First please run the Gismo Gismo component."
    print printMsg
    ghenv.Component.AddRuntimeMessage(level, printMsg)
