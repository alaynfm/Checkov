from checkov.common.models.enums import CheckResult, CheckCategories
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck

class SecretManagerSecretExists(BaseResourceCheck):
    def __init__(self):
        name = "Ensure Secrets Manager secret is created"
        id = "CKV_AWS_306"
        supported_resources = ("aws_secretsmanager_secret",)
        categories = (CheckCategories.SECRETS,)
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def scan_resource_conf(self, conf):
        if "aws_secretsmanager_secret" in conf:
            return CheckResult.PASSED
        return CheckResult.FAILED

check = SecretManagerSecretExists()