from . import chart_framework
from . import chart_setup
from . import utils
import pandas as pd
import numpy as np


class Radar(chart_setup.Chart_init):
    
    title = 'Radar Chart'
    chart_type = 'radar'

    def __init__(self, options=None, title = None, *pargs, **kwargs):
        super(Radar, self).__init__(title = title, *pargs, **kwargs)
        if options is None:
            options = utils.options(
					responsive=True,
                    legend=dict(position="top"),
                    title=dict(display=True, text=self.title),
					tooltips = dict(mode='index', intersect = False),
					scales = utils.scales(ticks = {'beginAtZero': True})
            )
        self.options = options
        self.reset()

    