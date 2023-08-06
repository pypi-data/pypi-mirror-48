# dscan

dscan makes scanning a list of domains for DNS records easy!

## Installation

Simply run:

    $ pip install dscan

## Command Reference

	usage: dscan [-h] [--input INPUT] [--output OUTPUT] [--rrtype RRTYPE]
				[--single]
				[--provider {adguard,appliedprivacy,cleanbrowsing-family,cloudflare,commons.host,dnswarden,dnswarden-adblock,google,powerdns,quad9}]
				[--verbose]
				[domain]

	positional arguments:
	domain                domain name (single mode only)

	optional arguments:
	-h, --help            show this help message and exit
	--input INPUT, -i INPUT
							path to list of domains (in plain text)
	--output OUTPUT, -o OUTPUT
							path to output
	--rrtype RRTYPE, -r RRTYPE
							rrtype to collate
	--single, -s          single domain mode
	--provider {adguard,appliedprivacy,cleanbrowsing-family,cloudflare,commons.host,dnswarden,dnswarden-adblock,google,powerdns,quad9}, -p {adguard,appliedprivacy,cleanbrowsing-family,cloudflare,commons.host,dnswarden,dnswarden-adblock,google,powerdns,quad9}
							dns provider to use
	--verbose, -v         increase output verbosity

## License

This project has been developed by Matthew Gall. This project is hereby released under the terms of the MIT License, and is included below

	MIT License

	Copyright (c) 2019 Matthew Gall

	Permission is hereby granted, free of charge, to any person obtaining a copy
	of this software and associated documentation files (the "Software"), to deal
	in the Software without restriction, including without limitation the rights
	to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
	copies of the Software, and to permit persons to whom the Software is
	furnished to do so, subject to the following conditions:

	The above copyright notice and this permission notice shall be included in all
	copies or substantial portions of the Software.

	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
	IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
	FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
	AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
	LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
	OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
	SOFTWARE.

## Support

Have a question? Need assistance? Don't stay stuck! If you do use this project or have any feedback we would love to hear from you, drop me an [e-mail](mailto:hello@matthewgall.com)