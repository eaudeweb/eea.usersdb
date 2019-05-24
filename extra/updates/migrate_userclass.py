#!/usr/bin/python2.7

import subprocess

search_users_cmd = 'ldapsearch -LLL -h {server} -s sub -D "{user_dn}" '\
    '-w {password} -x -b {base_dn} dn'
modify_cmd = 'ldapmodify -x -c -h {server} -D "{user_dn}" -w {password} '\
    '-f /tmp/out.ldiff'

operation = """{dn}
changetype: modify
add: objectClass
objectClass: eionetAccount

"""

no_limits_user_dn = "cn=Accounts Browser,o=EIONET,l=Europe"
write_access_user_dn = "cn=Eionet Administrator,o=EIONET,l=Europe"


def main(server, write_password, password):
    base_dn = "ou=Users,o=EIONET,l=Europe"

    search_cmd = search_users_cmd.format(server=server,
                                         user_dn=no_limits_user_dn,
                                         password=password, base_dn=base_dn)
    out = subprocess.Popen(search_cmd,
                           stdout=subprocess.PIPE,
                           shell=True).stdout.read()
    dns = [l for l in out.split('\n') if l.strip()]

    with open("/tmp/out.ldiff", "w") as outf:
        for dn in dns:
            if "uid=" not in dn:
                continue
            s = operation.format(dn=dn)
            outf.write(s)

    cmd = modify_cmd.format(server=server,
                            user_dn=write_access_user_dn,
                            password=write_password)
    subprocess.Popen(cmd, shell=True)   # , stdout=subprocess.PIPE, shell=True)


if __name__ == "__main__":

    server = raw_input("Enter server address: ")
    password = raw_input(
        "Enter password for user '{}': ".format(no_limits_user_dn))
    write_password = raw_input(
        "Enter password for user '{}': ".format(write_access_user_dn))

    main(server, write_password, password)
