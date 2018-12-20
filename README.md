# Shodan_Recon

Takes a set of IPs and performs recon to get domain names associated with the IP. Especially useful for when there is no reverse-dns record set.

## Why?

There are lots of times in a bug-bounty or a red-team pentest that you may be given a load of external IP ranges and you may want to investigate the web applications hosted on the servers. 

Sometimes the IP address will not directly resolve to the web app and may require a domain name. That is where this tool may come in handy, especially when there is no PTR (Reverse DNS) record.

## Usage 

You will need a Shodan API key and add it into the `shodanrecon.py` on the line:
```
SHODAN_API_KEY = ""
```

* `pip install -r requirements.txt`
* `python ./shodanrecon.py targets.txt`

The script will write to two files: errors.txt and results.txt. 

`errors.txt` will show any errors which may have occured throughout the scan.

`results.txt` will be the findings from the scan.

## Want to help?

Just submit a pull-request or add an issue :)

