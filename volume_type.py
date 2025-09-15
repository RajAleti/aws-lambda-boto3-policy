import boto3
import os

def get_volume_id_from_arn(volume_arn):
    # Split the arn using ":" operator
    arn_parts = str(volume_arn).split(':')
    # Volume id is the last part of arn after the "volume/" prefix
    volume_id = arn_parts[-1].split('/')[-1]
    return volume_id

def lambda_handler(event, context):
    # Prefer EBS Volume Notification shape: resources[0]
    volume_id = None
    resources = event.get('resources')
    if isinstance(resources, list) and resources:
        volume_id = get_volume_id_from_arn(resources[0])
    else:
        # Simple fallbacks for test/custom events
        volume_id = (
            event.get('volumeId')
            or event.get('volume_id')
            or event.get('detail', {}).get('volume-id')
            or event.get('detail', {}).get('requestParameters', {}).get('volumeId')
            or os.getenv('DEFAULT_VOLUME_ID')
        )

    if not volume_id:
        return {
            "error": "No volume ID found",
            "hint": "Provide 'resources[0]' with a volume ARN or a 'volumeId' field."
        }

    ec2_client = boto3.client('ec2')
    response = ec2_client.modify_volume(
        VolumeId=volume_id,
        VolumeType='gp3',
    )
    return {
        "VolumeId": volume_id,
        "RequestId": response["ResponseMetadata"]["RequestId"]
    }
