#!/bin/bash
#
# Automated creation of user by providing USERNAME, COMMENT, PASSWORD on local system
# Print USERNAME, PASSWORD, and HOSTNAME after successful creation 


# Global Variables
USERNAME=""
COMMENT=""
PASSWORD=""

main() {
	sanity_check_user	
 	prompt_input_for_tokens
 	create_user
 	check_is_user_created
 	return_tokens
}

sanity_check_user() {
	if [[ ${UID} -ne 0 ]]; then
		echo 'Script must be ran as root.'
		exit 1
	fi
}

prompt_input_for_tokens() {
	echo "Please input data for the new user..."
	read -p 'Login username: ' USERNAME
	read -p 'Real name of the user: ' COMMENT
	read -p 'Initial password for the user: ' PASSWORD
}

create_user() {
	useradd ${USERNAME} -c "${COMMET}"
	echo "${PASSWORD}" | passwd --stdin $USERNAME
	passwd -e $USERNAME
}

check_is_user_created() { 
	CREATED_USER=`id -un ${USERNAME}`
	if [[ ${CREATED_USER} != ${USERNAME} ]]; then
		echo "The account was not successfully created. Exitting..."
		exit 1
	fi
}

return_tokens() {
	echo "Username: ${USERNAME} Password: ${PASSWORD} Hostname: $HOSTNAME"
}

main
