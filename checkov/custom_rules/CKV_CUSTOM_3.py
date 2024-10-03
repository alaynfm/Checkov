from checkov.common.models.enums import CheckResult, CheckCategories
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck

class SecretManagerSecretRotation(BaseResourceCheck):
    def __init__(self):
        name = "Ensure Secrets Manager secrets have rotation enabled"
        id = "CKV_CUSTOM_3"
        supported_resources = ("aws_secretsmanager_secret",)
        categories = (CheckCategories.SECRETS,)
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def scan_resource_conf(self, conf):
        if "aws_secretsmanager_secret" in conf:
            secret_id = conf["aws_secretsmanager_secret"]["id"]
            rotation_resources = conf.get("aws_secretsmanager_secret_rotation", [])
            for rotation in rotation_resources:
                if rotation.get("secret_id") == secret_id:
                    return CheckResult.PASSED
            return CheckResult.FAILED
        return CheckResult.UNKNOWN

check = SecretManagerSecretRotation()
