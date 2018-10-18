from pcapng import FileScanner
from pcapng.blocks import *
from pcapng.utils import *
import numpy as np

prev = []
with open('capture.pcapng', 'rb') as fp:
    scanner = FileScanner(fp)
    for block in scanner:
      if type(block) is SectionHeader or \
         type(block) is InterfaceDescription:
         continue
      elif  type(block) is EnhancedPacket:
        if np.array_equal(prev, block):
          continue
        print block.packet_data
      else:
        print type(block)

