import logging
from checkov.common.models.enums import CheckResult, CheckCategories
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck

class RDSPostgreSQLPGAuditEnabled(BaseResourceCheck):
    def __init__(self):
        name = "Ensure PostgreSQL RDS instances have PGAudit enabled"
        id = "CKV_CUSTOM_2"
        supported_resources = ["aws_db_parameter_group"]
        categories = [CheckCategories.SECURITY]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def scan_resource_conf(self, conf):
        """
        Looks for the pgaudit.log parameter in the db parameter group to ensure it's set and enabled.
        """
        # Logging for debugging purposes
        logging.info(f"Scanning resource: {conf}")

        # Check if pgaudit.log is set to "all"
        if 'parameter' in conf:
            for param in conf['parameter']:
                if param['name'] == 'pgaudit.log' and param['value'] == 'all':
                    logging.info("PGAudit is enabled")
                    return CheckResult.PASSED
        
        logging.info("PGAudit is not enabled")
        return CheckResult.FAILED

check = RDSPostgreSQLPGAuditEnabled()
