

from xml.etree.ElementTree import Element, ElementTree, indent


def add(e : Element, name, disp, desc, val, rng, inc, ro, user):
    e.append(Element(name))

    se = e.find(f'./{name}')

    _add(se, 'DisplayName', disp)
    _add(se, 'Description', disp if desc is None else desc)
    _add(se, 'Values', val)
    _add(se, 'Range', rng)
    _add(se, 'Increment', inc)
    _add(se, 'ReadOnly', ro)
    _add(se, 'User', user)

def _add(e : Element, tag, text):
    if text is not None:
        se = Element(tag)
        se.text = text
        e.append(se)

def fix(e, lf=False):
    if e is None:
        e = Element('')
        e.text = 'None'
    elif lf:
        e.text = f'"""{e.text}"""'
    else:
        e.text = f'"{e.text}"'
    
    return e

def get_tree():
    t = ElementTree(file='ParameterMetaData.xml')

    for e in t.find('./ArduCopter2'):
        eDisp = fix(e.find('./DisplayName'))
        eDesc = fix(e.find('./Description'))
        eVal = fix(e.find('./Values'), lf=True)
        eRange = fix(e.find('./Range'))
        eInc = fix(e.find('./Increment'))
        eRo = fix(e.find('./ReadOnly'))
        eUser = fix(e.find('./User'))

        if eDisp.text == eDesc.text:
            eDesc.text = 'None'

        print( f'add(e, \nname="{e.tag}",\ndisp={eDisp.text},\ndesc={eDesc.text},\nval={eVal.text},\nrng={eRange.text},\ninc={eInc.text},\nro={eRo.text},\nuser={eUser.text})\n')

def begin():
    r = Element('Params')
    r.append(Element('ArduCopter2'))
    e = r[0]

    return e, r

def end(r):
    t = ElementTree(r)

    indent(t, '  ')

    t.write('ParameterMetaData.xml', encoding='utf-8', xml_declaration=True)

# get_tree()

e, r = begin()

add(e, 
name="CAM_EXPMODE",
disp="Exposure Mode",
desc=None,
val="""0:Manual,
1:Auto""",
rng=None,
inc=None,
ro=None,
user="Standard")

val_iso="""50:ISO 50,
64: ISO 64,
80: ISO 80,
100: ISO 100,
125: ISO 125,
160: ISO 160,
200: ISO 200,
250: ISO 250,
320: ISO 320,
400: ISO 400,
500: ISO 500,
640: ISO 640,
800: ISO 800,
1000: ISO 1000,
1250: ISO 1250,
1600: ISO 1600,
2000: ISO 2000,
2500: ISO 2500,
3200: ISO 3200,
4000: ISO 4000,
5000: ISO 5000,
6400: ISO 6400"""

add(e, 
name="CAM_ISO",
disp="Camera ISO",
desc="Light Sensitivity",
val=val_iso,
rng=None,
inc=None,
ro=None,
user="Standard")

val_aperture="""5.6: f5.6,
6.3: f6.3,
7.1: f7.1,
8.0: f8,
9.0: f9,
10.0: f10,
11.0: f11,
12.0: f12,
14.0: f14,
16.0: f16,
18.0: f18,
20.0: f20,
22.0: f22"""

add(e, 
name="CAM_APERTURE",
disp="Camera Aperture",
desc="F-stop value representing the aperture.",
val=val_aperture,
rng=None,
inc=None,
ro=None,
user="Standard")

val_sh_spd="""-1000: 1s,
-800: 0.8s,
-600: 0.6s,
-500: 0.5s,
-400: 0.4s,
3: 1/3,
4: 1/4,
5: 1/5,
6: 1/6,
8: 1/8,
10: 1/10,
13: 1/13,
15: 1/15,
20: 1/20,
25: 1/25,
30: 1/30,
40: 1/40,
50: 1/50,
60: 1/60,
80: 1/80,
100: 1/100,
125: 1/125,
160: 1/160,
200: 1/200,
250: 1/250,
320: 1/320,
400: 1/400,
500: 1/500,
640: 1/640,
800: 1/800,
1000: 1/1000,
1250: 1/1250,
1600: 1/1600,
2000: 1/2000,
2500: 1/2500"""

add(e, 
name="CAM_SHUTTERSPD",
disp="Shutter Speed",
desc=None,
val=val_sh_spd,
rng=None,
inc=None,
ro=None,
user="Standard")

add(e, 
name="CAM_EV",
disp="Exposure Compensation",
desc=None,
val="""-3.0: -3.0,
-2.67: -2.7,
-2.33: -2.3,
-2.0: -2.0,
-1.67: -1.7,
-1.33: -1.3,
-1.0: -1.0,
-0.67: -0.7,
-0.33: -0.3,
0.0: 0,
0.33: +0.3,
0.67: +0.7,
1.0: +1.0,
1.33: +1.3,
1.67: +1.7,
2.0: +2.0,
2.33: +2.3,
2.67: +2.7,
3.0: +3.0""",
rng=None,
inc=None,
ro=None,
user="Standard")

add(e, 
name="SHUTTER_MODE",
disp="Shutter Mode",
desc=None,
val="""0: Leaf Shutter,
1: Fusion Shutter""",
rng=None,
inc=None,
ro=None,
user="Standard")

add(e, 
name="AE_PRIORITY",
disp="Auto Exposure Priority",
desc=None,
val="""0: ISO/Aperture/Shutter,
1: ISO/Shutter/Aperture,
2: Aperture/ISO/Shutter,
3: Aperture/Shutter/ISO,
4: Shutter/Aperture/ISO,
5: Shutter/ISO/Aperture""",
rng=None,
inc=None,
ro=None,
user="Standard")

add(e, 
name="AE_ISO_MIN",
disp="Auto Exposure Min ISO",
desc=None,
val=val_iso,
rng=None,
inc=None,
ro=None,
user="Standard")

add(e, 
name="AE_ISO_MAX",
disp="Auto Exposure Max ISO",
desc=None,
val=val_iso,
rng=None,
inc=None,
ro=None,
user="Standard")

add(e, 
name="AE_SH_SPD_MIN",
disp="Auto Exposure Min Shutter Speed",
desc=None,
val=val_sh_spd,
rng=None,
inc=None,
ro=None,
user="Standard")

add(e, 
name="AE_SH_SPD_MAX",
disp="Auto Exposure Max Shutter Speed",
desc=None,
val=val_sh_spd,
rng=None,
inc=None,
ro=None,
user="Standard")

add(e, 
name="AE_APERTURE_MIN",
disp="Auto Exposure Min Camera Aperture",
desc=None,
val=val_aperture,
rng=None,
inc=None,
ro=None,
user="Standard")

add(e, 
name="AE_APERTURE_MAX",
disp="Auto Exposure Max Camera Aperture",
desc=None,
val=val_aperture,
rng=None,
inc=None,
ro=None,
user="Standard")

add(e, 
name="CAPTURE_MODE",
disp="Capture Mode",
desc=None,
val="""0: Off,
1: Horizontal Distance,
2: Vertical Distance,
3: 3D Distance,
4: Time Interval,
5: Manual Focus Bracketing,
6: Automatic Focus Bracketing,
7: Burst""",
rng=None,
inc=None,
ro=None,
user="Standard")

add(e, 
name="DIST_INTERVAL",
disp="Distance Interval for Auto Capture [m]",
desc=None,
val=None,
rng="0 1000",
inc=None,
ro=None,
user="Standard")

add(e, 
name="TIME_INTERVAL",
disp="Time Interval for Auto Capture [s]",
desc=None,
val=None,
rng="0 3600",
inc=None,
ro=None,
user="Standard")

add(e, 
name="CAPTURE_COUNT",
disp="Capture Count for Burst Mode",
desc=None,
val=None,
rng="0 10",
inc="1",
ro=None,
user="Standard")

add(e, 
name="FOCUS_MODE",
disp="Focus mode",
desc=None,
val="""0: Manual,
1: Auto""",
rng=None,
inc=None,
ro=None,
user="Standard")

add(e, 
name="FOCUS_DIST",
disp="Focus distance",
desc=None,
val=None,
rng="3 180",
inc=None,
ro=None,
user="Standard")

add(e, 
name="AF_MIN_DIST",
disp="Auto Focus Min Distance",
desc=None,
val=None,
rng="3 180",
inc=None,
ro=None,
user="Standard")

add(e, 
name="AF_MAX_DIST",
disp="Auto Focus Max Distance",
desc=None,
val=None,
rng="3 180",
inc=None,
ro=None,
user="Standard")

add(e, 
name="AF_STRATEGY",
disp="Focus Limit Control",
desc=None,
val="""0: Clip Distance,
1: Gate Distance,
2: Relative Distance""",
rng=None,
inc=None,
ro=None,
user="Standard")

add(e, 
name="AF_STRATEGY_THR",
disp="Threshold for Relative Distance [m]",
desc=None,
val=None,
rng="0 180",
inc=None,
ro=None,
user="Standard")

add(e, 
name="FOCUS_BKT_MODE",
disp="Focus Bracketing Mode",
desc=None,
val="""0: Around focus point,
1: In front of focus point,
2: Behind focus point""",
rng=None,
inc=None,
ro=None,
user="Standard")

add(e, 
name="FOCUS_BKT_COUNT",
disp="Focus Bracketing Capture Count",
desc=None,
val=None,
rng="1 100",
inc="1",
ro=None,
user="Standard")

add(e, 
name="FOCUS_BKT_STEP",
disp="Focus Bracketing Motor Step Count",
desc=None,
val=None,
rng="1 100",
inc="1",
ro=None,
user="Standard")

add(e, 
name="FOCUS_BKT_COC",
disp="Focus Bracketing Circle of Confusion",
desc=None,
val=None,
rng="1 100",
inc="1",
ro=None,
user="Standard")

add(e, 
name="FOCUS_BKT_OVRLP",
disp="Focus Bracketing Overlap",
desc=None,
val=None,
rng="1 100",
inc="1",
ro=None,
user="Standard")

add(e, 
name="FOCUS_BKT_DEPTH",
disp="Focus Bracketing Depth",
desc=None,
val=None,
rng="1 100",
inc="1",
ro=None,
user="Standard")

add(e, 
name="WHITE_BALANCE",
disp="White Balance",
desc=None,
val="""0: Auto,
1: Daylight,
2: Fluorescent,
3: Tungsten,
4: Flash,
5: Custom1,
6: Custom2,
7: Custom3,
8: Aerial""",
rng=None,
inc=None,
ro=None,
user="Standard")

add(e, 
name="HDMI_LV",
disp="HDMI Live View",
desc=None,
val="""0: Disabled,
1: Enabled""",
rng=None,
inc=None,
ro=None,
user="Standard")

add(e, 
name="HDMI_LV_ZOOM",
disp="HDMI Live View Zoom",
desc=None,
val="""0: Overview,
1: 100%""",
rng=None,
inc=None,
ro=None,
user="Standard")

add(e, 
name="HDMI_OVERLAY",
disp="HDMI Overlay",
desc=None,
val="""0: Disabled,
1: Enabled""",
rng=None,
inc=None,
ro=None,
user="Standard")

add(e, 
name="OVERLAY_TRANSP",
disp="Overlay Transparency",
desc=None,
val=None,
rng="1 255",
inc="1",
ro=None,
user="Standard")

add(e, 
name="FOCUS_POINT",
disp="Overlay Focus Point",
desc=None,
val="""0: Disabled,
1: Enabled""",
rng=None,
inc=None,
ro=None,
user="Standard")

add(e, 
name="OVERLAY_PREVIEW",
disp="Overlay Preview",
desc=None,
val="""0: Off,
1: Small,
4: Large""",
rng=None,
inc=None,
ro=None,
user="Standard")

add(e, 
name="PREVIEW_TIME",
disp="Overlay Preview Time",
desc=None,
val="""0: No Timeout,
2000: 2s,
4000: 4s,
6000: 6s,
10000: 10s,
15000: 15s,
30000: 30s""",
rng=None,
inc=None,
ro=None,
user="Standard")

add(e, 
name="FOCUS_MASK",
disp="Focus Mask",
desc=None,
val="""0: Disabled,
1: Enabled""",
rng=None,
inc=None,
ro=None,
user="Standard")

add(e, 
name="FOCUS_MASK_THR",
disp="Focus Mask Threshold",
desc=None,
val=None,
rng="1 1000",
inc="1",
ro=None,
user="Standard")

add(e, 
name="LEVER_ARM_FRONT",
disp="Camera Lever Arm Front",
desc="X coordinate of camera lever arm (from aircraft's center of gravity to gimbal's center of rotation)",
val=None,
rng=None,
inc=None,
ro=None,
user="Standard")

add(e, 
name="LEVER_ARM_RIGHT",
disp="Camera Lever Arm Right",
desc="Y coordinate of camera lever arm (from aircraft's center of gravity to gimbal's center of rotation)",
val=None,
rng=None,
inc=None,
ro=None,
user="Standard")

add(e, 
name="LEVER_ARM_UP",
disp="Camera Lever Arm Up",
desc="Z coordinate of camera lever arm (from aircraft's center of gravity to gimbal's center of rotation)",
val=None,
rng=None,
inc=None,
ro=None,
user="Standard")

add(e, 
name="NEW_FOLDER",
disp="New Folder",
desc="Create a new picture folder on the memory card.",
val="""0: None,
1: Create""",
rng=None,
inc=None,
ro=None,
user="Standard")

add(e, 
name="STORAGE_FORMAT",
disp="Storage Format",
desc="Format memory card (erasing all data on the memory card).",
val="""0: None,
1: Format""",
rng=None,
inc=None,
ro=None,
user="Standard")

add(e, 
name="MASS_STORAGE",
disp="Mass Storage",
desc="Let the camera behave as a memory card reader when connected to a computer via USB-C.",
val="""0: Disable,
1: Enable""",
rng=None,
inc=None,
ro=None,
user="Standard")

add(e, 
name="CUSTOM_INFO",
disp="Custom Information",
desc="Custom information to be added in the XMP metadata (only 1 character in Mission Planner).",
val=None,
rng="32 126",
inc=None,
ro=None,
user="Standard")

add(e, 
name="MAV_CAM_COMP_ID",
disp="MAVLink Camera Component ID",
desc=None,
val="""100: Camera 1,
101: Camera 2,
102: Camera 3,
103: Camera 4,
104: Camera 5,
105: Camera 6""",
rng=None,
inc=None,
ro=None,
user="Standard")

add(e, 
name="MAV_GMB_COMP_ID",
disp="MAVLink Gimbal Component ID",
desc=None,
val="""154: Gimbal 1,
171: Gimbal 2,
172: Gimbal 3,
173: Gimbal 4,
174: Gimbal 5,
175: Gimbal 6""",
rng=None,
inc=None,
ro=None,
user="Standard")

add(e, 
name="GMB_PARAM_RFRSH",
disp="Refresh Gimbal Parameters",
desc="Refresh cached value of gimbal parameters on camera.",
val="""0: None,
1: Refresh""",
rng=None,
inc=None,
ro=None,
user="Standard")

add(e, 
name="GMB_PARAM_STAT",
disp="Status of Refreshing Gimbal Parameters",
desc="Status of Refreshing Gimbal Parameters (Read Only)",
val=None,
rng=None,
inc=None,
ro=None,
user="Standard")

add(e, 
name="GMB_PARAM_NUM",
disp="Number of Gimbal Parameters",
desc="Number of Gimbal Parameters (Read Only)",
val=None,
rng=None,
inc=None,
ro=None,
user="Standard")

add(e, 
name="LRF_FORWARD",
disp="Enable Forwarding of Laser Range Finder Measurements",
desc=None,
val="""0: Disabled,
1: Enabled""",
rng=None,
inc=None,
ro=None,
user="Standard")

add(e, 
name="LRF_FREQUENCY",
disp="Frequency of Forwarding Laser Range Finder Measurements",
desc=None,
val="""1: 1 Hz,
2: 2 Hz,
4: 4 Hz,
8: 8 Hz,
16: 16 Hz""",
rng=None,
inc=None,
ro=None,
user="Standard")

add(e, 
name="LRF_ORIENTATION",
disp="Orientation field of DISTANCE_SENSOR message",
desc=None,
val=None,
rng="0 40",
inc=None,
ro=None,
user="Standard")

add(e, 
name="GMB_REBOOT",
disp="Reboot Gimbal",
desc=None,
val="""0: None,
1: Reboot""",
rng=None,
inc=None,
ro=None,
user="Standard")

add(e, 
name="VERSION_X",
disp="X of Gimbal Firmware Version X.Y.Z",
desc="X of Gimbal Firmware Version X.Y.Z (Read Only)",
val=None,
rng=None,
inc=None,
ro="True",
user="Standard")

add(e, 
name="VERSION_Y",
disp="Y of Gimbal Firmware Version X.Y.Z",
desc="Y of Gimbal Firmware Version X.Y.Z (Read Only)",
val=None,
rng=None,
inc=None,
ro="True",
user="Standard")

add(e, 
name="VERSION_Z",
disp="Z of Gimbal Firmware Version X.Y.Z",
desc="Z of Gimbal Firmware Version X.Y.Z (Read Only)",
val=None,
rng=None,
inc=None,
ro="True",
user="Standard")

add(e, 
name="SRL_NUMBER",
disp="Serial Number of Gimbal",
desc="Serial Number of Gimbal (Read Only)",
val=None,
rng=None,
inc=None,
ro="True",
user="Standard")

add(e, 
name="STIFF_TILT",
disp="Stiffness on Tilt Axis",
desc=None,
val=None,
rng="0 255",
inc=None,
ro=None,
user="Standard")

add(e, 
name="GAIN_ALL",
disp="Proportional Gain on Pan, Roll and Tilt Axis",
desc=None,
val=None,
rng="0 255",
inc=None,
ro=None,
user="Standard")

add(e, 
name="RC_CHAN_STILT",
disp="Not Used",
desc="Not Used (Read Only)",
val=None,
rng=None,
inc=None,
ro="True",
user="Standard")

add(e, 
name="STIFF_ROLL",
disp="Stiffness on Roll Axis",
desc=None,
val=None,
rng="0 255",
inc=None,
ro=None,
user="Standard")

add(e, 
name="MT_OFF_ROLL",
disp="Encoder Calibrated Value on Roll Axis",
desc="Encoder Calibrated Value on Roll Axis (Read Only)",
val=None,
rng=None,
inc=None,
ro="True",
user="Standard")

add(e, 
name="FLW_EN_TILT",
disp="Follow Enabled on Tilt Axis",
desc=None,
val=None,
rng="0 1",
inc=None,
ro=None,
user="Standard")

add(e, 
name="STIFF_PAN",
disp="Stiffness on Pan Axis",
desc=None,
val=None,
rng="0 255",
inc=None,
ro=None,
user="Standard")

add(e, 
name="FILTER_OUT",
disp="Output Filter",
desc=None,
val=None,
rng="0 10",
inc=None,
ro=None,
user="Standard")

add(e, 
name="RC_CHAN_SPAN",
disp="Not Used",
desc="Not Used (Read Only)",
val=None,
rng=None,
inc=None,
ro="True",
user="Standard")

add(e, 
name="PWR_TILT",
disp="Minimum Power on Tilt Axis",
desc=None,
val=None,
rng="0 100",
inc=None,
ro=None,
user="Standard")

add(e, 
name="PWR_ROLL",
disp="Minimum Power on Roll Axis",
desc=None,
val=None,
rng="0 100",
inc=None,
ro=None,
user="Standard")

add(e, 
name="PWR_PAN",
disp="Minimum Power on Pan Axis",
desc=None,
val=None,
rng="0 100",
inc=None,
ro=None,
user="Standard")

add(e, 
name="FLW_SP_TILT",
disp="Follow Speed on Tilt Axis",
desc=None,
val=None,
rng="0 100",
inc=None,
ro=None,
user="Standard")

add(e, 
name="GMB_HOME_PAN",
disp="Home Position on Pan Axis",
desc=None,
val=None,
rng="-180 180",
inc=None,
ro=None,
user="Standard")

add(e, 
name="FLW_SP_PAN",
disp="Follow Speed on Pan Axis",
desc=None,
val=None,
rng="0 100",
inc=None,
ro=None,
user="Standard")

add(e, 
name="FLW_LPF_TILT",
disp="Follow Low-pass Filter on Tilt Axis",
desc=None,
val=None,
rng="0 100",
inc=None,
ro=None,
user="Standard")

add(e, 
name="MAPPING_ANGLE",
disp="Mapping Angle",
desc=None,
val=None,
rng="0 90",
inc=None,
ro=None,
user="Standard")

add(e, 
name="FLW_LPF_PAN",
disp="Follow Low-pass Filter on Pan Axis",
desc=None,
val=None,
rng="0 100",
inc=None,
ro=None,
user="Standard")

add(e, 
name="GYRO_TRUST",
disp="Gyro Trust",
desc=None,
val=None,
rng="0 255",
inc=None,
ro=None,
user="Standard")

add(e, 
name="RC_DZONE_TILT",
disp="Deadzone on Tilt Commands",
desc=None,
val=None,
rng="0 255",
inc=None,
ro=None,
user="Standard")

add(e, 
name="RC_DZONE_ROLL",
disp="Deadzone on Roll Commands",
desc=None,
val=None,
rng="0 255",
inc=None,
ro=None,
user="Standard")

add(e, 
name="RC_DZONE_PAN",
disp="Deadzone on Pan Commands",
desc=None,
val=None,
rng="0 255",
inc=None,
ro=None,
user="Standard")

add(e, 
name="GMB_LIM_PAN",
disp="Not Used",
desc="Not Used (Read Only)",
val=None,
rng=None,
inc=None,
ro="True",
user="Standard")

add(e, 
name="PWR_AUTO",
disp="Auto Power",
desc=None,
val=None,
rng="0 1",
inc=None,
ro=None,
user="Standard")

add(e, 
name="GMB_INVERTED",
disp="Inverted Mode",
desc=None,
val=None,
rng="0 1",
inc=None,
ro=None,
user="Standard")

add(e, 
name="AIR_ENABLE",
disp="Not Used",
desc="Not Used (Read Only)",
val=None,
rng=None,
inc=None,
ro="True",
user="Standard")

add(e, 
name="RC_TYPE",
disp="Not Used",
desc="Not Used (Read Only)",
val=None,
rng=None,
inc=None,
ro="True",
user="Standard")

add(e, 
name="GYRO_LPF",
disp="Gyroscope Low-pass Filter",
desc=None,
val=None,
rng="0 10",
inc=None,
ro=None,
user="Standard")

add(e, 
name="RC_LIM_MIN_TILT",
disp="Min Limit on Tilt Axis",
desc=None,
val=None,
rng="-90 0",
inc=None,
ro=None,
user="Standard")

add(e, 
name="RC_LIM_MAX_TILT",
disp="Max Limit on Tilt Axis",
desc=None,
val=None,
rng="0 90",
inc=None,
ro=None,
user="Standard")

add(e, 
name="RC_LIM_MIN_ROLL",
disp="Min Limit on Roll Axis",
desc=None,
val=None,
rng="-45 0",
inc=None,
ro=None,
user="Standard")

add(e, 
name="RC_LIM_MAX_ROLL",
disp="Max Limit on Roll Axis",
desc=None,
val=None,
rng="0 45",
inc=None,
ro=None,
user="Standard")

add(e, 
name="GMB_HOFF_TILT",
disp="Encoder Calibrated Value on Tilt Axis",
desc="Encoder Calibrated Value on Tilt Axis (Read Only)",
val=None,
rng=None,
inc=None,
ro="True",
user="Standard")

add(e, 
name="GMB_HOFF_ROLL",
disp="Encoder Calibrated Value on Roll Axis",
desc="Encoder Calibrated Value on Roll Axis (Read Only)",
val=None,
rng=None,
inc=None,
ro="True",
user="Standard")

add(e, 
name="RC_LPF_TILT",
disp="Low-pass Filter on Tilt Commands",
desc=None,
val=None,
rng="0 100",
inc=None,
ro=None,
user="Standard")

add(e, 
name="RC_LPF_ROLL",
disp="Low-pass Filter on Roll Commands",
desc=None,
val=None,
rng="0 100",
inc=None,
ro=None,
user="Standard")

add(e, 
name="RC_LPF_PAN",
disp="Low-pass Filter on Pan Commands",
desc=None,
val=None,
rng="0 100",
inc=None,
ro=None,
user="Standard")

add(e, 
name="RC_CHAN_TILT",
disp="Not Used",
desc="Not Used (Read Only)",
val=None,
rng=None,
inc=None,
ro="True",
user="Standard")

add(e, 
name="RC_CHAN_ROLL",
disp="Not Used",
desc="Not Used (Read Only)",
val=None,
rng=None,
inc=None,
ro="True",
user="Standard")

add(e, 
name="RC_CHAN_PAN",
disp="Not Used",
desc="Not Used (Read Only)",
val=None,
rng=None,
inc=None,
ro="True",
user="Standard")

add(e, 
name="RC_CHAN_MODE",
disp="Not Used",
desc="Not Used (Read Only)",
val=None,
rng=None,
inc=None,
ro="True",
user="Standard")

add(e, 
name="ACC_OFFSETX",
disp="Accelerometer Calibrated Value on X-axis",
desc="Accelerometer Calibrated Value on X-axis (Read Only)",
val=None,
rng=None,
inc=None,
ro="True",
user="Standard")

add(e, 
name="ACC_OFFSETY",
disp="Accelerometer Calibrated Value on Y-axis",
desc="Accelerometer Calibrated Value on Y-axis (Read Only)",
val=None,
rng=None,
inc=None,
ro="True",
user="Standard")

add(e, 
name="ACC_OFFSETZ",
disp="Accelerometer Calibrated Value on Z-axis",
desc="Accelerometer Calibrated Value on Z-axis (Read Only)",
val=None,
rng=None,
inc=None,
ro="True",
user="Standard")

add(e, 
name="GYRO_OFFSETX",
disp="Gyroscope Calibrated Value on X-axis",
desc="Gyroscope Calibrated Value on X-axis (Read Only)",
val=None,
rng=None,
inc=None,
ro="True",
user="Standard")

add(e, 
name="GYRO_OFFSETY",
disp="Gyroscope Calibrated Value on Y-axis",
desc="Gyroscope Calibrated Value on Y-axis (Read Only)",
val=None,
rng=None,
inc=None,
ro="True",
user="Standard")

add(e, 
name="GYRO_OFFSETZ",
disp="Gyroscope Calibrated Value on Z-axis",
desc="Gyroscope Calibrated Value on Z-axis (Read Only)",
val=None,
rng=None,
inc=None,
ro="True",
user="Standard")

add(e, 
name="MT_OFF_TILT",
disp="Encoder Calibrated Value on Tilt Axis",
desc="Encoder Calibrated Value on Tilt Axis (Read Only)",
val=None,
rng=None,
inc=None,
ro="True",
user="Standard")

add(e, 
name="MAPPING_ENABLE",
disp="Mapping Enable",
desc=None,
val=None,
rng="0 1",
inc=None,
ro=None,
user="Standard")

add(e, 
name="RC_TRIM_TILT",
disp="Not Used",
desc="Not Used (Read Only)",
val=None,
rng=None,
inc=None,
ro="True",
user="Standard")

add(e, 
name="RC_TRIM_ROLL",
disp="Not Used",
desc="Not Used (Read Only)",
val=None,
rng=None,
inc=None,
ro="True",
user="Standard")

add(e, 
name="RC_TRIM_PAN",
disp="Not Used",
desc="Not Used (Read Only)",
val=None,
rng=None,
inc=None,
ro="True",
user="Standard")

add(e, 
name="RC_MODE_TILT",
disp="Follow/Lock Mode on Tilt Axis",
desc=None,
val=None,
rng="0 1",
inc=None,
ro=None,
user="Standard")

add(e, 
name="RC_MODE_ROLL",
disp="Follow/Lock Mode on Roll Axis",
desc=None,
val=None,
rng="0 1",
inc=None,
ro=None,
user="Standard")

add(e, 
name="RC_MODE_PAN",
disp="Follow/Lock Mode on Pan Axis",
desc=None,
val=None,
rng="0 1",
inc=None,
ro=None,
user="Standard")

add(e, 
name="FLW_WD_TILT",
disp="Follow Window on Tilt Axis",
desc=None,
val=None,
rng="0 100",
inc=None,
ro=None,
user="Standard")

add(e, 
name="FLW_WD_PAN",
disp="Follow Windows on Pan Axis",
desc=None,
val=None,
rng="0 100",
inc=None,
ro=None,
user="Standard")

add(e, 
name="MT_OFF_PAN",
disp="Encoder Calibrated Value on Pan Axis",
desc="Encoder Calibrated Value on Pan Axis (Read Only)",
val=None,
rng=None,
inc=None,
ro="True",
user="Standard")

add(e, 
name="RC_SPD_TILT",
disp="Speed on Tilt Commands",
desc=None,
val=None,
rng="0 100",
inc=None,
ro=None,
user="Standard")

add(e, 
name="RC_SPD_ROLL",
disp="Speed on Roll Commands",
desc=None,
val=None,
rng="0 100",
inc=None,
ro=None,
user="Standard")

add(e, 
name="RC_SPD_PAN",
disp="Speed on Pan Commands",
desc=None,
val=None,
rng="0 100",
inc=None,
ro=None,
user="Standard")

add(e, 
name="RC_REVERSE_AXIS",
disp="Bitmask for 5 Parameters",
desc=None,
val=None,
rng="0 31",
inc=None,
ro=None,
user="Standard")

add(e, 
name="AIR_OFF_HOZ",
disp="Not Used",
desc="Not Used (Read Only)",
val=None,
rng=None,
inc=None,
ro="True",
user="Standard")

add(e, 
name="AIR_OFF_VEL",
disp="Not Used",
desc="Not Used (Read Only)",
val=None,
rng=None,
inc=None,
ro="True",
user="Standard")

add(e, 
name="GMB_HOFF_PAN",
disp="Encoder Calibrated Value on Pan Axis",
desc="Encoder Calibrated Value on Pan Axis (Read Only)",
val=None,
rng=None,
inc=None,
ro="True",
user="Standard")

add(e, 
name="RC_LIM_MIN_PAN",
disp="Min Limit on Pan Axis",
desc=None,
val=None,
rng="-320 0",
inc=None,
ro=None,
user="Standard")

add(e, 
name="RC_LIM_MAX_PAN",
disp="Max Limit on Pan Axis",
desc=None,
val=None,
rng="0 320",
inc=None,
ro=None,
user="Standard")

add(e, 
name="GMB_OFF_OVAL",
disp="Accelerometer Oval Offset",
desc=None,
val=None,
rng="0 2",
inc=None,
ro=None,
user="Standard")

add(e, 
name="MAV_EMIT_HB",
disp="Frequency of Heartbeat Messages in Hz",
desc=None,
val=None,
rng="0 50",
inc=None,
ro=None,
user="Standard")

add(e, 
name="MAV_RATE_ST",
disp="Frequency of System Status Messages in Hz",
desc=None,
val=None,
rng="0 50",
inc=None,
ro=None,
user="Standard")

add(e, 
name="MAV_RATE_ENCCNT",
disp="Frequency of Encoder Messages in Hz",
desc=None,
val=None,
rng="0 50",
inc=None,
ro=None,
user="Standard")

add(e, 
name="MAV_TS_ENCNT",
disp="Control Mode: Angle or Rate",
desc=None,
val=None,
rng="0 1",
inc=None,
ro=None,
user="Standard")

add(e, 
name="MAV_RATE_ORIEN",
disp="Frequency of Mount Orientation Messages in Hz",
desc=None,
val=None,
rng="0 50",
inc=None,
ro=None,
user="Standard")

add(e, 
name="MAV_RATE_IMU",
disp="Frequency of IMU Messages in Hz",
desc=None,
val=None,
rng="0 50",
inc=None,
ro=None,
user="Standard")

add(e, 
name="BAUDRATE_COM2",
disp="Baudrate on COM port 2",
desc=None,
val=None,
rng="1152 9216",
inc=None,
ro=None,
user="Standard")

add(e, 
name="BAUDRATE_COM4",
disp="Baudrate on COM port 4",
desc=None,
val=None,
rng="1152 9216",
inc=None,
ro=None,
user="Standard")

add(e, 
name="GIMBAL_COMPID",
disp="MAVLink Component ID of Gimbal",
desc=None,
val=None,
rng="154 175",
inc=None,
ro=None,
user="Standard")

add(e, 
name="TILT_DAMPING",
disp="Damping on Tilt Axis",
desc=None,
val=None,
rng="0 255",
inc=None,
ro=None,
user="Standard")

add(e, 
name="ROLL_DAMPING",
disp="Damping on Roll Axis",
desc=None,
val=None,
rng="0 255",
inc=None,
ro=None,
user="Standard")

add(e, 
name="PAN_DAMPING",
disp="Damping on Pan Axis",
desc=None,
val=None,
rng="0 255",
inc=None,
ro=None,
user="Standard")

end(r)
