#!/bin/bash
 
# ************* Setting the Environment ***********************
$WL_HOME/server/bin/. ./setWLSEnv.sh

#DOMAIN_HOME="/u01/Oracle/Middleware/Oracle_Home/user_projects/domains/mega_domain"
$DOMAIN_HOME/bin/./setDomainEnv.sh $*
 
echo "Environment has been set....."
 
# ************* Changing the directory where all the related files are needed ***********************
cd /tmp
 
echo "Calling the PYTHON script....."
fecha=$(date +"%d-%b-%y_%H%M%S")
 
# ************* Calling the WLST script  *****************
java weblogic.WLST restartDomain.py > /tmp/restartDomain_$fecha.log

# send an email using /bin/mail
/bin/mail -s "Notificacion de reinicio" "galo.coloma@gmail.com" < /tmp/restartDomain_$fecha.log