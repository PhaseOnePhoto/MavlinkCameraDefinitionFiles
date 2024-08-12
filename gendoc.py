

from xml.etree.ElementTree import Element, ElementTree, indent


def add(e : Element, name, disp, desc = None, val = None, rng = None, inc = None, ro = None, user = None):
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
val="""0:Manual,
1:Auto""",
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
disp="ISO",
val=val_iso,
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
disp="Aperture",
val=val_aperture,
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
val=val_sh_spd,
user="Standard")

add(e, 
name="CAM_EV",
disp="Exposure Compensation",
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
user="Standard")

add(e, 
name="SHUTTER_MODE",
disp="Shutter Mode",
val="""0: Leaf Shutter,
1: Fusion Shutter""",
user="Standard")

add(e, 
name="AE_PRIORITY",
disp="Auto Exposure Priority",
val="""0: ISO/Aperture/Shutter,
1: ISO/Shutter/Aperture,
2: Aperture/ISO/Shutter,
3: Aperture/Shutter/ISO,
4: Shutter/Aperture/ISO,
5: Shutter/ISO/Aperture""",
user="Standard")

add(e, 
name="AE_ISO_MIN",
disp="Auto Exposure Min ISO",
val=val_iso,
user="Standard")

add(e, 
name="AE_ISO_MAX",
disp="Auto Exposure Max ISO",
val=val_iso,
user="Standard")

add(e, 
name="AE_SH_SPD_MIN",
disp="Auto Exposure Min Shutter Speed",
val=val_sh_spd,
user="Standard")

add(e, 
name="AE_SH_SPD_MAX",
disp="Auto Exposure Max Shutter Speed",
val=val_sh_spd,
user="Standard")

add(e, 
name="AE_APERTURE_MIN",
disp="Auto Exposure Min Aperture",
val=val_aperture,
user="Standard")

add(e, 
name="AE_APERTURE_MAX",
disp="Auto Exposure Max Aperture",
val=val_aperture,
user="Standard")

add(e, 
name="CAPTURE_MODE",
disp="Capture Mode",
val="""0: Off,
1: Horizontal Distance,
2: Vertical Distance,
3: 3D Distance,
4: Time Interval,
5: Manual Focus Bracketing,
6: Automatic Focus Bracketing,
7: Burst""",
user="Standard")

add(e, 
name="DIST_INTERVAL",
disp="Distance Interval for Auto Capture Mode Based on Distance [m]",
rng="0 1000",
user="Standard")

add(e, 
name="TIME_INTERVAL",
disp="Time Interval for Auto Capture Mode Based on Time [s]",
rng="0 3600",
user="Standard")

add(e, 
name="CAPTURE_COUNT",
disp="Capture Count for Burst Mode (only available on iXM-GS120)",
rng="0 10",
inc="1",
user="Standard")

add(e, 
name="FOCUS_MODE",
disp="Focus mode",
val="""0: Manual,
1: Auto""",
user="Standard")

add(e, 
name="FOCUS_DIST",
disp="Focus distance",
rng="3 180",
user="Standard")

add(e, 
name="AF_MIN_DIST",
disp="Auto Focus Min Distance",
rng="3 180",
user="Standard")

add(e, 
name="AF_MAX_DIST",
disp="Auto Focus Max Distance",
rng="3 180",
user="Standard")

add(e, 
name="AF_STRATEGY",
disp="Focus Limit Control",
val="""0: Clip Distance,
1: Gate Distance,
2: Relative Distance""",
user="Standard")

add(e, 
name="AF_STRATEGY_THR",
disp="Threshold for Relative Distance [m]",
rng="0 180",
user="Standard")

add(e, 
name="FOCUS_BKT_MODE",
disp="Focus Bracketing Mode",
val="""0: Around focus point,
1: In front of focus point,
2: Behind focus point""",
user="Standard")

add(e, 
name="FOCUS_BKT_CNT",
disp="Focus Bracketing Capture Count",
rng="1 100",
inc="1",
user="Standard")

add(e, 
name="FOCUS_BKT_STEP",
disp="Focus Bracketing Motor Step Count",
rng="1 100",
inc="1",
user="Standard")

add(e, 
name="FOCUS_BKT_COC",
disp="Focus Bracketing Circle of Confusion",
rng="1 100",
inc="1",
user="Standard")

add(e, 
name="FOCUS_BKT_OVRLP",
disp="Focus Bracketing Overlap",
rng="1 100",
inc="1",
user="Standard")

add(e, 
name="FOCUS_BKT_DEPTH",
disp="Focus Bracketing Depth",
rng="1 100",
inc="1",
user="Standard")

add(e, 
name="HDMI_LV",
disp="HDMI Live View",
val="""0: Disabled,
1: Enabled""",
user="Standard")

add(e, 
name="HDMI_OVERLAY",
disp="HDMI Overlay",
val="""0: Disabled,
4: Left with Margin,
5: Bottom,
6: Left""",
user="Standard")

add(e, 
name="OVERLAY_TRANSP",
disp="Overlay Transparency",
rng="1 255",
inc="1",
user="Standard")

add(e, 
name="HDMI_LV_ZOOM",
disp="HDMI Live View Zoom",
val="""0: Overview,
1: 100%""",
user="Standard")

add(e, 
name="FOCUS_POINT",
disp="Overlay Focus Point",
val="""0: Disabled,
1: Without LRF,
2: With LRF""",
user="Standard")

add(e, 
name="OVERLAY_PREVIEW",
disp="Overlay Preview",
val="""0: Off,
1: Small,
4: Large""",
user="Standard")

add(e, 
name="OVERLAY_CAP_FDBK",
disp="Overlay Capture Feedback",
val="""0: Disabled,
1: Enabled""",
user="Standard")

add(e, 
name="PREVIEW_TIME",
disp="Overlay Preview Time",
val="""0: No Timeout,
2000: 2s,
4000: 4s,
6000: 6s,
10000: 10s,
15000: 15s,
30000: 30s""",
user="Standard")

add(e, 
name="FOCUS_MASK",
disp="Focus Mask",
val="""0: Disabled,
1: Enabled""",
user="Standard")

add(e, 
name="FOCUS_MASK_THR",
disp="Focus Mask Threshold",
rng="1 1000",
inc="1",
user="Standard")

add(e, 
name="NEW_FOLDER",
disp="New Folder",
desc="Create a new picture folder on the memory card.",
val="""0: None,
1: Create""",
user="Standard")

add(e, 
name="STORAGE_FORMAT",
disp="Storage Format",
desc="Format memory card (erasing all data on the memory card).",
val="""0: None,
1: Format""",
user="Standard")

add(e, 
name="MASS_STORAGE",
disp="Mass Storage",
desc="Let the camera behave as a memory card reader when connected to a computer via USB-C.",
val="""0: Disable,
1: Enable""",
user="Standard")

add(e, 
name="CUSTOM_INFO",
disp="Custom Information",
desc="Custom information to be added in the XMP metadata (only 1 character in Mission Planner).",
rng="32 126",
user="Standard")

add(e, 
name="LEVER_ARM_FRONT",
disp="Camera Lever Arm Front [mm]",
desc="X coordinate of camera lever arm in millimeters (from aircraft's center of gravity to gimbal's center of rotation)",
rng="-10000 10000",
user="Standard")

add(e, 
name="LEVER_ARM_RIGHT",
disp="Camera Lever Arm Right [mm]",
desc="Y coordinate of camera lever arm in millimeters (from aircraft's center of gravity to gimbal's center of rotation)",
rng="-10000 10000",
user="Standard")

add(e, 
name="LEVER_ARM_UP",
disp="Camera Lever Arm Up [mm]",
desc="Z coordinate of camera lever arm in millimeters (from aircraft's center of gravity to gimbal's center of rotation)",
rng="-10000 10000",
user="Standard")

add(e, 
name="WHITE_BALANCE",
disp="White Balance",
val="""0: Auto,
1: Daylight,
2: Fluorescent,
3: Tungsten,
4: Flash,
5: Custom1,
6: Custom2,
7: Custom3,
8: Aerial""",
user="Standard")

add(e, 
name="MAV_CAM_COMP_ID",
disp="MAVLink Camera Component ID",
val="""100: Camera 1,
101: Camera 2,
102: Camera 3,
103: Camera 4,
104: Camera 5,
105: Camera 6""",
user="Standard")

add(e, 
name="MAV_GMB_COMP_ID",
disp="MAVLink Gimbal Component ID",
val="""154: Gimbal 1,
171: Gimbal 2,
172: Gimbal 3,
173: Gimbal 4,
174: Gimbal 5,
175: Gimbal 6""",
user="Standard")

add(e, 
name="GMB_PARAM_RFRSH",
disp="Refresh Cached Values of Gimbal Parameters on Camera",
val="""0: None,
1: Refresh""",
user="Standard")

add(e, 
name="GMB_PARAM_STAT",
disp="Status of Refreshing Gimbal Parameters",
desc="Status of Refreshing Gimbal Parameters (Read Only)",
user="Standard")

add(e, 
name="GMB_PARAM_NUM",
disp="Number of Gimbal Parameters",
desc="Number of Gimbal Parameters (Read Only)",
user="Standard")

add(e,
name="GMB_PARAM_FWD",
disp="Expose gimbal parameters as if they were camera parameters and forward read and write requests",
val="""0: Disabled,
1: Enabled""",
user="Standard")

add(e, 
name="GMB_AP_MSG_RATE",
disp="Requested Rate of AUTOPILOT_STATE_FOR_GIMBAL_DEVICE Message from Autopilot",
rng="0 100",
user="Standard")

add(e, 
name="GMB_AT_MSG_RATE",
disp="Requested Rate of Attitude Message from Autopilot",
rng="0 100",
user="Standard")

add(e, 
name="GPS_RAW_MSG_RATE",
disp="Requested Rate of Raw GPS Message from Autopilot",
rng="0 100",
user="Standard")

add(e, 
name="LRF_FREQUENCY",
disp="Frequency of Laser Range Finder Measurements",
rng="0 100",
user="Standard")

add(e, 
name="LRF_FORWARD",
disp="Enable Forwarding of Laser Range Finder Measurements to Ground Station",
val="""0: Disabled,
1: Enabled""",
user="Standard")

add(e, 
name="LRF_FWD_RATIO",
disp="Forward 1 over LRF_FWD_RATIO Laser Rangefinder Measurements to Ground Station",
rng="0 100",
user="Standard")

add(e, 
name="LRF_ORIENTATION",
disp="ORIENTATION Field of DISTANCE_SENSOR Message when Forwarding Laser Rangefinder Measurements to Ground Station",
rng="0 40",
user="Standard")

add(e,
name="LASER_CAP_CNT",
disp="Capture count when CAPTURE_MODE is set to 'Laser'",
rng="1 100",
user="Standard")

add(e,
name="LASER_CORR",
disp="Delay in milliseconds (lead time if negative) added to scheduled capture time when CAPTURE_MODE is set to 'Timed Laser'",
rng="-1000 1000",
user="Standard")

add(e, 
name="GMB_CMD",
disp="Command addressed by the camera to the gimbal",
val="""0: None,
1: Calibrate Gyro,
2: Turn on Motors,
3: Turn off Motors,
4: Reboot""",
user="Standard")

add(e,
name="GMB_PARAM_RESET",
disp="Factory Reset of Gimbal Parameters",
val="""0: None,
1: Reset""",
user="Standard")

add(e,
name="GMB_PARAM_BMP1",
disp="Bitmask for Gimbal Parameters Different than Default Value [0, 31]",
rng="0 4294967296",
user="Standard")

add(e,
name="GMB_PARAM_BMP2",
disp="Bitmask for Gimbal Parameters Different than Default Value [32, 63]",
rng="0 4294967296",
user="Standard")

add(e,
name="GMB_PARAM_BMP3",
disp="Bitmask for Gimbal Parameters Different than Default Value [64, 84]",
rng="0 4294967296",
user="Standard")

add(e,
name="CAM_ORIENT",
disp="Orientation for the video feed, image metadata and overlay preview",
val="""0: Horizontal,
1: Vertical""",
user="Standard")

add(e,
name="CAM_PARAM_RFRSH",
disp="Re-send List of Camera Parameters (Including Cached Gimbal Parameters) to Ground Station",
val="""0: None,
1: Refresh""",
user="Standard")

add(e,
name="CAM_PARAM_RESET",
disp="Set List of Camera Parameters back to Default Values",
val="""0: None,
1: Reset""",
user="Standard")

add(e, 
name="VERSION_X",
disp="X of Gimbal Firmware Version X.Y.Z",
desc="X of Gimbal Firmware Version X.Y.Z (Read Only)",
ro="True",
user="Standard")

add(e, 
name="VERSION_Y",
disp="Y of Gimbal Firmware Version X.Y.Z",
desc="Y of Gimbal Firmware Version X.Y.Z (Read Only)",
ro="True",
user="Standard")

add(e, 
name="VERSION_Z",
disp="Z of Gimbal Firmware Version X.Y.Z",
desc="Z of Gimbal Firmware Version X.Y.Z (Read Only)",
ro="True",
user="Standard")

add(e, 
name="SRL_NUMBER",
disp="Serial Number of Gimbal",
desc="Serial Number of Gimbal (Read Only)",
ro="True",
user="Standard")

add(e, 
name="STIFF_TILT",
disp="Stiffness on Tilt Axis",
rng="0 255",
user="Standard")

add(e, 
name="GAIN_ALL",
disp="Proportional Gain on Pan, Roll and Tilt Axis",
rng="0 255",
user="Standard")

add(e, 
name="RC_CHAN_STILT",
disp="Not Used",
desc="Not Used (Read Only)",
ro="True",
user="Standard")

add(e, 
name="STIFF_ROLL",
disp="Stiffness on Roll Axis",
rng="0 255",
user="Standard")

add(e, 
name="MT_OFF_ROLL",
disp="Encoder Calibrated Value on Roll Axis",
desc="Encoder Calibrated Value on Roll Axis (Read Only)",
ro="True",
user="Standard")

add(e, 
name="FLW_EN_TILT",
disp="Follow Enabled on Tilt Axis",
rng="0 1",
user="Standard")

add(e, 
name="STIFF_PAN",
disp="Stiffness on Pan Axis",
rng="0 255",
user="Standard")

add(e, 
name="FILTER_OUT",
disp="Output Filter",
rng="0 10",
user="Standard")

add(e, 
name="RC_CHAN_SPAN",
disp="Not Used",
desc="Not Used (Read Only)",
ro="True",
user="Standard")

add(e, 
name="PWR_TILT",
disp="Minimum Power on Tilt Axis",
rng="0 100",
user="Standard")

add(e, 
name="PWR_ROLL",
disp="Minimum Power on Roll Axis",
rng="0 100",
user="Standard")

add(e, 
name="PWR_PAN",
disp="Minimum Power on Pan Axis",
rng="0 100",
user="Standard")

add(e, 
name="FLW_SP_TILT",
disp="Follow Speed on Tilt Axis",
rng="0 100",
user="Standard")

add(e, 
name="GMB_HOME_PAN",
disp="Home Position on Pan Axis",
rng="-180 180",
user="Standard")

add(e, 
name="FLW_SP_PAN",
disp="Follow Speed on Pan Axis",
rng="0 100",
user="Standard")

add(e, 
name="FLW_LPF_TILT",
disp="Follow Low-pass Filter on Tilt Axis",
rng="0 100",
user="Standard")

add(e, 
name="MAPPING_ANGLE",
disp="Mapping Angle",
rng="0 90",
user="Standard")

add(e, 
name="FLW_LPF_PAN",
disp="Follow Low-pass Filter on Pan Axis",
rng="0 100",
user="Standard")

add(e, 
name="GYRO_TRUST",
disp="Gyro Trust",
rng="0 255",
user="Standard")

add(e, 
name="RC_DZONE_TILT",
disp="Deadzone on Tilt Commands",
rng="0 255",
user="Standard")

add(e, 
name="RC_DZONE_ROLL",
disp="Deadzone on Roll Commands",
rng="0 255",
user="Standard")

add(e, 
name="RC_DZONE_PAN",
disp="Deadzone on Pan Commands",
rng="0 255",
user="Standard")

add(e, 
name="GMB_LIM_PAN",
disp="Not Used",
desc="Not Used (Read Only)",
ro="True",
user="Standard")

add(e, 
name="PWR_AUTO",
disp="Auto Power",
rng="0 1",
user="Standard")

add(e, 
name="GMB_INVERTED",
disp="Inverted Mode",
rng="0 1",
user="Standard")

add(e, 
name="AIR_ENABLE",
disp="Not Used",
desc="Not Used (Read Only)",
ro="True",
user="Standard")

add(e, 
name="RC_TYPE",
disp="Not Used",
desc="Not Used (Read Only)",
ro="True",
user="Standard")

add(e, 
name="GYRO_LPF",
disp="Gyroscope Low-pass Filter",
rng="0 10",
user="Standard")

add(e, 
name="RC_LIM_MIN_TILT",
disp="Min Limit on Tilt Axis",
rng="-90 0",
user="Standard")

add(e, 
name="RC_LIM_MAX_TILT",
disp="Max Limit on Tilt Axis",
rng="0 90",
user="Standard")

add(e, 
name="RC_LIM_MIN_ROLL",
disp="Min Limit on Roll Axis",
rng="-45 0",
user="Standard")

add(e, 
name="RC_LIM_MAX_ROLL",
disp="Max Limit on Roll Axis",
rng="0 45",
user="Standard")

add(e, 
name="GMB_HOFF_TILT",
disp="Encoder Calibrated Value on Tilt Axis",
desc="Encoder Calibrated Value on Tilt Axis (Read Only)",
ro="True",
user="Standard")

add(e, 
name="GMB_HOFF_ROLL",
disp="Encoder Calibrated Value on Roll Axis",
desc="Encoder Calibrated Value on Roll Axis (Read Only)",
ro="True",
user="Standard")

add(e, 
name="RC_LPF_TILT",
disp="Low-pass Filter on Tilt Commands",
rng="0 100",
user="Standard")

add(e, 
name="RC_LPF_ROLL",
disp="Low-pass Filter on Roll Commands",
rng="0 100",
user="Standard")

add(e, 
name="RC_LPF_PAN",
disp="Low-pass Filter on Pan Commands",
rng="0 100",
user="Standard")

add(e, 
name="RC_CHAN_TILT",
disp="Not Used",
desc="Not Used (Read Only)",
ro="True",
user="Standard")

add(e, 
name="RC_CHAN_ROLL",
disp="Not Used",
desc="Not Used (Read Only)",
ro="True",
user="Standard")

add(e, 
name="RC_CHAN_PAN",
disp="Not Used",
desc="Not Used (Read Only)",
ro="True",
user="Standard")

add(e, 
name="RC_CHAN_MODE",
disp="Not Used",
desc="Not Used (Read Only)",
ro="True",
user="Standard")

add(e, 
name="ACC_OFFSETX",
disp="Accelerometer Calibrated Value on X-axis",
desc="Accelerometer Calibrated Value on X-axis (Read Only)",
ro="True",
user="Standard")

add(e, 
name="ACC_OFFSETY",
disp="Accelerometer Calibrated Value on Y-axis",
desc="Accelerometer Calibrated Value on Y-axis (Read Only)",
ro="True",
user="Standard")

add(e, 
name="ACC_OFFSETZ",
disp="Accelerometer Calibrated Value on Z-axis",
desc="Accelerometer Calibrated Value on Z-axis (Read Only)",
ro="True",
user="Standard")

add(e, 
name="GYRO_OFFSETX",
disp="Gyroscope Calibrated Value on X-axis",
desc="Gyroscope Calibrated Value on X-axis (Read Only)",
ro="True",
user="Standard")

add(e, 
name="GYRO_OFFSETY",
disp="Gyroscope Calibrated Value on Y-axis",
desc="Gyroscope Calibrated Value on Y-axis (Read Only)",
ro="True",
user="Standard")

add(e, 
name="GYRO_OFFSETZ",
disp="Gyroscope Calibrated Value on Z-axis",
desc="Gyroscope Calibrated Value on Z-axis (Read Only)",
ro="True",
user="Standard")

add(e, 
name="MT_OFF_TILT",
disp="Encoder Calibrated Value on Tilt Axis",
desc="Encoder Calibrated Value on Tilt Axis (Read Only)",
ro="True",
user="Standard")

add(e, 
name="MAPPING_ENABLE",
disp="Mapping Enable",
rng="0 1",
user="Standard")

add(e, 
name="RC_TRIM_TILT",
disp="Not Used",
desc="Not Used (Read Only)",
ro="True",
user="Standard")

add(e, 
name="RC_TRIM_ROLL",
disp="Not Used",
desc="Not Used (Read Only)",
ro="True",
user="Standard")

add(e, 
name="RC_TRIM_PAN",
disp="Not Used",
desc="Not Used (Read Only)",
ro="True",
user="Standard")

add(e, 
name="RC_MODE_TILT",
disp="Follow/Lock Mode on Tilt Axis",
rng="0 1",
user="Standard")

add(e, 
name="RC_MODE_ROLL",
disp="Follow/Lock Mode on Roll Axis",
rng="0 1",
user="Standard")

add(e, 
name="RC_MODE_PAN",
disp="Follow/Lock Mode on Pan Axis",
rng="0 1",
user="Standard")

add(e, 
name="FLW_WD_TILT",
disp="Follow Window on Tilt Axis",
rng="0 100",
user="Standard")

add(e, 
name="FLW_WD_PAN",
disp="Follow Windows on Pan Axis",
rng="0 100",
user="Standard")

add(e, 
name="MT_OFF_PAN",
disp="Encoder Calibrated Value on Pan Axis",
desc="Encoder Calibrated Value on Pan Axis (Read Only)",
ro="True",
user="Standard")

add(e, 
name="RC_SPD_TILT",
disp="Speed on Tilt Commands",
rng="0 100",
user="Standard")

add(e, 
name="RC_SPD_ROLL",
disp="Speed on Roll Commands",
rng="0 100",
user="Standard")

add(e, 
name="RC_SPD_PAN",
disp="Speed on Pan Commands",
rng="0 100",
user="Standard")

add(e, 
name="RC_REVERSE_AXIS",
disp="Bitmask for 5 Parameters",
rng="0 31",
user="Standard")

add(e, 
name="AIR_OFF_HOZ",
disp="Not Used",
desc="Not Used (Read Only)",
ro="True",
user="Standard")

add(e, 
name="AIR_OFF_VEL",
disp="Not Used",
desc="Not Used (Read Only)",
ro="True",
user="Standard")

add(e, 
name="GMB_HOFF_PAN",
disp="Encoder Calibrated Value on Pan Axis",
desc="Encoder Calibrated Value on Pan Axis (Read Only)",
ro="True",
user="Standard")

add(e, 
name="RC_LIM_MIN_PAN",
disp="Min Limit on Pan Axis",
rng="-320 0",
user="Standard")

add(e, 
name="RC_LIM_MAX_PAN",
disp="Max Limit on Pan Axis",
rng="0 320",
user="Standard")

add(e, 
name="GMB_OFF_OVAL",
disp="Accelerometer Oval Offset",
rng="0 2",
user="Standard")

add(e, 
name="MAV_EMIT_HB",
disp="Frequency of Heartbeat Messages in Hz",
rng="0 50",
user="Standard")

add(e, 
name="MAV_RATE_ST",
disp="Frequency of System Status Messages in Hz",
rng="0 50",
user="Standard")

add(e, 
name="MAV_RATE_ENCCNT",
disp="Frequency of Encoder Messages in Hz",
rng="0 50",
user="Standard")

add(e, 
name="MAV_TS_ENCNT",
disp="Control Mode: Angle or Rate",
rng="0 1",
user="Standard")

add(e, 
name="MAV_RATE_ORIEN",
disp="Frequency of Mount Orientation Messages in Hz",
rng="0 50",
user="Standard")

add(e, 
name="MAV_RATE_IMU",
disp="Frequency of IMU Messages in Hz",
rng="0 50",
user="Standard")

add(e, 
name="BAUDRATE_COM2",
disp="Baudrate on COM port 2",
rng="1152 9216",
user="Standard")

add(e, 
name="BAUDRATE_COM4",
disp="Baudrate on COM port 4",
rng="1152 9216",
user="Standard")

add(e, 
name="GIMBAL_COMPID",
disp="MAVLink Component ID of Gimbal",
rng="154 175",
user="Standard")

add(e, 
name="TILT_DAMPING",
disp="Damping on Tilt Axis",
rng="0 255",
user="Standard")

add(e, 
name="ROLL_DAMPING",
disp="Damping on Roll Axis",
rng="0 255",
user="Standard")

add(e, 
name="PAN_DAMPING",
disp="Damping on Pan Axis",
rng="0 255",
user="Standard")

end(r)
