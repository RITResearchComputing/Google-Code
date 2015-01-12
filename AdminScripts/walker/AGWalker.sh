#!/bin/bash
# Walking program to execute commands across multiple linux nodes
# using SSH connections

function printhelp {
	echo "Usage: ./AGWalker -c walk.cmd -l walk.list"
	echo ""
	echo "Script runs the provided script at each of the nodes on the provided list of nodes"
	echo "-h	print out help"
	echo "-c	pass in script to run"
	echo "-l 	pass in list of nodes"

}
function walker {
	#read in list of nodes to walk
	echo "#######################"
	echo "Reading $Nodes"
	n=0
	while read line
	do
        	nodes[$n]=$line
        	#echo "$n = $line"
        	n=$[$n + 1]
	done < $Nodes
	#echo ${nodes[*]}
	echo "#######################"
	echo "Done reading $Nodes"

#read in command list
#echo "Reading $Cmds"
#c=0
#while read line
#do
#       cmd[$c]=$line
#       echo "$c = $line"
#       c=$[$c + 1]
#done < $Cmds
#echo ${cmd[*]}
#echo "Done reading $Cmds"


	#iterate through list of nodes
	echo "#######################"
	echo "Starting to walk..."
	for node in ${nodes[@]}
	do

	        echo "-----------------------------------------"
	        echo "-----------------------------------------"
	        echo "Running for $node"
	        echo "----------------------"
	        #ssh ${node}
	        scp $Cmds ${node}:/root/$Cmds
	        #for (( command = 0 ; command < ${#cmd[@]} ; command++ ))
	        #do
	        #       ssh ${node} "${cmd[$command]}"
	        #done
	        ssh ${node} "bash /root/$Cmds"
	        ssh ${node} "rm /root/$Cmds"

	        #exit
	done
	echo "#######################"
	echo "Finished walking."
	echo "#######################"
}
Nodes=""
Cmds=""
while [ $# -gt 0 ]
do
	case $1
	in

	-h)
		#print useage information
		printhelp
		exit
	;;
	-l)
		#filename of list of nodes
		Nodes=$2
		shift 2
	;;
	-c)
		#filename for script to run
		Cmds=$2
		shift 2
	;;
	esac
done
LOG=AGWalker-$(date +%Y%m%d-%H:%M)
walker 2>&1 | tee -a /var/log/AGWalker/$LOG.log
