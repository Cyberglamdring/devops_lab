#!/bin/bash
# 0: install python v. 2.7 & 3.7
pyenv install 2.7.16
pyenv install 3.7.3

# 1: create first virtualenv
echo && echo "#################create first virtualenv#################" && echo
pyenv virtualenv 2.7.16 env1_v2.7
eval "$(pyenv init -)"
pyenv activate env1_v2.7
pyenv deactivate env1_v2.7

# 2: create second virtualenv
echo && echo "#################create second virtualenv#################" && echo
pyenv virtualenv 3.7.3 env1_v3.7
eval "$(pyenv init -)"
pyenv activate env1_v3.7
pyenv deactivate env1_v3.7

pyenv virtualenv 3.7.3 env2_v3.7
eval "$(pyenv init -)"
pyenv activate env2_v3.7
pyenv deactivate env2_v3.7

# 3: view created environment
echo && echo "#################view created environments#################" && echo
pyenv virtualenvs

# 4: cleanup
echo && echo "Cleaning..."
pyenv uninstall -f env1_v2.7
pyenv uninstall -f env1_v3.7
pyenv uninstall -f env2_v3.7
echo "Done!"

