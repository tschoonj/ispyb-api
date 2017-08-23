#!/usr/bin/env python
# shipping.py
#
#    Copyright (C) 2017 Diamond Light Source, Karl Levik
#    
# 2017-06-28 
#
# Methods to update data related to shipping of samples
#

import string
import logging
import time
import os
import sys
import datetime
from logging.handlers import RotatingFileHandler
from collections import OrderedDict
import copy
from ispyb.ExtendedOrderedDict import ExtendedOrderedDict

class Shipping:
  '''Shipping provides methods to update shipments and samples.'''

  def __init__(self):
    pass

# IN p_beamline varchar(20), IN p_registry_barcode varchar(45), IN p_position int
  def update_container_assign(self, cursor, beamline, registry_barcode, position):
    '''Assign a container'''
    result_args = cursor.callproc(procname='ispyb.update_container_assign', args=(beamline, registry_barcode, position))

shipping = Shipping()


