import maya.cmds as cmds

def viewportColor(BG):
    if BG == 'gradGrey':
        cmds.displayPref(dgr=True)
    elif BG == 'Grey':
        cmds.displayPref(dgr=False)
        cmds.displayRGBColor('background', .631, .631, .631)
    elif BG == 'Green':
        cmds.displayPref(dgr=False)
        cmds.displayRGBColor('background', 0, 1, 0)
    elif BG == 'Blue':
        cmds.displayPref(dgr=False)
        cmds.displayRGBColor('background', 0, 0, 1)
    elif BG == 'Red':
        cmds.displayPref(dgr=False)
        cmds.displayRGBColor('background', 1, 0, 0)
    elif BG == 'White':
        cmds.displayPref(dgr=False)
        cmds.displayRGBColor('background', 1, 1, 1)
    elif BG == 'Black':
        cmds.displayPref(dgr=False)
        cmds.displayRGBColor('background', 0, 0, 0)
    else:
        print 'Error: There was a problem with setting the camera viewport background color'

#viewportColor('gradGrey')
