import numpy as numpy
from astropy import units
import math
from . import Tools
from .Formatter import formatter as fmt
from .Engine import Engine

__author__ = "Do Kester"
__year__ = 2017
__license__ = "GPL3"
__version__ = "0.9"
__maintainer__ = "Do"
__status__ = "Development"

#  *
#  * This file is part of the BayesicFitting package.
#  *
#  * BayesicFitting is free software: you can redistribute it and/or modify
#  * it under the terms of the GNU Lesser General Public License as
#  * published by the Free Software Foundation, either version 3 of
#  * the License, or ( at your option ) any later version.
#  *
#  * BayesicFitting is distributed in the hope that it will be useful,
#  * but WITHOUT ANY WARRANTY; without even the implied warranty of
#  * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  * GNU Lesser General Public License for more details.
#  *
#  * The GPL3 license can be found at <http://www.gnu.org/licenses/>.
#  *
#  * A JAVA version of this code was part of the Herschel Common
#  * Science System (HCSS), also under GPL3.
#  *
#  *    2010 - 2014 Do Kester, SRON (Java code)
#  *    2017        Do Kester

class StartEngine( Engine ):
    """
    StartEngine generates a random trial sample.

    It is used to initialize the set of trial samples.

    Author       Do Kester.

    """
    #  *********CONSTRUCTORS***************************************************
    def __init__( self, walkers, errdis, copy=None, seed=4213, verbose=0 ):
        """
        Constructor.
        Parameters
        ----------
        copy : StartEngine
            engine to be copied

        """
        super( ).__init__( walkers, errdis, copy=copy, seed=seed, verbose=verbose )

    def copy( self ):
        """ Return copy of this.  """
        return StartEngine( self.walkers, self.errdis, copy=self )

    def __str__( self ):
        return str( "StartEngine" )

    #  *********EXECUTE***************************************************
    def execute( self, walker, lowLhood ):
        """
        Execute the engine by a random selection of the parameters.

        Parameters
        ----------
        walker : Sample
            sample to diffuse
        lowLhood : float
            lower limit in logLikelihood

        Returns
        -------
        int : the number of successfull moves

        """
        problem = walker.problem
        fitIndex = walker.fitIndex
        par = walker.allpars.copy()

#        print( "FI   ", fitIndex )

        ktry = 0
        while True :
            uval = self.rng.rand( len( fitIndex ) )
            par[fitIndex] = self.unit2Domain( problem, uval, kpar=fitIndex )

#           ## fiture extension
#           if self.constrain :
#               xdata = self.errdis.xdata
#               par = self.constrain( model, par, xdata )

            logL = self.errdis.logLikelihood( problem, par )

            if numpy.isfinite( logL ) :
                break
            elif ktry > ( self.maxtrials + walker.id ) :
                raise RuntimeError( "Cannot find valid starting solutions" )
            else :
                ktry += 1

        self.setWalker( walker, problem, par, logL, fitIndex=fitIndex )

        return len( fitIndex )


