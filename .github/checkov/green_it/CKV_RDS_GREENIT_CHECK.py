# .github/checkov/custom_rules/rds_green_it_check.py

from checkov.common.models.enums import CheckResult, CheckCategories
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck
import re

class RDSGreenITCheck(BaseResourceCheck):
    def __init__(self):
        name = "Ensure RDS instances use energy-efficient instance types"
        id = "CUSTOM_RDS_GREEN_IT_1"
        supported_resources = ['aws_db_instance']
        categories = [CheckCategories.GENERAL_SECURITY]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def scan_resource_conf(self, conf):
        # Allowed RDS instance types for Green IT
        allowed_instance_types = [
            "db.t3.micro",
            "db.t3.small",
            "db.t3.medium",
            "db.t3.large",
            "db.t3.xlarge",
            "db.t3.2xlarge",
            # Add other energy-efficient instance types as needed
        ]

        if 'instance_class' in conf:
            instance_class = conf['instance_class'][0] if isinstance(conf['instance_class'], list) else conf['instance_class']
            if instance_class in allowed_instance_types:
                return CheckResult.PASSED
            else:
                return CheckResult.FAILED

        # If instance_class is not defined, consider it as failed
        return CheckResult.FAILED

check = RDSGreenITCheck()