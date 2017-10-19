#!/usr/bin/env python

import context
import sys
import os
from xml.etree import ElementTree
from datetime import datetime
from ispyb.xmltools import XmlDictConfig, mx_data_reduction_xml_to_ispyb
from testtools import get_mxprocessing

def test_mx_data_reduction_xml_to_ispyb():
    xml_file = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/mx_data_reduction_pipeline_results.xml'))
    # Convert the XML to a dictionary
    tree = ElementTree.parse(xml_file)
    xmldict = XmlDictConfig( tree.getroot() )

    # Find the datacollection associated with this data reduction run
    xml_dir = os.path.split(xml_file)[0]
    try:
        dc_id = int(open(os.path.join(xml_dir, '.dc_id'), 'r').read())
        print('Got DC ID %d from file system' % dc_id)
    except:
        dc_id = None

    (app_id, ap_id, scaling_id, integration_id) = mx_data_reduction_xml_to_ispyb(xmldict, dc_id, get_mxprocessing())

    # Output results xml
    xml = '<?xml version="1.0" encoding="ISO-8859-1"?>'\
            '<dbstatus><autoProcProgramId>%d</autoProcProgramId>'\
            '<autoProcId>%d</autoProcId>'\
            '<autoProcScalingId>%d</autoProcScalingId>'\
            '<autoProcIntegrationId>%d</autoProcIntegrationId>'\
            '<code>ok</code></dbstatus>' % (app_id, ap_id, scaling_id, integration_id)
    print(xml)