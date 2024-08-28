import aiofiles
import boto3
from botocore.exceptions import NoCredentialsError
import json


class S3Service:
    def __init__(self):
        self.s3_client = boto3.client(
            "s3",
            endpoint_url="http://minio:9000",
            aws_access_key_id="minioadmin",
            aws_secret_access_key="minioadmin123",
        )

    async def handle_pdf_generation(self, message):
        data = json.loads(message.value)
        pdf_path = data["pdf_path"]
        competition_name = data["competition_name"]
        competition_date = data["competition_date"]
        s3_path = f"{competition_name}/{competition_date}/results.pdf"
        await self.upload_file(pdf_path, "your-s3-bucket", s3_path)

    async def upload_file(self, file_path, bucket="your-s3-bucket", object_name=None):
        if object_name is None:
            object_name = file_path

        try:
            async with aiofiles.open(file_path, "rb") as file:
                await self.s3_client.upload_fileobj(file, bucket, object_name)
            s3_url = f"http://minio:9000/{bucket}/{object_name}"
            return s3_url
        except FileNotFoundError:
            print("The file was not found")
            return None
        except NoCredentialsError:
            print("Credentials not available")
            return None
