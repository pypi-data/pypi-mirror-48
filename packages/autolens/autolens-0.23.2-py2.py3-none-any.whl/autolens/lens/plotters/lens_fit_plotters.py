import autofit as af
import matplotlib
backend = af.conf.instance.visualize.get('figures', 'backend', str)
matplotlib.use(backend)
from matplotlib import pyplot as plt

from autolens.plotters import plotter_util
from autolens.lens.plotters import lens_plotter_util
from autolens.lens.plotters import plane_plotters
from autolens.model.inversion.plotters import inversion_plotters


def plot_lens_fit_for_phase(
        fit, during_analysis, extract_array_from_mask, zoom_around_mask, positions, units,
        should_plot_mask,
        should_plot_image_plane_pix,
        should_plot_as_subplot,
        should_plot_all_at_end_png,
        should_plot_all_at_end_fits,
        should_plot_image,
        should_plot_noise_map,
        should_plot_signal_to_noise_map,
        should_plot_lens_subtracted_image,
        should_plot_model_image,
        should_plot_lens_model_image,
        should_plot_source_model_image,
        should_plot_source_plane_image,
        should_plot_residual_map,
        should_plot_chi_squared_map,
        should_plot_regularization_weights,
        visualize_path):

    output_path = visualize_path

    if should_plot_as_subplot:
        
        plot_fit_subplot(
            fit=fit, should_plot_mask=should_plot_mask,
            extract_array_from_mask=extract_array_from_mask, zoom_around_mask=zoom_around_mask,
            positions=positions, should_plot_image_plane_pix=should_plot_image_plane_pix,
            units=units,
            output_path=output_path, output_format='png')

    plot_fit_individuals(
        fit=fit, should_plot_mask=should_plot_mask,
        extract_array_from_mask=extract_array_from_mask, zoom_around_mask=zoom_around_mask,
        positions=positions, should_plot_image_plane_pix=should_plot_image_plane_pix,
        should_plot_image=should_plot_image,
        should_plot_noise_map=should_plot_noise_map,
        should_plot_signal_to_noise_map=should_plot_signal_to_noise_map,
        should_plot_lens_subtracted_image=should_plot_lens_subtracted_image,
        should_plot_model_image=should_plot_model_image,
        should_plot_lens_model_image=should_plot_lens_model_image,
        should_plot_source_model_image=should_plot_source_model_image,
        should_plot_source_plane_image=should_plot_source_plane_image,
        should_plot_residual_map=should_plot_residual_map,
        should_plot_chi_squared_map=should_plot_chi_squared_map,
        should_plot_regularization_weights=should_plot_regularization_weights,
        units=units,
        output_path=output_path, output_format='png')

    if not during_analysis:

        if should_plot_all_at_end_png:

            plot_fit_individuals(
                fit=fit, should_plot_mask=should_plot_mask,
                extract_array_from_mask=extract_array_from_mask, zoom_around_mask=zoom_around_mask,
                positions=positions, should_plot_image_plane_pix=should_plot_image_plane_pix,
                should_plot_image=True,
                should_plot_noise_map=True,
                should_plot_signal_to_noise_map=True,
                should_plot_lens_subtracted_image=True,
                should_plot_model_image=True,
                should_plot_lens_model_image=True,
                should_plot_source_model_image=True,
                should_plot_source_plane_image=True,
                should_plot_residual_map=True,
                should_plot_chi_squared_map=True,
                units=units,
                output_path=output_path, output_format='png')

        if should_plot_all_at_end_fits:

            plot_fit_individuals(
                fit=fit, should_plot_mask=should_plot_mask,
                extract_array_from_mask=extract_array_from_mask, zoom_around_mask=zoom_around_mask,
                positions=positions, should_plot_image_plane_pix=should_plot_image_plane_pix,
                should_plot_image=True,
                should_plot_noise_map=True,
                should_plot_signal_to_noise_map=True,
                should_plot_lens_subtracted_image=True,
                should_plot_model_image=True,
                should_plot_lens_model_image=True,
                should_plot_source_model_image=True,
                should_plot_source_plane_image=True,
                should_plot_residual_map=True,
                should_plot_chi_squared_map=True,
                output_path=output_path + 'fits/', output_format='fits')

def plot_fit_subplot(
        fit, should_plot_mask=True, extract_array_from_mask=False, zoom_around_mask=False, positions=None,
        should_plot_image_plane_pix=False, plot_mass_profile_centres=True,
        units='arcsec', figsize=None, aspect='square',
        cmap='jet', norm='linear', norm_min=None, norm_max=None, linthresh=0.05, linscale=0.01,
        cb_ticksize=10, cb_fraction=0.047, cb_pad=0.01, cb_tick_values=None, cb_tick_labels=None,
        titlesize=10, xlabelsize=10, ylabelsize=10, xyticksize=10,
        mask_pointsize=10, position_pointsize=10, grid_pointsize=1,
        output_path=None, output_filename='lens_fit', output_format='show'):

    if fit.tracer.total_planes == 1:

        plot_fit_subplot_lens_plane_only(
            fit=fit, should_plot_mask=should_plot_mask, extract_array_from_mask=extract_array_from_mask, zoom_around_mask=zoom_around_mask, positions=positions,
            should_plot_image_plane_pix=should_plot_image_plane_pix,
            units=units, figsize=figsize, aspect=aspect,
            cmap=cmap, norm=norm, norm_min=norm_min, norm_max=norm_max, linthresh=linthresh, linscale=linscale,
            cb_ticksize=cb_ticksize, cb_fraction=cb_fraction, cb_pad=cb_pad, 
        cb_tick_values=cb_tick_values, cb_tick_labels=cb_tick_labels,
            titlesize=titlesize, xlabelsize=xlabelsize, ylabelsize=ylabelsize, xyticksize=xyticksize,
            mask_pointsize=mask_pointsize, position_pointsize=position_pointsize, grid_pointsize=grid_pointsize,
            output_path=output_path, output_filename=output_filename, output_format=output_format)

    elif fit.tracer.total_planes >= 2:

        plot_fit_subplot_lens_and_source_planes(
            fit=fit, should_plot_mask=should_plot_mask, extract_array_from_mask=extract_array_from_mask, zoom_around_mask=zoom_around_mask, positions=positions,
            should_plot_image_plane_pix=should_plot_image_plane_pix, plot_mass_profile_centres=plot_mass_profile_centres,
            units=units, figsize=figsize, aspect=aspect,
            cmap=cmap, norm=norm, norm_min=norm_min, norm_max=norm_max, linthresh=linthresh, linscale=linscale,
            cb_ticksize=cb_ticksize, cb_fraction=cb_fraction, cb_pad=cb_pad, 
        cb_tick_values=cb_tick_values, cb_tick_labels=cb_tick_labels,
            titlesize=titlesize, xlabelsize=xlabelsize, ylabelsize=ylabelsize, xyticksize=xyticksize,
            mask_pointsize=mask_pointsize, position_pointsize=position_pointsize, grid_pointsize=grid_pointsize,
            output_path=output_path, output_filename=output_filename, output_format=output_format)

def plot_fit_subplot_lens_plane_only(
        fit, should_plot_mask=True, extract_array_from_mask=False, zoom_around_mask=False, positions=None,
        should_plot_image_plane_pix=False,
        units='arcsec', figsize=None, aspect='square',
        cmap='jet', norm='linear', norm_min=None, norm_max=None, linthresh=0.05, linscale=0.01,
        cb_ticksize=10, cb_fraction=0.047, cb_pad=0.01, cb_tick_values=None, cb_tick_labels=None,
        titlesize=10, xlabelsize=10, ylabelsize=10, xyticksize=10,
        mask_pointsize=10, position_pointsize=10, grid_pointsize=1,
        output_path=None, output_filename='lens_fit', output_format='show'):
    """Plot the model datas_ of an analysis, using the *Fitter* class object.

    The visualization and output type can be fully customized.

    Parameters
    -----------
    fit : autolens.lens.fitting.Fitter
        Class containing fit between the model datas_ and observed lens datas_ (including residual_map, chi_squared_map etc.)
    output_path : str
        The path where the datas_ is output if the output_type is a file format (e.g. png, fits)
    output_filename : str
        The name of the file that is output, if the output_type is a file format (e.g. png, fits)
    output_format : str
        How the datas_ is output. File formats (e.g. png, fits) output the datas_ to harddisk. 'show' displays the datas_ \
        in the python interpreter window.
    """

    rows, columns, figsize_tool = plotter_util.get_subplot_rows_columns_figsize(number_subplots=6)

    mask = lens_plotter_util.get_mask(fit=fit, should_plot_mask=should_plot_mask)

    if figsize is None:
        figsize = figsize_tool

    plt.figure(figsize=figsize)
    plt.subplot(rows, columns, 1)

    kpc_per_arcsec = fit.tracer.image_plane.kpc_per_arcsec

    image_plane_pix_grid = lens_plotter_util.get_image_plane_pix_grid(should_plot_image_plane_pix, fit)

    lens_plotter_util.plot_image(
        fit=fit, mask=mask, extract_array_from_mask=extract_array_from_mask, zoom_around_mask=zoom_around_mask,
        positions=positions, image_plane_pix_grid=image_plane_pix_grid, as_subplot=True,
        units=units, kpc_per_arcsec=kpc_per_arcsec, figsize=figsize, aspect=aspect,
        cmap=cmap, norm=norm, norm_min=norm_min, norm_max=norm_max, linthresh=linthresh, linscale=linscale,
        cb_ticksize=cb_ticksize, cb_fraction=cb_fraction, cb_pad=cb_pad, 
        cb_tick_values=cb_tick_values, cb_tick_labels=cb_tick_labels,
        titlesize=titlesize, xlabelsize=xlabelsize, ylabelsize=ylabelsize, xyticksize=xyticksize,
        grid_pointsize=grid_pointsize, position_pointsize=position_pointsize, mask_pointsize=mask_pointsize,
        output_path=output_path, output_filename='', output_format=output_format)

    plt.subplot(rows, columns, 2)

    lens_plotter_util.plot_noise_map(
        fit=fit, mask=mask, extract_array_from_mask=extract_array_from_mask, zoom_around_mask=zoom_around_mask,
        positions=positions, as_subplot=True,
        units=units, kpc_per_arcsec=kpc_per_arcsec, figsize=figsize, aspect=aspect,
        cmap=cmap, norm=norm, norm_min=norm_min, norm_max=norm_max, linthresh=linthresh, linscale=linscale,
        cb_ticksize=cb_ticksize, cb_fraction=cb_fraction, cb_pad=cb_pad, 
        cb_tick_values=cb_tick_values, cb_tick_labels=cb_tick_labels,
        titlesize=titlesize, xlabelsize=xlabelsize, ylabelsize=ylabelsize, xyticksize=xyticksize,
        position_pointsize=position_pointsize, mask_pointsize=mask_pointsize,
        output_path=output_path, output_filename='', output_format=output_format)

    plt.subplot(rows, columns, 3)

    lens_plotter_util.plot_signal_to_noise_map(
        fit=fit, mask=mask, extract_array_from_mask=extract_array_from_mask, zoom_around_mask=zoom_around_mask,
        positions=positions, as_subplot=True,
        units=units, kpc_per_arcsec=kpc_per_arcsec, figsize=figsize, aspect=aspect,
        cmap=cmap, norm=norm, norm_min=norm_min, norm_max=norm_max, linthresh=linthresh, linscale=linscale,
        cb_ticksize=cb_ticksize, cb_fraction=cb_fraction, cb_pad=cb_pad, 
        cb_tick_values=cb_tick_values, cb_tick_labels=cb_tick_labels,
        titlesize=titlesize, xlabelsize=xlabelsize, ylabelsize=ylabelsize, xyticksize=xyticksize,
        position_pointsize=position_pointsize, mask_pointsize=mask_pointsize,
        output_path=output_path, output_filename='', output_format=output_format)

    plt.subplot(rows, columns, 4)

    lens_plotter_util.plot_model_data(
        fit=fit, mask=mask, extract_array_from_mask=extract_array_from_mask, zoom_around_mask=zoom_around_mask, as_subplot=True,
        units=units, kpc_per_arcsec=kpc_per_arcsec, figsize=figsize, aspect=aspect,
        cmap=cmap, norm=norm, norm_min=norm_min, norm_max=norm_max, linthresh=linthresh, linscale=linscale,
        cb_ticksize=cb_ticksize, cb_fraction=cb_fraction, cb_pad=cb_pad, 
        cb_tick_values=cb_tick_values, cb_tick_labels=cb_tick_labels,
        titlesize=titlesize, xlabelsize=xlabelsize, ylabelsize=ylabelsize, xyticksize=xyticksize,
        output_path=output_path, output_filename='', output_format=output_format)

    plt.subplot(rows, columns, 5)

    lens_plotter_util.plot_residual_map(
        fit=fit, mask=mask, extract_array_from_mask=extract_array_from_mask, zoom_around_mask=zoom_around_mask, as_subplot=True,
        units=units, kpc_per_arcsec=kpc_per_arcsec, figsize=figsize, aspect=aspect,
        cmap=cmap, norm=norm, norm_min=norm_min, norm_max=norm_max, linthresh=linthresh, linscale=linscale,
        cb_ticksize=cb_ticksize, cb_fraction=cb_fraction, cb_pad=cb_pad, 
        cb_tick_values=cb_tick_values, cb_tick_labels=cb_tick_labels,
        titlesize=titlesize, xlabelsize=xlabelsize, ylabelsize=ylabelsize, xyticksize=xyticksize,
        output_path=output_path, output_filename='', output_format=output_format)

    plt.subplot(rows, columns, 6)

    lens_plotter_util.plot_chi_squared_map(
        fit=fit, mask=mask, extract_array_from_mask=extract_array_from_mask, zoom_around_mask=zoom_around_mask, as_subplot=True,
        units=units, kpc_per_arcsec=kpc_per_arcsec, figsize=figsize, aspect=aspect,
        cmap=cmap, norm=norm, norm_min=norm_min, norm_max=norm_max, linthresh=linthresh, linscale=linscale,
        cb_ticksize=cb_ticksize, cb_fraction=cb_fraction, cb_pad=cb_pad, 
        cb_tick_values=cb_tick_values, cb_tick_labels=cb_tick_labels,
        titlesize=titlesize, xlabelsize=xlabelsize, ylabelsize=ylabelsize, xyticksize=xyticksize,
        output_path=output_path, output_filename='', output_format=output_format)

    plotter_util.output_subplot_array(output_path=output_path, output_filename=output_filename,
                                      output_format=output_format)

    plt.close()

def plot_fit_subplot_lens_and_source_planes(
        fit, should_plot_mask=True, extract_array_from_mask=False, zoom_around_mask=False,
        should_plot_source_grid=False, positions=None, should_plot_image_plane_pix=False, plot_mass_profile_centres=True,
        units='arcsec', figsize=None, aspect='square',
        cmap='jet', norm='linear', norm_min=None, norm_max=None, linthresh=0.05, linscale=0.01,
        cb_ticksize=10, cb_fraction=0.047, cb_pad=0.01, cb_tick_values=None, cb_tick_labels=None,
        titlesize=10, xlabelsize=10, ylabelsize=10, xyticksize=10,
        mask_pointsize=10, position_pointsize=10, grid_pointsize=1,
        output_path=None, output_filename='lens_fit', output_format='show'):
    """Plot the model datas_ of an analysis, using the *Fitter* class object.

    The visualization and output type can be fully customized.

    Parameters
    -----------
    fit : autolens.lens.fitting.Fitter
        Class containing fit between the model datas_ and observed lens datas_ (including residual_map, chi_squared_map etc.)
    output_path : str
        The path where the datas_ is output if the output_type is a file format (e.g. png, fits)
    output_filename : str
        The name of the file that is output, if the output_type is a file format (e.g. png, fits)
    output_format : str
        How the datas_ is output. File formats (e.g. png, fits) output the datas_ to harddisk. 'show' displays the datas_ \
        in the python interpreter window.
    """

    rows, columns, figsize_tool = plotter_util.get_subplot_rows_columns_figsize(number_subplots=9)

    mask = lens_plotter_util.get_mask(fit=fit, should_plot_mask=should_plot_mask)

    if figsize is None:
        figsize = figsize_tool

    plt.figure(figsize=figsize)

    kpc_per_arcsec = fit.tracer.image_plane.kpc_per_arcsec

    image_plane_pix_grid = lens_plotter_util.get_image_plane_pix_grid(should_plot_image_plane_pix, fit)

    plt.subplot(rows, columns, 1)

    lens_plotter_util.plot_image(
        fit=fit, mask=mask, extract_array_from_mask=extract_array_from_mask, zoom_around_mask=zoom_around_mask, positions=positions,
        image_plane_pix_grid=image_plane_pix_grid, as_subplot=True,
        units=units, kpc_per_arcsec=kpc_per_arcsec, figsize=figsize, aspect=aspect,
        cmap=cmap, norm=norm, norm_min=norm_min, norm_max=norm_max, linthresh=linthresh, linscale=linscale,
        cb_ticksize=cb_ticksize, cb_fraction=cb_fraction, cb_pad=cb_pad, 
        cb_tick_values=cb_tick_values, cb_tick_labels=cb_tick_labels,
        titlesize=titlesize, xlabelsize=xlabelsize, ylabelsize=ylabelsize, xyticksize=xyticksize,
        grid_pointsize=grid_pointsize, position_pointsize=position_pointsize, mask_pointsize=mask_pointsize,
        output_path=output_path, output_filename='', output_format=output_format)

    plt.subplot(rows, columns, 2)

    lens_plotter_util.plot_noise_map(
        fit=fit, mask=mask, extract_array_from_mask=extract_array_from_mask, zoom_around_mask=zoom_around_mask, positions=None, as_subplot=True,
        units=units, kpc_per_arcsec=kpc_per_arcsec, figsize=figsize, aspect=aspect,
        cmap=cmap, norm=norm, norm_min=norm_min, norm_max=norm_max, linthresh=linthresh, linscale=linscale,
        cb_ticksize=cb_ticksize, cb_fraction=cb_fraction, cb_pad=cb_pad, 
        cb_tick_values=cb_tick_values, cb_tick_labels=cb_tick_labels,
        titlesize=titlesize, xlabelsize=xlabelsize, ylabelsize=ylabelsize, xyticksize=xyticksize,
        position_pointsize=position_pointsize, mask_pointsize=mask_pointsize,
        output_path=output_path, output_filename='', output_format=output_format)

    plt.subplot(rows, columns, 3)

    lens_plotter_util.plot_signal_to_noise_map(
        fit=fit, mask=mask, extract_array_from_mask=extract_array_from_mask, zoom_around_mask=zoom_around_mask, positions=None, as_subplot=True,
        units=units, kpc_per_arcsec=kpc_per_arcsec, figsize=figsize, aspect=aspect,
        cmap=cmap, norm=norm, norm_min=norm_min, norm_max=norm_max, linthresh=linthresh, linscale=linscale,
        cb_ticksize=cb_ticksize, cb_fraction=cb_fraction, cb_pad=cb_pad, 
        cb_tick_values=cb_tick_values, cb_tick_labels=cb_tick_labels,
        titlesize=titlesize, xlabelsize=xlabelsize, ylabelsize=ylabelsize, xyticksize=xyticksize,
        position_pointsize=position_pointsize, mask_pointsize=mask_pointsize,
        output_path=output_path, output_filename='', output_format=output_format)

    plt.subplot(rows, columns, 4)

    lens_plotter_util.plot_lens_subtracted_image(
        fit=fit, mask=mask, extract_array_from_mask=extract_array_from_mask, zoom_around_mask=zoom_around_mask, positions=positions, as_subplot=True,
        units=units, kpc_per_arcsec=kpc_per_arcsec, figsize=figsize, aspect=aspect,
        cmap=cmap, norm=norm, norm_min=norm_min, norm_max=norm_max, linthresh=linthresh, linscale=linscale,
        cb_ticksize=cb_ticksize, cb_fraction=cb_fraction, cb_pad=cb_pad, 
        cb_tick_values=cb_tick_values, cb_tick_labels=cb_tick_labels,
        title='Fit Lens Subtracted Image', titlesize=titlesize, xlabelsize=xlabelsize, ylabelsize=ylabelsize,
        position_pointsize=position_pointsize, xyticksize=xyticksize,
        output_path=output_path, output_filename='', output_format=output_format)

    if fit.tracer.image_plane.has_light_profile:

        plt.subplot(rows, columns, 5)

        lens_plotter_util.plot_model_image_of_planes(
            fit=fit, plot_foreground=True, mask=mask, extract_array_from_mask=extract_array_from_mask,
            zoom_around_mask=zoom_around_mask, plot_mass_profile_centres=plot_mass_profile_centres, as_subplot=True,
            units=units, kpc_per_arcsec=kpc_per_arcsec, figsize=figsize, aspect=aspect,
            cmap=cmap, norm=norm, norm_min=norm_min, norm_max=norm_max, linthresh=linthresh, linscale=linscale,
            cb_ticksize=cb_ticksize, cb_fraction=cb_fraction, cb_pad=cb_pad, 
        cb_tick_values=cb_tick_values, cb_tick_labels=cb_tick_labels,
            title='Fit Image-Plane Model Image', titlesize=titlesize, xlabelsize=xlabelsize, ylabelsize=ylabelsize,
            xyticksize=xyticksize,
            output_path=output_path, output_filename='', output_format=output_format)

    plt.subplot(rows, columns, 6)

    lens_plotter_util.plot_model_image_of_planes(
        fit=fit, plot_source=True, mask=mask, extract_array_from_mask=extract_array_from_mask,
        zoom_around_mask=zoom_around_mask, plot_mass_profile_centres=plot_mass_profile_centres, as_subplot=True,
        units=units, kpc_per_arcsec=kpc_per_arcsec, figsize=figsize, aspect=aspect,
        cmap=cmap, norm=norm, norm_min=norm_min, norm_max=norm_max, linthresh=linthresh, linscale=linscale,
        cb_ticksize=cb_ticksize, cb_fraction=cb_fraction, cb_pad=cb_pad, 
        cb_tick_values=cb_tick_values, cb_tick_labels=cb_tick_labels,
        title='Fit Source-Plane Model Image', titlesize=titlesize, xlabelsize=xlabelsize, ylabelsize=ylabelsize,
        xyticksize=xyticksize,
        output_path=output_path, output_filename='lens_subtracted_image', output_format=output_format)

    if fit.total_inversions == 0:

        plt.subplot(rows, columns, 7)

        plane_plotters.plot_plane_image(
            plane=fit.tracer.source_plane, positions=None, plot_grid=should_plot_source_grid, as_subplot=True,
            units=units, figsize=figsize, aspect=aspect,
            cmap=cmap, norm=norm, norm_min=norm_min, norm_max=norm_max, linthresh=linthresh, linscale=linscale,
            cb_ticksize=cb_ticksize, cb_fraction=cb_fraction, cb_pad=cb_pad,
            cb_tick_values=cb_tick_values, cb_tick_labels=cb_tick_labels,
            titlesize=titlesize, xlabelsize=xlabelsize, ylabelsize=ylabelsize, xyticksize=xyticksize,
            grid_pointsize=grid_pointsize, position_pointsize=position_pointsize,
            output_path=output_path, output_filename='', output_format=output_format)

    elif fit.total_inversions == 1:
        
        ratio = float((fit.inversion.mapper.geometry.arc_second_maxima[1] - fit.inversion.mapper.geometry.arc_second_minima[1]) / \
                (fit.inversion.mapper.geometry.arc_second_maxima[0] - fit.inversion.mapper.geometry.arc_second_minima[0]))

        if aspect is 'square':
            aspect_inv = ratio
        elif aspect is 'auto':
            aspect_inv = 1.0 / ratio
        elif aspect is 'equal':
            aspect_inv = 1.0

        plt.subplot(rows, columns, 7, aspect=float(aspect_inv))

        inversion_plotters.plot_reconstructed_pixelization(
            inversion=fit.inversion, positions=None, should_plot_grid=False, should_plot_centres=False, as_subplot=True,
            units=units, kpc_per_arcsec=kpc_per_arcsec, figsize=figsize, aspect=None,
            cmap=cmap, norm=norm, norm_min=norm_min, norm_max=norm_max, linthresh=linthresh, linscale=linscale,
            cb_ticksize=cb_ticksize, cb_fraction=cb_fraction, cb_pad=cb_pad,
        cb_tick_values=cb_tick_values, cb_tick_labels=cb_tick_labels,
            titlesize=titlesize, xlabelsize=xlabelsize, ylabelsize=ylabelsize, xyticksize=xyticksize,
            output_path=output_path, output_filename=None, output_format=output_format)

    plt.subplot(rows, columns, 8)

    lens_plotter_util.plot_residual_map(
        fit=fit, mask=mask, extract_array_from_mask=extract_array_from_mask, zoom_around_mask=zoom_around_mask, as_subplot=True,
        units=units, kpc_per_arcsec=kpc_per_arcsec, figsize=figsize, aspect=aspect,
        cmap=cmap, norm=norm, norm_min=norm_min, norm_max=norm_max, linthresh=linthresh, linscale=linscale,
        cb_ticksize=cb_ticksize, cb_fraction=cb_fraction, cb_pad=cb_pad,
        cb_tick_values=cb_tick_values, cb_tick_labels=cb_tick_labels,
        titlesize=titlesize, xlabelsize=xlabelsize, ylabelsize=ylabelsize, xyticksize=xyticksize,
        output_path=output_path, output_filename='', output_format=output_format)

    plt.subplot(rows, columns, 9)

    lens_plotter_util.plot_chi_squared_map(
        fit=fit, mask=mask, extract_array_from_mask=extract_array_from_mask, zoom_around_mask=zoom_around_mask, as_subplot=True,
        units=units, kpc_per_arcsec=kpc_per_arcsec, figsize=figsize, aspect=aspect,
        cmap=cmap, norm=norm, norm_min=norm_min, norm_max=norm_max, linthresh=linthresh, linscale=linscale,
        cb_ticksize=cb_ticksize, cb_fraction=cb_fraction, cb_pad=cb_pad,
        cb_tick_values=cb_tick_values, cb_tick_labels=cb_tick_labels,
        titlesize=titlesize, xlabelsize=xlabelsize, ylabelsize=ylabelsize, xyticksize=xyticksize,
        output_path=output_path, output_filename='', output_format=output_format)

    plotter_util.output_subplot_array(output_path=output_path, output_filename=output_filename,
                                      output_format=output_format)

    plt.close()

def plot_fit_individuals(
        fit, should_plot_mask=True, extract_array_from_mask=False, zoom_around_mask=False, positions=None,
        should_plot_image_plane_pix=False,
        should_plot_image=False,
        should_plot_noise_map=False,
        should_plot_signal_to_noise_map=False,
        should_plot_lens_subtracted_image=False,
        should_plot_model_image=False,
        should_plot_lens_model_image=False,
        should_plot_source_model_image=False,
        should_plot_source_plane_image=False,
        should_plot_residual_map=False,
        should_plot_chi_squared_map=False,
        should_plot_regularization_weights=False,
        units='arcsec',
        output_path=None, output_format='show'):

    if fit.tracer.total_planes == 1:

        plot_fit_individuals_lens_plane_only(
            fit=fit,
            should_plot_mask=should_plot_mask, extract_array_from_mask=extract_array_from_mask,
            zoom_around_mask=zoom_around_mask, positions=positions,
            should_plot_image_plane_pix=should_plot_image_plane_pix,
            should_plot_image=should_plot_image,
            should_plot_noise_map=should_plot_noise_map,
            should_plot_signal_to_noise_map=should_plot_signal_to_noise_map,
            should_plot_model_image=should_plot_model_image,
            should_plot_residual_map=should_plot_residual_map,
            should_plot_chi_squared_map=should_plot_chi_squared_map,
            units=units,
            output_path=output_path, output_format=output_format)

    elif fit.tracer.total_planes == 2:

        plot_fit_individuals_lens_and_source_planes(
            fit=fit,
            should_plot_mask=should_plot_mask, extract_array_from_mask=extract_array_from_mask,
            zoom_around_mask=zoom_around_mask, positions=positions,
            should_plot_image_plane_pix=should_plot_image_plane_pix,
            should_plot_image=should_plot_image,
            should_plot_noise_map=should_plot_noise_map,
            should_plot_signal_to_noise_map=should_plot_signal_to_noise_map,
            should_plot_lens_subtracted_image=should_plot_lens_subtracted_image,
            should_plot_model_image=should_plot_model_image,
            should_plot_lens_model_image=should_plot_lens_model_image,
            should_plot_source_model_image=should_plot_source_model_image,
            should_plot_source_plane_image=should_plot_source_plane_image,
            should_plot_residual_map=should_plot_residual_map,
            should_plot_chi_squared_map=should_plot_chi_squared_map,
            should_plot_regularization_weights=should_plot_regularization_weights,
            units=units,
            output_path=output_path, output_format=output_format)

def plot_fit_individuals_lens_plane_only(
        fit, should_plot_mask=True, extract_array_from_mask=False, zoom_around_mask=False, positions=None,
        should_plot_image_plane_pix=False,
        should_plot_image=False,
        should_plot_noise_map=False,
        should_plot_signal_to_noise_map=False,
        should_plot_model_image=False,
        should_plot_residual_map=False,
        should_plot_chi_squared_map=False,
        units='arcsec',
        output_path=None, output_format='show'):
    """Plot the model datas_ of an analysis, using the *Fitter* class object.

    The visualization and output type can be fully customized.

    Parameters
    -----------
    fit : autolens.lens.fitting.Fitter
        Class containing fit between the model datas_ and observed lens datas_ (including residual_map, chi_squared_map etc.)
    output_path : str
        The path where the datas_ is output if the output_type is a file format (e.g. png, fits)
    output_format : str
        How the datas_ is output. File formats (e.g. png, fits) output the datas_ to harddisk. 'show' displays the datas_ \
        in the python interpreter window.
    """

    mask = lens_plotter_util.get_mask(fit=fit, should_plot_mask=should_plot_mask)

    kpc_per_arcsec = fit.tracer.image_plane.kpc_per_arcsec

    if should_plot_image:

        image_plane_pix_grid = lens_plotter_util.get_image_plane_pix_grid(should_plot_image_plane_pix, fit)

        lens_plotter_util.plot_image(
            fit=fit, mask=mask, extract_array_from_mask=extract_array_from_mask, zoom_around_mask=zoom_around_mask,
            image_plane_pix_grid=image_plane_pix_grid,
            units=units, kpc_per_arcsec=kpc_per_arcsec,
            output_path=output_path, output_format=output_format)

    if should_plot_noise_map:

        lens_plotter_util.plot_noise_map(
            fit=fit, mask=mask, extract_array_from_mask=extract_array_from_mask, zoom_around_mask=zoom_around_mask,
            units=units, kpc_per_arcsec=kpc_per_arcsec,
            output_path=output_path, output_format=output_format)

    if should_plot_signal_to_noise_map:

        lens_plotter_util.plot_signal_to_noise_map(
            fit=fit, mask=mask, extract_array_from_mask=extract_array_from_mask, zoom_around_mask=zoom_around_mask,
            units=units, kpc_per_arcsec=kpc_per_arcsec,
            output_path=output_path, output_format=output_format)

    if should_plot_model_image:

        lens_plotter_util.plot_model_data(
            fit=fit, mask=mask, extract_array_from_mask=extract_array_from_mask, zoom_around_mask=zoom_around_mask, positions=positions,
            units=units, kpc_per_arcsec=kpc_per_arcsec,
            output_path=output_path, output_format=output_format)

    if should_plot_residual_map:

        lens_plotter_util.plot_residual_map(
            fit=fit, mask=mask, extract_array_from_mask=extract_array_from_mask, zoom_around_mask=zoom_around_mask,
            units=units, kpc_per_arcsec=kpc_per_arcsec,
            output_path=output_path, output_format=output_format)

    if should_plot_chi_squared_map:

        lens_plotter_util.plot_chi_squared_map(
            fit=fit, mask=mask, extract_array_from_mask=extract_array_from_mask, zoom_around_mask=zoom_around_mask,
            units=units, kpc_per_arcsec=kpc_per_arcsec,
            output_path=output_path, output_format=output_format)

def plot_fit_individuals_lens_and_source_planes(
        fit, should_plot_mask=True, extract_array_from_mask=False, zoom_around_mask=False, positions=None,
        should_plot_image_plane_pix=False,
        should_plot_image=False,
        should_plot_noise_map=False,
        should_plot_signal_to_noise_map=False,
        should_plot_lens_subtracted_image=False,
        should_plot_model_image=False,
        should_plot_lens_model_image=False,
        should_plot_source_model_image=False,
        should_plot_source_plane_image=False,
        should_plot_residual_map=False,
        should_plot_chi_squared_map=False,
        should_plot_regularization_weights=False,
        units='arcsec',
        output_path=None, output_format='show'):
    """Plot the model datas_ of an analysis, using the *Fitter* class object.

    The visualization and output type can be fully customized.

    Parameters
    -----------
    fit : autolens.lens.fitting.Fitter
        Class containing fit between the model datas_ and observed lens datas_ (including residual_map, chi_squared_map etc.)
    output_path : str
        The path where the datas_ is output if the output_type is a file format (e.g. png, fits)
    output_format : str
        How the datas_ is output. File formats (e.g. png, fits) output the datas_ to harddisk. 'show' displays the datas_ \
        in the python interpreter window.
    """

    mask = lens_plotter_util.get_mask(fit=fit, should_plot_mask=should_plot_mask)

    kpc_per_arcsec = fit.tracer.image_plane.kpc_per_arcsec

    if should_plot_image:

        image_plane_pix_grid = lens_plotter_util.get_image_plane_pix_grid(should_plot_image_plane_pix, fit)

        lens_plotter_util.plot_image(
            fit=fit, mask=mask, extract_array_from_mask=extract_array_from_mask, zoom_around_mask=zoom_around_mask,
            image_plane_pix_grid=image_plane_pix_grid,
            units=units, kpc_per_arcsec=kpc_per_arcsec,
            output_path=output_path, output_format=output_format)

    if should_plot_noise_map:

        lens_plotter_util.plot_noise_map(
            fit=fit, mask=mask, extract_array_from_mask=extract_array_from_mask, zoom_around_mask=zoom_around_mask,
            units=units, kpc_per_arcsec=kpc_per_arcsec,
            output_path=output_path, output_format=output_format)

    if should_plot_signal_to_noise_map:

        lens_plotter_util.plot_signal_to_noise_map(
            fit=fit, mask=mask, extract_array_from_mask=extract_array_from_mask, zoom_around_mask=zoom_around_mask,
            units=units, kpc_per_arcsec=kpc_per_arcsec,
            output_path=output_path, output_format=output_format)

    if should_plot_lens_subtracted_image:

        lens_plotter_util.plot_lens_subtracted_image(
            fit=fit, mask=mask, positions=positions, extract_array_from_mask=extract_array_from_mask,
            zoom_around_mask=zoom_around_mask,
            units=units, kpc_per_arcsec=kpc_per_arcsec,
            output_path=output_path, output_format=output_format)

    if should_plot_model_image:
        lens_plotter_util.plot_model_data(
            fit=fit, mask=mask, extract_array_from_mask=extract_array_from_mask, zoom_around_mask=zoom_around_mask,
            units=units, kpc_per_arcsec=kpc_per_arcsec,
            output_path=output_path, output_format=output_format)

    if should_plot_lens_model_image:

        lens_plotter_util.plot_model_image_of_planes(
            fit=fit, mask=mask, extract_array_from_mask=extract_array_from_mask, zoom_around_mask=zoom_around_mask,
            plot_foreground=True,
            units=units, kpc_per_arcsec=kpc_per_arcsec,
            output_path=output_path, output_filename='fit_lens_plane_model_image', output_format=output_format)

    if should_plot_source_model_image:

        lens_plotter_util.plot_model_image_of_planes(
            fit=fit, mask=mask, extract_array_from_mask=extract_array_from_mask, zoom_around_mask=zoom_around_mask,
            plot_source=True,
            units=units, kpc_per_arcsec=kpc_per_arcsec,
            output_path=output_path, output_filename='fit_source_plane_model_image', output_format=output_format)

    if should_plot_source_plane_image:

        if fit.total_inversions == 0:

           plane_plotters.plot_plane_image(
               plane=fit.tracer.source_plane, plot_grid=True,
               units=units, figsize=(20, 20),
               output_path=output_path, output_filename='fit_source_plane', output_format=output_format)

        elif fit.total_inversions == 1:

            inversion_plotters.plot_reconstructed_pixelization(
                inversion=fit.inversion, should_plot_grid=True,
                units=units, figsize=(20, 20),
                output_path=output_path, output_filename='fit_source_plane', output_format=output_format)
    if should_plot_residual_map:

        lens_plotter_util.plot_residual_map(
            fit=fit, mask=mask, extract_array_from_mask=extract_array_from_mask, zoom_around_mask=zoom_around_mask,
            units=units, kpc_per_arcsec=kpc_per_arcsec,
            output_path=output_path, output_format=output_format)

    if should_plot_chi_squared_map:

        lens_plotter_util.plot_chi_squared_map(
            fit=fit, mask=mask, extract_array_from_mask=extract_array_from_mask, zoom_around_mask=zoom_around_mask,
            units=units, kpc_per_arcsec=kpc_per_arcsec,
            output_path=output_path, output_format=output_format)

    if should_plot_regularization_weights:

        if fit.total_inversions == 1:

            inversion_plotters.plot_regularization_weights(
                inversion=fit.inversion, should_plot_grid=True,
                units=units, figsize=(20, 20),
                output_path=output_path, output_filename='fit_regularization_weights', output_format=output_format)