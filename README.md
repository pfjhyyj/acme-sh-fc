# acme sh fc

## Description
This repo aim to use [acme.sh](https://github.com/acmesh-official/acme.sh) in Aliyun FC to issue/renew the certificates of fc with dns-01 challenge.

## Prerequisite
- Clone this repo with --recurse-submodules
- An account with access key in aliyun, with FCFullAccess and DNSFullAccess
- Your email address (to apply for a certificate)
- FC Python3.9 runtime
- Add Layer alibabacloud_fc_open20210406

## Environment Variables
- Ali_Key
- Ali_Ali_Secret
- ACCOUNT_EMAIL
- End_Point (ACCOUNT-ID.REGION_NAME.fc.aliyuncs.com)
- Domain (*.example.com)

## Tips
End of line should be CRLF