import numpy as np
import matplotlib as mpl
from matplotlib import style
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap as lscmap
plt.rcParams['text.usetex'] = True

def spectype_colormap(temps, log_flag = False):
    ##########################################################
    # Function: spectype_colormap                            #
    # Purpose: creates a custom color bar coordinated with   #
    #          the temperature, spectral types, and colors   #
    #          associated with each spectral type            #
    #          SpecType | Color      | Temp Range (K)        #
    #             M     | Red        | 2000-3500             #
    #             K     | Orange     | 3500-4900             #
    #             G     | Yellow     | 4900-6000             #
    #             F     | White      | 6000-7500             #
    #             A     | White-Blue | 7500-10000            #
    #             B     | Blue-White | 10000-28000           # 
    #             O     | Blue       | 28000-50000           #
    # To use:                                                #
    #        1. Create an array of temperatures.             #
    #        2. Call the function and set the log_flag       #
    #           If log_flag is True:                         #
    #             make sure your array of temps are in log10 #
    #           If log_flag is False:                        #
    #             make sure your array of temps are not in   #
    #             log space                                  #
    #        3. Function will output the following:          #
    #           SpecTypeCmap: the defined colormap           #
    #           normal_data: normalized temperatures         #
    #           normal_ranges_cbar: normalized ranges for    #
    #                               the color bar            #
    #           cbarlabel_pos: zipped list defining the      #
    #                          colorbar spectral type labels,#
    #                          the x-pos, and y-pos of the   #
    #                          colorbar label                #
    # Example:                                               #
    #   #Import the function                                 #
    #   from spectype_colormap import spectype_colormap      #
    #   #Call the color-map function                         #
    #   custom_cmap, normal_d, normal_r_cbar, cbarlabs =     #
    #   spectype_colormap(teffs, log_flag = False)           #
    #   #Plot your data and use the outputs from the color   #
    #   #map function above                                  #
    #   ax = plt.scatter(teffs,lums, c = normal_d,           #
    #                    cmap = custom_cmap)                 #
    #   #Plot the colorbar using the output from the func.   #
    #   cbar = plt.colorbar(ax, ticks= normal_r_cbar)        #
    #   #Label the colorbar with the spectral type labels    #
    #   for i in range(len(cbarlabs)):                       #
    #        cbar.ax.text(cbarlabs[i][1], cbarlabs[i][2],    #
    #                     cbarlabs[i][0], fontsize = 15)     #
    ##########################################################

    colors = ['xkcd:red', 'xkcd:tangerine', 'xkcd:yellow', 'xkcd:white', 'xkcd:powder blue', 'xkcd:cool blue', 'xkcd:deep blue']
    cbarlabels = [r'$\rm \textbf{M}$', r'$\rm \textbf{K}$', r'$\rm \textbf{G}$', r'$\rm \textbf{F}$', r'$\rm \textbf{A}$', r'$\rm \textbf{B}$', r'$\rm \textbf{O}$']
    teffs = temps
    if log_flag:
        teff_ranges = np.array([np.log10(2000),np.log10(3500),np.log10(4900),np.log10(6000),np.log10(7500),np.log10(10000),np.log10(28000)])
        teff_ranges_cbar= np.array([3.25,np.log10(2000),np.log10(3500),np.log10(4900),np.log10(6000),np.log10(7500),np.log10(10000),np.log10(28000), 4.55])
        cbarlabel_xpos = np.array([0.127, 0.29, 0.38, 0.45, 0.53, 0.75, 0.97])
        cbarlabel_ypos = np.array([0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35])
        normal_ranges = (teff_ranges-min(teff_ranges))/(max(teff_ranges)-min(teff_ranges))
        normal_ranges_cbar = (teff_ranges_cbar-min(teff_ranges_cbar))/(max(teff_ranges_cbar)-min(teff_ranges_cbar))
    if not log_flag:
        teff_ranges = np.array([2000, 3500, 4900,6000,7500,10000,28000])
        teff_ranges_cbar = np.array([1500, 2000,3500,4900,6000,7500,10000,28000, 35000])
        cbarlabel_xpos = np.array([0.01, 0.045, 0.09, 0.125, 0.165, 0.225, 0.80])
        cbarlabel_ypos = np.array([-0.6, -0.6, -0.6, -0.6, -0.6, -0.6, -0.6])
        normal_ranges = (teff_ranges-min(teff_ranges))/(max(teff_ranges)-min(teff_ranges))
        normal_ranges_cbar = (teff_ranges_cbar-min(teff_ranges_cbar))/(max(teff_ranges_cbar)-min(teff_ranges_cbar))
    
    color_segs = list(zip(normal_ranges, colors))
    SpecTypeCmap = lscmap.from_list('SpecType_cmap', color_segs)

    normal_data = (teffs-min(teffs))/(max(teffs)-min(teffs))
    cbarlabel_pos = list(zip(cbarlabels, cbarlabel_xpos, cbarlabel_ypos))
    
    return SpecTypeCmap, normal_data, normal_ranges_cbar, cbarlabel_pos