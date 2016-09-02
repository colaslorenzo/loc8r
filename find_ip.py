import os

print "\nExecuting python script to update localhost IP...\n"

grep_gawk = "ifconfig|" + \
  "grep \"Bcast\"|" + \
  "gawk '{print $2}'|" + \
  "gawk -F\":\" '{print $2}'"

cmd = grep_gawk + " > ip_localhost.txt"
os.system(cmd)
