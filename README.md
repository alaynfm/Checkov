# Pipeline for IaC (Infrastructure as Code)

Welcome to the Infrastructure Deployment Laboratory! It is only a test !!

This laboratory is designed to ensure the correct deployment of infrastructure using diffrents tools for both AWS and Azure clouds. 

## Branch Strategy

Before any code changes are merged into the `main` branch, the branch strategy ensures that all necessary checks and validations are performed. This process helps maintain the integrity and stability of the production code. Here's how it works:

1. **Development in `dev` Branch**: All new features, bug fixes, and updates are first developed in the `dev` branch. This branch is used for ongoing development and integration.

2. **Static Analysis**: When changes are committed to the `dev`, static analysis tools (like TFLint, Checkov, TFSec, and Infracost) are triggered to check the code for errors, security vulnerabilities, and cost implications. Any issues identified must be resolved before proceeding.

3. **Merge Request**: Once the code in the `dev` branch is stable and passes all static analysis checks, a merge request is created to merge these changes into the `main` branch.

4. **Dynamic Analysis**: Before the merge is completed, dynamic analysis tools (like Terraform Plan, Checkov over the Terraform plan output, Terratest, and Apply) are run to test the code in a runtime environment. This ensures that the code not only passes static checks but also works correctly when executed.

5. **Review and Approval**: The results of the dynamic analysis are reviewed. If all tests pass and no issues are found, the merge request is approved.

6. **Merge to `main`**: After approval, the changes are merged into the `main` branch. This branch contains production-ready code that has been thoroughly tested and validated.

Applying changes before merging into the `main` branch offers several advantages:

1. **Early Detection**: Identifies issues early, preventing them from reaching production.
2. **Stability**: Ensures `main` branch remains stable and production-ready.
3. **Streamlined Review**: Simplifies the review process by ensuring all checks are passed.
4. **Preventing Rework**: Reduces the need for rework by catching issues early.
5. **Collaboration**: Encourages team collaboration and continuous improvement.
6. **Compliance**: Ensures adherence to security and compliance standards.

By following this branch strategy, the laboratory ensures that only high-quality, stable, and secure code is deployed to production. This process helps catch and fix issues early, reducing the risk of problems in the live environment.

## Github Actions

Two different pipelines will be exuted:


1. **Static Analysis**: This analysis checks the code for errors and potential issues without executing it. It is triggered on the `dev` branch.
   - **TFLint**: A linter for Terraform configurations that identifies potential issues and enforces best practices.
   - **Checkov**: Scans infrastructure as code (IaC) files for security and compliance misconfigurations.
   - **TFSec**: A security scanner for Terraform code that identifies vulnerabilities and misconfigurations.
   - **Infracost**: Provides cloud cost estimates for Terraform code, helping to understand the financial impact of infrastructure changes.
   - **Results**: Aggregates and reviews the outputs from the static analysis tools to ensure all issues are documented and addressed.

2. **Dynamic Analysis**: This analysis tests the code by executing it in a runtime environment. It is triggered when a merge is done from the `dev` branch to the `main` branch.

    - **Terraform Plan**: Generates an execution plan, showing what actions Terraform will take to achieve the desired state of the infrastructure.
   - **Checkov**: Runs over the output of the Terraform plan to identify any security or compliance issues in the planned changes.
   - **Terratest**: Executes automated tests to validate the infrastructure code by deploying it in a real environment and running various checks.
   - **Apply**: Applies the Terraform plan to provision the infrastructure in the target environment.
