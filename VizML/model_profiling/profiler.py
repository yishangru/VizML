"""
Input:
dict -> list ->
{"tensor":
     {"mem":
          {"max": 0, "min": float("inf")},
      "grad":
          {"max": 0, "min": float("inf")}
      },
 "layer":
     {"mem":
          {"max": 0, "min": float("inf")},
      "grad":
          {"max": 0, "min": float("inf")}
      }
}

"""

import numpy as np
import matplotlib.pyplot as plt

class BlockProfiler(object):
    def __init__(self, generationPath: str):
        self.generationPath = generationPath

    def generateBlockImage(self, blockMemDict):
        for block in blockMemDict:
            # just for max and min
            pass