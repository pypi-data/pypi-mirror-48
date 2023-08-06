from __future__ import absolute_import, division

import numpy as np
from fisspy.image.base import rot
from fisspy import cm
import sunpy.map
from sunpy.coordinates import frames
from astropy.coordinates import SkyCoord
from sunpy.coordinates.ephemeris import get_earth
from sunpy.physics.differential_rotation import solar_rotate_coordinate
from interpolation.splines import LinearSpline

__author__="Juhyeong Kang"
__email__="jhkang@astro.snu.ac.kr"

__all__=["fissMap", "map_header", "align", "map_rot_correct"]

def fissMap(data0,header0,pre_align=False,**kwargs):
    """
    Make sunpy.map.Map for given data and header.
    
    Parameters
    ----------
    data0 : ~numpy.ndarray
        2 dimensional image.
    header0 : astropy.io.fits.Header
        FTS file header.\n
        It must has the wcs informations.
    pre_align : bool
        If False, data0 is aligned with its wcs information.
    kwargs
        plot_setting keyword arguments. \n
        See : `sunpy.map <http://docs.sunpy.org/en/stable/code_ref/map.html>`_
    
    Returns
    -------
    fmap : sunpy.map.GenericMap
        Map class.
        
    See Also
    --------
    fisspy.image.coalignment.match_wcs : The routine to match wcs information
        of FISS data with SDO
    
    Notes
    -----
    The header0 must has the infromations of the coalignment for FISS with SDO.
    
    .. warning::
        This code use the SunPy Map structure, but it may has errors
        since sunpy is the developing package.
    
    References
    ----------
    `SunPy <http://sunpy.org/>`_.\n
    `SunPy docs <http://docs.sunpy.org/en/stable/>`_.\n
    `sunpy.map.Map <http://docs.sunpy.org/en/stable/code_ref/map.html>`_.
    
    
    Example
    -------
    .. plot::
        :include-source:
            
        from fisspy.io import read
        from fisspy.map.map_factory import fissmap
        import fisspy.data.sample
        raster=read.raster(fisspy.data.sample.FISS_IMAGE,0,smooth=True)
        header=read.getheader(fisspy.data.sample.FISS_IMAGE)
        fmap=fissmap(raster,header)
        fmap.peek()
    """
    if data0.ndim !=2:
        raise ValueError('Data must be 2-dimensional numpy.ndarray')
    
    if not pre_align:
        data,header=align(data0,header0)
    else:
        data=data0.copy()
        header=map_header(header0)
        header['crpix1']=header['crpix1']+header['shift1']+header['margin1']
        header['crpix2']=header['crpix2']+header['shift2']+header['margin2']
        header['crota2']=0
        
    fmap=sunpy.map.Map(data,header)
    fmap.plot_settings['title']=fmap.name.replace('Angstrom','')
    fmap.plot_settings['title']=fmap.plot_settings['title'].replace('6562.8',r'H$\alpha$')
    fmap.plot_settings['title']=fmap.plot_settings['title'].replace('8542.0','Ca II')
    interp=kwargs.pop('interpolation','bilinear')
    fmap.plot_settings['interpolation']=interp
    clim=kwargs.pop('clim',False)
    if clim:
        fmap.plot_settings['clim']=clim
    cmap=kwargs.pop('cmap',False)
    if cmap:
        fmap.plot_settings['cmap']=cmap
    else:
        if header['wavelen']=='6562.8':
            fmap.plot_settings['cmap'] = cm.ha
        elif header['wavelen']=='8542':
            fmap.plot_settings['cmap'] = cm.ca
    title=kwargs.pop('title',False)
    if title:
        fmap.plot_settings['title']=title

    return fmap
    
def map_header(header0):
    """
    Header change to correct the fissmap
    """
    header=header0.copy()
    header['naxis']=2
    
    if header['reflect']:
        header['naxis1']=header['naxis2']
        header['naxis2']=header['naxis3']
        header['crpix1']=header['crpix2']
        header['crpix2']=header['crpix3']
        header['crval1']=header['crval3']
        header['cdelt1']=header['cdelt2']
        header['cdelt2']=header['cdelt3']
        header['shift1']=header['shift2']
        header['shift2']=header['shift3']
        header['crota2']=np.rad2deg(header['crota2'])
        header['margin1']=header['margin2']
        header['margin2']=header['margin3']
        header.remove('naxis3')
        header.remove('crpix3')
        header.remove('crval3')
        header.remove('cdelt3')
        header.remove('crota1')
        header.remove('shift3')
    else:
        header['naxis1']=header['naxis3']
        header['crpix1']=header['crpix3']
        header['crval1']=header['crval3']
        header['cdelt1']=header['cdelt3']
        header['shift1']=header['shift3']
        header['crota2']=np.rad2deg(header['crota2'])
        header['margin1']=header['margin3']
        header.remove('naxis3')
        header.remove('crpix3')
        header.remove('crval3')
        header.remove('cdelt3')
        header.remove('crota1')
        header.remove('shift3')
    
    header['instrume']='FISS'
    header['detector']='FISS'
    header['telescop']='GST'
    header['wavelnth']=float(header['wavelen'])
    header['waveunit']='Angstrom'
    header['date-obs']=header['date']
    return header 

def align(data0,header0,missing=0):
    """
    Align the input data with its header.
    
    Header must has the wcs informations.
    
    Parameters
    ----------
    data0 : ~numpy.ndarray
        2 dimensional numpy array.
    header0 : astropy.io.fits.Header
        An Header for input data.
    missing : (optional) float
        Missing value for 2d interpolation.
        
    Returns
    -------
    img : ~numpy.ndarray
    mheader : astropy.io.fits.Header
    
    Notes
    -----
    The header0 must has the infromations of the coalignment for FISS with SDO.
    """
    mheader=map_header(header0)
    reflect=mheader['reflect']
    
    if reflect:
        data=data0.T
        
    xmargin=mheader['margin1']
    ymargin=mheader['margin2']
    
    
    img=rot(data,np.deg2rad(mheader['crota2']),mheader['crpix1'],
            mheader['crpix2'],mheader['shift1'],mheader['shift2'],
            mheader['margin1'],mheader['margin2'])
    
    mheader['crpix1']=mheader['crpix1']+mheader['shift1']+xmargin
    mheader['crpix2']=mheader['crpix2']+mheader['shift2']+ymargin
    mheader['crota2']=0
    
    return img, mheader
    

def map_rot_correct(mmap,refx,refy,reftime):
    """
    Correct the solar rotation.
    
    Parameters
    ----------
    mmap : sunpy.map.GenericMap
        Single map class.
    refx : astropy.units.Quantity
        Horizontal wcs information of reference frame.
    refy : astropy.units.Quantity
        Vertical wcs information of reference frame.
    reftime : astropy.time.Time
        Time for the reference frame.
    
    Returns
    -------
    smap : sunpy.map.GenericMap
        Solar rotation corrected map class.
    
    """
    
    refc = SkyCoord(refx, refy, obstime= reftime,
                    observer= get_earth(reftime),
                    frame= frames.Helioprojective)
    
    date = mmap.date
    res = solar_rotate_coordinate(refc, date ,frame_time= 'synodic')
    x = res.Tx.value
    y = res.Ty.value
    
    sx = x - refx.value
    sy = y - refy.value
    mmap.shift
    smap = _mapShift(mmap, sx, sy)
    return smap

def _mapShift(map1, sx, sy):
    
    new_meta = map1.meta.copy()
    new_meta['crval1'] = ((map1.meta['crval1']*
                           map1.spatial_units[0] +
                           sx * map1.spatial_units[0]).to(map1.spatial_units[0])).value
    new_meta['crval2'] = ((map1.meta['crval2']*
                           map1.spatial_units[0] +
                           sy * map1.spatial_units[0]).to(map1.spatial_units[0])).value
    delx = sx/map1.meta['cdelt1']
    dely = sy/map1.meta['cdelt2']
    
    smin = [0, 0]
    smax = [new_meta['naxis2']-1, new_meta['naxis1']-1]
    order = map1.data.shape
    interp = LinearSpline(smin, smax, order, map1.data)
    
    x = np.arange(new_meta['naxis1'], dtype=float)
    xx0 = x * np.ones([new_meta['naxis2'],1])
    xx = xx0 + delx
    y = np.arange(new_meta['naxis2'], dtype=float)
    yy0 = y[:,None] + np.ones(new_meta['naxis1'])
    yy = yy0 + dely
    size = new_meta['naxis1']*new_meta['naxis2']
    inp = np.array([yy.reshape(size), xx.reshape(size)])
    out = interp(inp.T)
    
    out = out.reshape(new_meta['naxis2'], new_meta['naxis1'])
    mask = np.invert((xx<=xx0.max())*(xx>=xx0.min())*(yy<=yy0.max())*(yy>=yy0.min()))
    out[mask] = 0
    newMap = map1._new_instance(out, new_meta, map1.plot_settings)
    
    return newMap
    