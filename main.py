import boto3
import requests
import os
from dotenv import load_dotenv
from botocore.exceptions import BotoCoreError, ClientError

load_dotenv()

def extract_text_from_image(image_url):
    # Get AWS credentials from .env
    aws_access_key = os.getenv('AWS_ACCESS_KEY')
    aws_secret_key = os.getenv('AWS_SECRET_KEY')
    aws_region = os.getenv('AWS_REGION')

    # Initialize Rekognition client
    rekognition = boto3.client(
        'rekognition',
        aws_access_key_id=aws_access_key,
        aws_secret_access_key=aws_secret_key,
        region_name=aws_region
    )

    # Download the image
    try:
        response = requests.get(image_url)
        response.raise_for_status()
        image_bytes = response.content
    except requests.RequestException as e:
        print(f"Failed to download image: {e}")
        return

    # Analyze the image for text extraction
    try:
        result = rekognition.detect_text(Image={'Bytes': image_bytes})
    except (BotoCoreError, ClientError) as e:
        print(f"AWS Rekognition error: {e}")
        return

    # Print extracted text
    print("Extracted Text from the Image:")
    for text_detail in result['TextDetections']:
        if text_detail['Type'] == 'LINE':
            print(text_detail['DetectedText'])

if __name__ == "__main__":
    image_url = input("Enter the URL of the image: ")
    extract_text_from_image(image_url)
