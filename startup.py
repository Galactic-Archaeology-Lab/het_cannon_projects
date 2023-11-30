from numpy import *
<<<<<<< HEAD
=======
# hi keith
#hi Zoe. I hope you are having a good day
>>>>>>> b2914ec4eab4cef841b12a520a35815f5981932d
import pylab as p
from matplotlib import *
import astropy
import re
from utils import *
import numpy.random as rand
import pickle
import scipy
#import pyfits
import astropy.io.fits as pyfits
import csv
import astropy
from astropy.table import Table
from importlib import reload

# p.rcParams['axes.color_cycle']='k','b','g','r','c','m','y'
# p.rcParams['axes.labelsize']='x-large'
# p.rcParams['xtick.labelsize'] = 'x-large' # fontsize of the tick labels
# p.rcParams['ytick.labelsize']='x-large'

# p.rcParams['axes.linewidth']=2.0
# p.rcParams['lines.linewidth']=2.0
# p.rcParams['savefig.dpi']=300
# p.rcParams['savefig.format']='pdf'
# #p.rcParams['ps.useafm'] = True
# #p.rcParams['pdf.use14corefonts'] = True
# p.rcParams['text.usetex'] = True

# p.rc('font',**{'family':'sans-serif','sans-serif':['Times'],'size':16}) 
# p.rcParams['ps.fonttype'] = 42
# p.rcParams['pdf.fonttype'] = 42

#---andys---
p.rc('axes',prop_cycle=(cycler('color', ['k','b','g','r','c','m','y'])))
p.rcParams['lines.linewidth']= 1.5
p.rcParams['axes.linewidth']=2.0

p.rcParams['text.usetex']= True
#p.rcParams['font.family']='times'
p.rcParams['mathtext.fontset']= 'custom'
p.rcParams['mathtext.default']= 'rm'

p.rcParams['font.size']= 15.0
p.rcParams['axes.formatter.use_mathtext']=False
p.rcParams['axes.labelsize']=16.0
p.rcParams['axes.unicode_minus']=False
p.rcParams['xtick.major.size']=6
p.rcParams['xtick.minor.size']=3
p.rcParams['xtick.major.width']=1.5#2.0
p.rcParams['xtick.minor.width']=1.0

p.rcParams['axes.linewidth']=2.5
#p.rcParams['axes.labelsize']='medium'
p.rcParams['axes.titlesize']=20#'large'
#p.rcParams['xtick.labelsize'] = 'medium' # fontsize of the tick labels
#p.rcParams['ytick.labelsize']='medium'
p.rcParams['xtick.labelsize'] = 20#'x-large' # fontsize of the tick labels
p.rcParams['ytick.labelsize']=20 #'x-large'


#p.rcParams['ytick.major.size']=6
#p.rcParams['ytick.minor.size']=3
p.rcParams['ytick.major.width']=2.0 #4
p.rcParams['ytick.minor.width']=1.0 #2.0
p.rcParams['ps.fonttype'] = 42
p.rcParams['pdf.fonttype'] = 42
p.rcParams['savefig.dpi']=300
p.rcParams['savefig.format']='pdf'


#params = {
#          'text.usetex': True,
#          }
#pylab.rcParams.update(params)
