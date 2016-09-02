import os
import argparse

parser = argparse.ArgumentParser(description="Caller to local web server. Withouth arguments, it calls heroku local")
parser.add_argument('-n', '--nodemon', action='store_true')
parser.add_argument('-p', '--production', action='store_true')
args = parser.parse_args()

with open('ip_localhost.txt', "r") as f_in:
  for line in f_in:
    ip = line.strip()

cmd = "rm ip_localhost.txt"
os.system(cmd)

print "Current IP localhost:"
print ip + "\n"

if args.nodemon:
  print "nodemon provided\n"
  cmd = "NODE_ENV=\"http://" + ip + ":3000\" nodemon"
elif args.production:
  print "production provided\n"
  cmd = "NODE_ENV=production nodemon"
else:
  print "heroku selected by default\n"
  cmd = "NODE_ENV=\"http://" + ip + ":5000\" heroku local"

os.system(cmd)
