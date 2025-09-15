
# AWS Lambda Boto3 Policy

This repository contains AWS Lambda functions for managing EBS resources using the Boto3 library. The main scripts automate EBS snapshot cleanup and volume type modification.

## Contents

- `delete_snapshots.py`: Lambda function to delete unused EBS snapshots.
- `volume_type.py`: Lambda function to change EBS volume type to `gp3`.

## Examples

### Delete Unused Snapshots

Automatically deletes EBS snapshots that are not attached to any volume or whose associated volume is not attached to a running instance.

```python
# Example event for Lambda
def lambda_handler(event, context):
	# ...existing code...
```

### Modify EBS Volume Type

Changes the type of an EBS volume to `gp3` using a volume ARN or ID.

```python
# Example event for Lambda
{
	"resources": ["arn:aws:ec2:region:account-id:volume/vol-1234567890abcdef0"]
}
```

## How and Why We Write Use Cases

**Writing use cases** involves describing specific scenarios in which a system or function is used. In this project, use cases help define the automation goals, such as cleaning up unused EBS snapshots or standardizing volume types. Well-written use cases:

- Clarify requirements and expected outcomes.
- Guide development and testing.
- Ensure alignment with organizational policies and compliance.

**Why we write use cases:**

- To automate repetitive cloud management tasks, reducing manual effort and risk of human error.
- To enforce resource optimization and cost savings by removing unused resources.
- To maintain compliance and security by ensuring only necessary resources are retained.

**Impact to the Organization:**

- **Cost Efficiency:** Automated cleanup of unused resources directly reduces AWS costs.
- **Operational Excellence:** Standardizing resource types and automating management improves reliability and scalability.
- **Security & Compliance:** Ensures only required resources are retained, reducing attack surface and supporting audit requirements.
- **Developer Productivity:** Frees up engineering time for innovation by reducing manual cloud maintenance.

## Future Use Cases

- Automate additional EBS lifecycle management tasks.
- Integrate with AWS EventBridge for real-time resource management.
- Extend to other AWS resources (e.g., S3, RDS).

## Official Documentation

- [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)
- [Boto3 EC2 Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html)

## Further Improvements

- Add unit and integration tests.
- Implement logging and error handling.
- Support for multi-region resource management.
- Add configuration via environment variables.

## Test Cases

### delete_snapshots.py
- Should delete snapshots not attached to any volume.
- Should delete snapshots whose volume is not attached to a running instance.
- Should skip snapshots attached to volumes in use by running instances.
- Should handle missing or invalid snapshot/volume IDs gracefully.

### volume_type.py
- Should modify volume type to `gp3` for valid volume IDs/ARNs.
- Should return error if no volume ID is found in the event.
- Should handle AWS API errors (e.g., permission denied, invalid volume).

## Anticipated Errors in Implementation

- AWS permission errors (missing IAM roles/policies).
- Invalid or missing resource IDs/ARNs in event payloads.
- API rate limits or throttling from AWS.
- Network connectivity issues.
- Lambda timeout or memory limits exceeded.

## Troubleshooting Steps

1. Check Lambda execution role for required EC2 permissions.
2. Validate event payload structure and required fields.
3. Review CloudWatch logs for error messages and stack traces.
4. Test with sample events in the Lambda console.
5. Ensure Boto3 and AWS SDK versions are up to date.

## Common Mistakes

- Not granting sufficient permissions to Lambda execution role.
- Incorrect event payload format (missing `resources` or `volumeId`).
- Hardcoding resource IDs instead of using event data.
- Not handling exceptions from Boto3 API calls.
- Ignoring AWS region configuration.

## Recommended Approach

- Always validate input event data before processing.
- Use try/except blocks to handle Boto3 and AWS errors.
- Log all actions and errors for traceability.
- Test Lambda functions with various event scenarios.
- Use environment variables for configuration and secrets.
