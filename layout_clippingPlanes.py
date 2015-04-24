import maya.cmds as cmds

def setClipPlanes(value):
    if value == 'button1':
        set_clip_plane_vals(0.01, 10000.0)
    elif value == 'button2':
        set_clip_plane_vals(0.1, 100000.0)
    elif value == 'button3':
        set_clip_plane_vals(1.0, 1000000.0)
    elif value == 'button4':
        set_clip_plane_vals(10.0, 10000000.0)
    else:
        print 'Error: Imaginary button pressed!'

def set_clip_plane_vals(near_val, far_val):
    cams = cmds.ls(cameras=True)
    for curr_cam in cams:
        try:
            cmds.camera (curr_cam, edit=True, cp=True, ncp=near_val, fcp=far_val)
        except RuntimeError, err:
            print 'Error: Camera clipping planes not set correctly for camera %s. (%s)' % (curr_cam, err[0][:-1])

#setClipPlanes('button1')
