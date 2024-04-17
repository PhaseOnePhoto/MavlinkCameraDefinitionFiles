
"""
MIT License Copyright (c) 2022 Phase One A/S

Contributors:
 - David Wuthier (dwu@phaseone.com)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is furnished
to do so, subject to the following conditions:

The above copyright notice and this permission notice (including the next
paragraph) shall be included in all copies or substantial portions of the
Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS
OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF
OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""


from xml.etree import ElementTree
from utilities import *


def main():
    version = '31'

    build_ixm_50(version)
    build_ixm_100(version)
    build_ixm_100_achromatic(version)
    build_ixm_gs120(version)
    build_p5_gs128('32')

def build_ixm_50(version='26', model='iXM-50', vendor='PhaseOne'):
    template = get_template('template.xml')

    set_attribute(template, './definition', 'version', version)

    set_text(template, './definition/model', model)
    set_text(template, './definition/vendor', vendor)

    options_iso = get_options('options_iso.xml')

    limit_options(options_iso, 100, 6400)

    copy_options(template, 'CAM_ISO', options_iso)
    copy_options(template, 'AE_ISO_MIN', options_iso)
    copy_options(template, 'AE_ISO_MAX', options_iso)

    options_aperture = get_options('options_aperture.xml')

    copy_options(template, 'CAM_APERTURE', options_aperture)
    copy_options(template, 'AE_APERTURE_MIN', options_aperture)
    copy_options(template, 'AE_APERTURE_MAX', options_aperture)

    options_shutter_speed = get_options('options_shutter_speed.xml')

    limit_options(options_shutter_speed, -1000, 2500)

    copy_options(template, 'CAM_SHUTTERSPD', options_shutter_speed)
    copy_options(template, 'AE_SH_SPD_MIN', options_shutter_speed)
    copy_options(template, 'AE_SH_SPD_MAX', options_shutter_speed)

    exposure_value = get_options('options_exposure_value.xml')

    copy_options(template, 'CAM_EV', exposure_value)

    remove_option(template, 'CAPTURE_MODE', 'Burst Mode')

    write_file(template, version, model, vendor)

def build_ixm_100(version='26', model='iXM-100', vendor='PhaseOne'):
    template = get_template('template.xml')

    set_attribute(template, './definition', 'version', version)

    set_text(template, './definition/model', model)
    set_text(template, './definition/vendor', vendor)

    options_iso = get_options('options_iso.xml')

    limit_options(options_iso, 50, 6400)

    copy_options(template, 'CAM_ISO', options_iso)
    copy_options(template, 'AE_ISO_MIN', options_iso)
    copy_options(template, 'AE_ISO_MAX', options_iso)

    options_aperture = get_options('options_aperture.xml')

    copy_options(template, 'CAM_APERTURE', options_aperture)
    copy_options(template, 'AE_APERTURE_MIN', options_aperture)
    copy_options(template, 'AE_APERTURE_MAX', options_aperture)

    options_shutter_speed = get_options('options_shutter_speed.xml')

    limit_options(options_shutter_speed, -1000, 2500)

    copy_options(template, 'CAM_SHUTTERSPD', options_shutter_speed)
    copy_options(template, 'AE_SH_SPD_MIN', options_shutter_speed)
    copy_options(template, 'AE_SH_SPD_MAX', options_shutter_speed)

    exposure_value = get_options('options_exposure_value.xml')

    copy_options(template, 'CAM_EV', exposure_value)

    remove_option(template, 'CAPTURE_MODE', 'Burst Mode')

    write_file(template, version, model, vendor)

def build_ixm_100_achromatic(version='26', model='iXM-100_Achromatic', vendor='PhaseOne'):
    template = get_template('template.xml')

    set_attribute(template, './definition', 'version', version)

    set_text(template, './definition/model', model)
    set_text(template, './definition/vendor', vendor)

    options_iso = get_options('options_iso.xml')

    limit_options(options_iso, 200, 25600)

    copy_options(template, 'CAM_ISO', options_iso)
    copy_options(template, 'AE_ISO_MIN', options_iso)
    copy_options(template, 'AE_ISO_MAX', options_iso)

    options_aperture = get_options('options_aperture.xml')

    copy_options(template, 'CAM_APERTURE', options_aperture)
    copy_options(template, 'AE_APERTURE_MIN', options_aperture)
    copy_options(template, 'AE_APERTURE_MAX', options_aperture)

    options_shutter_speed = get_options('options_shutter_speed.xml')

    limit_options(options_shutter_speed, -1000, 2500)

    copy_options(template, 'CAM_SHUTTERSPD', options_shutter_speed)
    copy_options(template, 'AE_SH_SPD_MIN', options_shutter_speed)
    copy_options(template, 'AE_SH_SPD_MAX', options_shutter_speed)

    exposure_value = get_options('options_exposure_value.xml')

    copy_options(template, 'CAM_EV', exposure_value)

    remove_option(template, 'CAPTURE_MODE', 'Burst Mode')

    write_file(template, version, model, vendor)

def build_ixm_gs120(version='26', model='iXM-GS120', vendor='PhaseOne'):
    template = get_template('template.xml')

    set_attribute(template, './definition', 'version', version)

    set_text(template, './definition/model', model)
    set_text(template, './definition/vendor', vendor)

    options_iso = get_options('options_iso.xml')

    limit_options(options_iso, 200, 6400)

    copy_options(template, 'CAM_ISO', options_iso)
    copy_options(template, 'AE_ISO_MIN', options_iso)
    copy_options(template, 'AE_ISO_MAX', options_iso)

    options_aperture = get_options('options_aperture.xml')

    copy_options(template, 'CAM_APERTURE', options_aperture)
    copy_options(template, 'AE_APERTURE_MIN', options_aperture)
    copy_options(template, 'AE_APERTURE_MAX', options_aperture)

    options_shutter_speed = get_options('options_shutter_speed.xml')

    limit_options(options_shutter_speed, -1000, 16000)

    copy_options(template, 'CAM_SHUTTERSPD', options_shutter_speed)
    copy_options(template, 'AE_SH_SPD_MIN', options_shutter_speed)
    copy_options(template, 'AE_SH_SPD_MAX', options_shutter_speed)

    exposure_value = get_options('options_exposure_value.xml')

    copy_options(template, 'CAM_EV', exposure_value)

    remove_exclude(template, 'CAM_EXPMODE', 'Manual', 'SHUTTER_MODE')
    remove_exclude(template, 'CAM_EXPMODE', 'Auto', 'SHUTTER_MODE')

    write_file(template, version, model, vendor)

def build_p5_gs128(version='01', model='P5-GS128', vendor='PhaseOne'):
    template = get_template('template.xml')

    set_attribute(template, './definition', 'version', version)

    set_text(template, './definition/model', model)
    set_text(template, './definition/vendor', vendor)

    options_iso = get_options('options_iso.xml')

    limit_options(options_iso, 200, 6400)

    copy_options(template, 'CAM_ISO', options_iso)
    copy_options(template, 'AE_ISO_MIN', options_iso)
    copy_options(template, 'AE_ISO_MAX', options_iso)

    options_aperture = get_options('options_aperture.xml')

    copy_options(template, 'CAM_APERTURE', options_aperture)
    copy_options(template, 'AE_APERTURE_MIN', options_aperture)
    copy_options(template, 'AE_APERTURE_MAX', options_aperture)

    options_shutter_speed = get_options('options_shutter_speed.xml')

    limit_options(options_shutter_speed, -1000, 16000)

    copy_options(template, 'CAM_SHUTTERSPD', options_shutter_speed)
    copy_options(template, 'AE_SH_SPD_MIN', options_shutter_speed)
    copy_options(template, 'AE_SH_SPD_MAX', options_shutter_speed)

    exposure_value = get_options('options_exposure_value.xml')

    copy_options(template, 'CAM_EV', exposure_value)

    remove_exclude(template, 'CAM_EXPMODE', 'Manual', 'SHUTTER_MODE')
    remove_exclude(template, 'CAM_EXPMODE', 'Auto', 'SHUTTER_MODE')
    remove_parameter(template, 'SHUTTER_MODE')

    remove_parameter(template, 'FOCUS_MODE')
    remove_parameter(template, 'FOCUS_DIST')
    remove_parameter(template, 'AF_MIN_DIST')
    remove_parameter(template, 'AF_MAX_DIST')
    remove_parameter(template, 'AF_STRATEGY')
    remove_parameter(template, 'AF_STRATEGY_THR')
    
    remove_option(template, 'CAPTURE_MODE', 'Manual Focus Bracketing')
    remove_option(template, 'CAPTURE_MODE', 'Automatic Focus Bracketing')
    remove_option(template, 'CAPTURE_MODE', 'Laser')
    remove_option(template, 'CAPTURE_MODE', 'Timed Laser')
    remove_option(template, 'CAPTURE_MODE', 'Burst Mode')
    
    remove_parameter(template, 'FOCUS_BKT_MODE')
    remove_parameter(template, 'FOCUS_BKT_CNT')
    remove_parameter(template, 'FOCUS_BKT_STEP')
    remove_parameter(template, 'FOCUS_BKT_COC')
    remove_parameter(template, 'FOCUS_BKT_OVRLP')
    remove_parameter(template, 'FOCUS_BKT_DEPTH')
    remove_parameter(template, 'LASER_CAP_CNT')
    remove_parameter(template, 'LASER_CORR')
    remove_parameter(template, 'HDMI_LV')
    remove_parameter(template, 'HDMI_LV_ZOOM')
    remove_parameter(template, 'HDMI_OVERLAY')
    
    remove_parameter(template, 'OVERLAY_TRANSP')
    remove_parameter(template, 'FOCUS_POINT')
    remove_parameter(template, 'OVERLAY_PREVIEW')
    remove_parameter(template, 'PREVIEW_TIME')
    remove_parameter(template, 'FOCUS_MASK')
    remove_parameter(template, 'FOCUS_MASK_THR')
    remove_parameter(template, 'MASS_STORAGE')  
    
    remove_parameter(template, 'CAM_ORIENT')
    remove_parameter(template, 'GMB_CMD')
    
    write_file(template, version, model, vendor)


if __name__ == '__main__':
    main()
