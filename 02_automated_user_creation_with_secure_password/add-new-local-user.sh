#!/bin/bash
#
# Automated creation of user by providing USERNAME. Optinally, a COMMENT can be also provide
# PASSWORD for the user will be automatically created.
# Print USERNAME, PASSWORD, and HOSTNAME after successful creation 


# Global Variables
USERNAME=""
COMMENT=""
PASSWORD=""
COUNT_OF_ARGS="${#}"

main() {
	sanity_check_user	
	sanity_check_params "$@"
	prepare_arguments "$@"
	generate_password
 	create_user
 	check_is_user_created_by_status
	force_password_change_on_first_login
 	return_tokens
}

sanity_check_user() {
	if [[ ${UID} -ne 0 ]]; then
		echo 'Script must be run as root.' 1>&2  
		exit 1
	fi
}

sanity_check_params() {
	if [[ "${COUNT_OF_ARGS}" -lt 1 ]]; then
		echo "Usage: ${0} USERNAME [COMMENT]" 1>&2
		echo 'Create an account on the local system with the name of USERNAME and a comments filled of COMMENT.' 1>&2
		exit 1
	fi
}

prepare_arguments() {
	USERNAME="${1}"
	shift
	COMMENT="${*}"

}

generate_password() {
	SPECIAL_CHARACTERS=$(echo '!@#$%^&*()-_=+' | fold -w1 | shuf | head -c1)
	HASH_CHARACTERS=$(date +%s%N | sha256sum | head -c15)
	PASSWORD="${HASH_CHARACTERS}${SPECIAL_CHARACTERS}"
}

create_user() {
	useradd -c "${COMMENT}" -m ${USERNAME} 2&>1 /dev/null
	echo "${PASSWORD}" | passwd --stdin "${USERNAME}" 2>&1 /dev/null
}

check_is_user_created_by_status() { 
	if [[ "${?}" -ne 0 ]]; then
		echo "The account could not have been created. Exiting..." 1>&2
		exit 1
	fi
}

force_password_change_on_first_login() {
	passwd -e "${USERNAME}" 2>&1 /dev/null
}

return_tokens() {
	echo "||||||||||||||"
	echo "Username:"
	echo "${USERNAME}"
	echo "--------------"
	echo "Password:"
	echo "${PASSWORD}"
	echo "--------------"
	echo "Hostname"
	echo "${HOSTNAME}"
	echo "||||||||||||||"
}

main "$@"
exit 0
