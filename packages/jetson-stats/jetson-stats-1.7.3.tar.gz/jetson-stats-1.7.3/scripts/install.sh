#!/bin/bash
# Copyright (C) 2019, Raffaello Bonghi <raffaello@rnext.it>
# All rights reserved
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright 
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
# 3. Neither the name of the copyright holder nor the names of its 
#    contributors may be used to endorse or promote products derived 
#    from this software without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND 
# CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, 
# BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS 
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, 
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; 
# OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, 
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE 
# OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, 
# EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

BIN_FOLDER="/usr/local/bin"

uninstaller_old_bin()
{
    # Remove jetson_release link
    if [ -f "$BIN_FOLDER/jtop" ] ; then
        echo "   * Remove jtop link"
        sudo rm "$BIN_FOLDER/jtop"
    fi
    
    # Remove jetson_release link
    if [ -f "$BIN_FOLDER/jetson_release" ] ; then
        echo "   * Remove jetson_release link"
        sudo rm "$BIN_FOLDER/jetson_release"
    fi

    # Remove jetson_swap link
    if [ -f "$BIN_FOLDER/jetson_swap" ] ; then
        echo "   * Remove jetson_swap link"
        sudo rm "$BIN_FOLDER/jetson_swap"
    fi

    # Remove jetson-docker link
    if [ -f "$BIN_FOLDER/jetson-docker" ] ; then
        echo "   * Remove jetson-docker link"
        sudo rm "$BIN_FOLDER/jetson-docker"
    fi
}

disable_service()
{
    # Remove the service from /etc/init.d
    if [ -f "/etc/systemd/system/jetson_performance.service" ] ; then
        # Uninstall the service
        if [ $(systemctl is-active jetson_performance.service) = "active" ] ; then
            tput setaf 1
            echo "   * Stop and jetson_performance service"
            tput sgr0
            # Stop the service
            sudo systemctl stop jetson_performance.service
        fi
        # Disable the service
        echo "   * Disable service from /etc/systemd/system"
        sudo systemctl disable jetson_performance.service
    fi
}

uninstaller_bin()
{
    # Remove the service from /etc/init.d
    if [ -f "/etc/systemd/system/jetson_performance.service" ] ; then
        # Remove service
        sudo systemctl disable jetson_performance.service
        echo "   * Remove the service from /etc/systemd/system"
        sudo rm "/etc/systemd/system/jetson_performance.service"
    fi
    # Update service list
    sudo systemctl daemon-reload

    # Remove from bashrc jetsonstat variables
    if [ -f "/etc/profile.d/jetson_env.sh" ] ; then
        echo "   * Remove the jetson_env.sh from /etc/profile.d/"
        sudo rm "/etc/profile.d/jetson_env.sh"
    fi
}

uninstaller()
{
    local JETSON_FOLDER=$1
    
    echo " - Uninstall jetson_stats on $JETSON_FOLDER"
    # Remove configuration
    if [ -f $JETSON_FOLDER/l4t_dfs.conf ] ; then
        echo "   * Remove the jetson_clock.sh configuration"
        sudo rm $JETSON_FOLDER/l4t_dfs.conf
    fi

    # remove folder
    echo "   * Remove jetson_easy folder"
    sudo rm -r $JETSON_FOLDER
}

installer()
{
    local FORCE_INSTALL=$1
    
    # Launch installer pip
    if $FORCE_INSTALL ; then
        sudo -H pip install -U -e .
    else
        sudo -H pip install -e .
    fi
}

installer_bin()
{
    local JETSON_FOLDER=$1
    
    sudo mkdir -p "$1" 
    
    echo "   * Copy jetson_variables and jetson_performance"
    sudo cp "scripts/jetson_variables" "/opt/jetson_stats/jetson_variables"
    sudo cp "scripts/jetson_performance.sh" "/opt/jetson_stats/jetson_performance.sh"
    
    echo "   * Copy jetson_env.sh in /etc/profile.d/"
    sudo cp "scripts/jetson_env.sh" "/etc/profile.d/jetson_env.sh"
    
    echo "   * Copy jetson_variables and other scripts"
    sudo cp "scripts/jetson_performance.service" "/etc/systemd/system/jetson_performance.service"
}

usage()
{
	if [ "$1" != "" ]; then
    	tput setaf 1
		echo "$1"
		tput sgr0
	fi
	
    echo "Jetson_stats, Installer for nvidia top and different information modules."
    echo "Usage:"
    echo "$0 [options]"
    echo "options,"
    echo "   -h|--help    | This help"
    echo "   -s|--silent  | Run jetson_stats in silent mode"
    echo "   -i|--inst    | Change default install folder"
    echo "   -f|--force   | Force install all tools"
    echo "   --uninstall  | Run the uninstaller"
    echo "   -no-bin      | NOT Install this binaries fiels"
    echo "   -no-pip      | NOT Install this repository with pip"
    echo "   -test        | Install test files"
    echo "   -auto        | Run at start-up jetson performance"

}

main()
{
    local SKIP_ASK=true
    local AUTO_START=false
    local FORCE_INSTALL=false
    local START_UNINSTALL=false
    local JETSON_FOLDER="/opt/jetson_stats"
    local THIS_FOLDER=true
    local INSTALL_BIN=true
    local TEST_FILES=false
    
	# Decode all information from startup
    while [ -n "$1" ]; do
        case "$1" in
            -i|--inst)
                JETSON_FOLDER=$2
                shift 1
                ;;
            -s|--silent)
                SKIP_ASK=false
                ;;
            -f|--force)
                FORCE_INSTALL=true
                ;;
            --uninstall)
                START_UNINSTALL=true
                ;;
            -no-bin)
                INSTALL_BIN=false
                ;;
            -test)
                TEST_FILES=true
                ;;
            -auto)
                AUTO_START=true
                ;;
            -no-pip)
                THIS_FOLDER=false
                ;;
            -h|--help)
                # Load help
                usage
                exit 0
                ;;
            *)
                usage "[ERROR] Unknown option: $1"
                exit 1
            ;;
        esac
            shift 1
    done

    if [ $(basename $(pwd)) == "scripts" ] ; then
        tput setaf 1
        echo "Please run in home project"
        tput sgr0
        exit 1
    fi    

    if [[ `id -u` -ne 0 ]] ; then 
        tput setaf 1
        echo "Please run as root"
        tput sgr0
        exit 1
    fi
	
	local install_uninstall_string="install"
	if $START_UNINSTALL ; then
        install_uninstall_string="uninstall"
    fi
	
    while $SKIP_ASK; do
        read -p "Do you wish to $install_uninstall_string jetson_stats? [Y/n] " yn
            case $yn in
                [Yy]* ) # Break and install jetson_stats 
                        break;;
                [Nn]* ) exit;;
            * ) echo "Please answer yes or no.";;
        esac
    done
    
    if $START_UNINSTALL ; then
        tput setaf 3
        echo "Uninstaller jetson-stats"
        tput sgr0
    
        # Run uninstaller binaries
        disable_service
        
        # remove old configurations
        if [ -d /etc/jetson_easy ] && ! $TEST_FILES ; then
            uninstaller_old_bin
            uninstaller /etc/jetson_easy
        fi
        
        if $THIS_FOLDER && ! $TEST_FILES ; then
            # Remove configuration standard
            if [ -d "$JETSON_FOLDER" ] ; then
                uninstaller_bin
                uninstaller $JETSON_FOLDER
            fi
        fi
        
        if $TEST_FILES ; then
            # Remove tegrastats
            if [ -f /usr/bin/tegrastats ] ; then
                echo " - Remove /usr/bin/tegrastats"
                sudo rm /usr/bin/tegrastats
            else
                echo " - /usr/bin/tegrastats does not exist"
            fi
            # Remove nvpmodel
            if [ -f /usr/bin/nvpmodel ] ; then
            echo " - Remove /usr/bin/nvpmodel"
                sudo rm /usr/bin/nvpmodel
            else
                echo " - /usr/bin/nvpmodel does not exist"
            fi
            # Remove jetson_clock
            if [ -f /usr/bin/jetson_clocks ] ; then
            echo " - Remove /usr/bin/jetson_clocks"
                sudo rm /usr/bin/jetson_clocks
            else
                echo " - /usr/bin/jetson_clocks does not exist"
            fi
        fi
    else
        # ---------------------------------------------------------------
        #                INSTALLER
        # ---------------------------------------------------------------
        tput setaf 3
        echo "Installer jetson-stats"
        tput sgr0
        
        if $FORCE_INSTALL ; then
            tput setaf 4
            echo "Force install"
            tput sgr0
        fi
        
        if $THIS_FOLDER && ! $TEST_FILES ; then
            # Run installer
            installer $FORCE_INSTALL
        fi
        
        if $INSTALL_BIN && ! $TEST_FILES ; then
            installer_bin $JETSON_FOLDER
        fi
        
        if $TEST_FILES ; then
            # tegrastats emulator
            if [ ! -f /usr/bin/tegrastats ] || $FORCE_INSTALL ; then
                echo " - Copy emulation tegrastats in /usr/bin/"
                sudo cp tests/tegrastats /usr/bin/
            else
                echo " - Already exist tegrastats in /usr/bin/"
            fi
            # nvpmodel emulator
            if [ ! -f /usr/bin/nvpmodel ] || $FORCE_INSTALL ; then
            echo " - Copy emulation nvpmodel in /usr/bin/"
                sudo cp tests/nvpmodel /usr/bin/
            else
                echo " - Already exist nvpmodel in /usr/bin/"
            fi
            # jetson_clock
            if [ ! -f /usr/bin/jetson_clocks ] || $FORCE_INSTALL ; then
            echo " - Copy emulation jetson_clocks in /usr/bin/"
                sudo cp tests/jetson_clocks /usr/bin/
            else
                echo " - Already exist jetson_clocks in /usr/bin/"
            fi
        fi
        
        # Update service list
        sudo systemctl daemon-reload
        
        if $AUTO_START ; then
            tput setaf 4
            echo " - Enable and start jetson_performance"
            tput sgr0
            # Enable service
            sudo systemctl enable jetson_performance.service
            # Run the service
            sudo systemctl start jetson_performance.service
        fi
    fi
    
    tput setaf 2
    echo "DONE!"
    tput sgr0
}


main $@
exit 0

#EOF
