import os

print "\nExecuting python script to update localhost IP...\n"

grep_gawk = "ifconfig|" + \
  "grep \"Bcast\"|" + \
  "gawk '{print $2}'|" + \
  "gawk -F\":\" '{print $2}'"

cmd = grep_gawk + " > ip_localhost.txt"
os.system(cmd)

with open('ip_localhost.txt', "r") as f_in:
  for line in f_in:
    ip = line.strip()

sed_cmd = "'s,  server: \\\"http://192\\.168\\..*\\..*:3000," + \
  "  server: \\\"http://" + ip + ":3000,g'"

cmd = "sed -e " + sed_cmd + " locations.js > out.txt"
os.system(cmd)
cmd = "mv out.txt locations.js"
os.system(cmd)
