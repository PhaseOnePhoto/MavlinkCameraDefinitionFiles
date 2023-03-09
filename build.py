
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
    version = '26'

    build_ixm_50(version)
    build_ixm_100(version)
    build_ixm_100_achromatic(version)
    build_ixm_gs120(version)

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

    limit_options(options_shutter_speed, 0.0004, 1.0)

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

    limit_options(options_shutter_speed, 0.0004, 1.0)

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

    limit_options(options_shutter_speed, 0.0004, 1.0)

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

    limit_options(options_shutter_speed, 0.0000625, 1.0)

    copy_options(template, 'CAM_SHUTTERSPD', options_shutter_speed)
    copy_options(template, 'AE_SH_SPD_MIN', options_shutter_speed)
    copy_options(template, 'AE_SH_SPD_MAX', options_shutter_speed)

    exposure_value = get_options('options_exposure_value.xml')

    copy_options(template, 'CAM_EV', exposure_value)

    write_file(template, version, model, vendor)

if __name__ == '__main__':
    main()
