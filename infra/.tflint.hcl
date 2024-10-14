plugin "aws" {
    enabled = true
    version = "0.33.0"
    source  = "github.com/terraform-linters/tflint-ruleset-aws"
}

# .tflint.hcl file
rule "terraform_naming_convention" {
  enabled = true
# Module names must start with 'aws' and can contain lowercase letters and digits only.
  module{
    custom = "^aws_[a-z0-9_]*$" 
  }
# Resource names must start with a lowercase letter, end with a lowercase letter, and contain only lowercase letters and underscores.
  resource {
    custom = "^[a-z]([a-z_]*[a-z])?$"
  }
# Resource names must start with a lowercase letter, end with a lowercase letter, and contain only lowercase letters and underscores.
  output {
    custom = "^[a-z]([a-z_]*[a-z])?$"
  }
# Resource names must start with a lowercase letter, end with a lowercase letter, and contain only lowercase letters and underscores.
  variable {
    custom = "^[a-z]([a-z_]*[a-z])?$"
  }
}

