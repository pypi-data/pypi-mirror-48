# httpie-xsisip

[httpie](https://httpie.org/) Broadsoft authentication plugin to use XSI-SIP (BroadWorksSIP) authentication

## Installation

```
$ pip install httpie-xsisip
```

You should now see `xsisip` under `--auth-type` in `$ http --help` output.

## Usage

```
$ http --auth-type=xsisip -a "XSI_ACCOUNT:SIP_ACCOUNT:SIP_PASSWORD" https://xsi-server.example.com/com.broadsoft.xsi-actions/v2.0/versions
```
