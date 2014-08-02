profile
=======

 common tmux,vim,tsch configuration
<<<<<<< HEAD
=======

export PYTHONSTARTUP=~/.pythonrc

----------~/.pythonrc---------_

# enabling name completion

# import needed modules
import atexit
import os
import readline
import rlcompleter

# where is history saved
historyPath = os.path.expanduser("~/.pyhistory")

# handler for saving history
def save_history(historyPath=historyPath):
    import readline
    readline.write_history_file(historyPath)

# read history, if it exists
if os.path.exists(historyPath):
    readline.set_history_length(10000)
    readline.read_history_file(historyPath)

# register saving handler
atexit.register(save_history)

# enable completion
readline.parse_and_bind('tab: complete')

# cleanup
del os, atexit, readline, rlcompleter, save_history, historyPath
>>>>>>> 2bffca51a98e1d9f2550615ad996adef4a8de344
