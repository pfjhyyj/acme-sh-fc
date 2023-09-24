# -*- coding: utf-8 -*-
import os
import sys

from typing import List
from datetime import datetime

from alibabacloud_fc_open20210406.client import Client as FC_Open20210406Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_fc_open20210406 import models as fc__open_20210406_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient


def handler(event, context):
    RenewCertificate.main(sys.argv[1:])
    return "RenewCertificate Success"

class RenewCertificate:
    def __init__(self):
        pass

    @staticmethod
    def create_client(
        access_key_id: str,
        access_key_secret: str,
    ) -> FC_Open20210406Client:
        config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret
        )
        config.endpoint = os.environ['End_Point']
        return FC_Open20210406Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        domain = os.environ['Domain']
        command = f"./acme.sh/acme.sh --issue --dns dns_ali -d {domain} --keylength 4096 --cert-file cert.cer --key-file cert.key"
        os.system(command)

        certFile = open("./cert.cer", "r")
        keyFile = open("./cert.key", "r")
        cert = certFile.read()
        key = keyFile.read()
        certFile.close()
        keyFile.close()

        client = RenewCertificate.create_client(os.environ['Ali_Key'], os.environ['Ali_Secret'])
        update_custom_domain_headers = fc__open_20210406_models.UpdateCustomDomainHeaders()
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        certName = f"certificate-{timestamp}"
        cert_config = fc__open_20210406_models.CertConfig(
            cert_name=certName,
            certificate=cert,
            private_key=key
        )
        update_custom_domain_request = fc__open_20210406_models.UpdateCustomDomainRequest(
            protocol='HTTPS',
            cert_config=cert_config
        )
        runtime = util_models.RuntimeOptions()
        try:
            client.update_custom_domain_with_options(domain, update_custom_domain_request, update_custom_domain_headers, runtime)
        except Exception as error:
            UtilClient.assert_as_string(error.message)
            print(error)
            raise


if __name__ == '__main__':
    RenewCertificate.main(sys.argv[1:])
