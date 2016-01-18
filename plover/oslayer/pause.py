import re

PAUSE_PATTERN = re.compile(r'Pause(:([0-9]+))?')

def is_pause(token):
    """
    Used to determine whether the 'key' is actually a request for
    a pause.  This is used by the various keyboard controllers.

    e.g. The key "Pause:500" is interpreted as a request to pause
    for 500 ms.  This is useful since sometimes a chord maps to
    a series of instructions that interacts with a program.  Adding
    pauses gives the program a chance to keep up.
    """
    match = re.match(PAUSE_PATTERN, token)
    if match:
        pause_int = match.groups()[1]
        if pause_int is None:
            pause_time = 0.05
        else:
            pause_time = float(pause_int)/1000
    else:
        pause_time = None
    is_pause = (pause_time is not None)
    return (is_pause, pause_time)

def keycode_is_pause(keycode):
    """
    Checks if the keycode representation (used in Linux and OSX) is a pause request.
    """
    return isinstance(keycode, tuple) and (len(keycode) == 2) and (keycode[0] == 'Pause')
