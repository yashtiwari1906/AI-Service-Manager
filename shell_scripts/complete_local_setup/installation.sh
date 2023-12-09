#!/bin/bash

# Open three terminals and start servers in each
chmod +x ./install_detector.sh
chmod +x ./install_verifier.sh
chmod +x ./service_manager_installation.sh
chmod +x ./db_installation.sh
chmod +x ./configure_db.sh
gnome-terminal --tab --title="postgres-installer" --command="bash -c './db_installation.sh'" \
	       --tab --title="cofigure-postgres" --command="bash -c './configure_db.sh'" \
	       --tab --title="detector" --command="bash -c './install_detector.sh'" \
               --tab --title="verifier" --command="bash -c './install_verifier.sh'" \
--tab --title="service_manager" --command="bash -c './service_manager_installation.sh'" \

