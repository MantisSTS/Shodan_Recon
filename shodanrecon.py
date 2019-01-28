from __future__ import print_function
import sys
import json
import shodan 
import time

class Recon:
    api = None
    results = ""
    def __init__(self):
        SHODAN_API_KEY = ""
        self.api = shodan.Shodan(SHODAN_API_KEY)

    def do_lookup(self, ip):
        try:
            time.sleep(0.6)
            # dt = self.api.host(str(ip))
            dt = self.api.search("net:" + str(ip))
            for match in dt['matches']:
                if 'hostnames' in match:
                    for host in match['hostnames']:
                        if host != "":
                            self.results += host + "\n"
                if 'domains' in match:
                    for domain in match['domains']:
                        if domain != "":
                            self.results += domain + "\n"  
                if 'ssl' in match:
                    new = match['ssl']['cert']['subject']['CN'].encode("UTF-8")               
                    self.results += new + "\n"

        except Exception as e:
            print(str(e))
            f = open('errors.txt', "a+")
            f.write(str(e))
            f.close
            pass
        return self.results

    def main(self):
        hosts_file = sys.argv[1]
        f = open('results.txt', 'w+')
        with open(hosts_file, 'r') as lines:        
            for line in lines:
                print('Looking up IP: ' + str(str(line)))
                res = self.do_lookup(str(line))
                f.write(res)
        f.close()
        return self.results

def main():
    a = Recon()
    a.main()

if __name__ == '__main__':
    main()