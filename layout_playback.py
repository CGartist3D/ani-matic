import maya.cmds as cmds

def playbackRate(RT):
    if RT == True:
        # sets Playback Speed to Realtime, but caps Max Playback Speed to scene's Frame Rate
        cmds.playbackOptions(playbackSpeed=1, maxPlaybackSpeed=1)
    else:
        cmds.playbackOptions(playbackSpeed=0, maxPlaybackSpeed=1)

#playbackRate(True)

def playbackWin(all):
    if all == True:
        cmds.playbackOptions(view='all')
    else:
        cmds.playbackOptions(view='active')

#playbackWin(True)