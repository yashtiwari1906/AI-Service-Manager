#!/bin/bash

# Open three terminals and start servers in each
chmod +x ./install_detector.sh
chmod +x ./install_verifier.sh
gnome-terminal --tab --title="detector" --command="bash -c './install_detector.sh'" \
               --tab --title="verifier" --command="bash -c './install_verifier.sh'" \

