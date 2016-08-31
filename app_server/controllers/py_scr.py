import os
import os.path

print "\nExecuting python script to update localhost IP...\n"

grep_gawk = "ifconfig|" + \
  "grep \"Bcast\"|" + \
  "gawk '{print $2}'|" + \
  "gawk -F\":\" '{print $2}'"

cmd = grep_gawk + " > ip_localhost.txt"
os.system(cmd)

if not os.path.exists("stored_ip.txt"):
  # the simplest way to continue the flow is to create the missing file:
  cmd = "touch stored_ip.txt"
  os.system(cmd)

cmd = "diff ip_localhost.txt stored_ip.txt > diff.txt"
os.system(cmd)

with open('ip_localhost.txt', "r") as f_in:
  for line in f_in:
    ip = line.strip()

def delete_diff_file():
  cmd = "rm diff.txt"
  os.system(cmd)

with open("diff.txt", "r") as f:
  print "Current localhost IP:\n" + ip + "\n"
  for line in f:
    break # file is not empty, therefore there are differences
  else:
    #print "\nthere are NOT differences\n"
    delete_diff_file()
    exit() # nothing else to do

delete_diff_file()

cmd = "cp ip_localhost.txt stored_ip.txt"
os.system(cmd)

sed_cmd = "'s,  server: \\\"http://192\\.168\\..*\\..*:3000," + \
  "  server: \\\"http://" + ip + ":3000,g'"

cmd = "sed -e " + sed_cmd + " locations.js > out.txt"
os.system(cmd)

cmd = "mv out.txt locations.js"
os.system(cmd)
