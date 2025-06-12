import json
from typing import Optional
from lib.logging_utils import init_logger
from server.lib.vcon_redis import VconRedis
from azure.storage.blob import ContainerClient
from datetime import datetime

logger = init_logger(__name__)


default_options = {}


def save(
    vcon_uuid,
    opts=default_options,
):
    logger.info("Starting the Azure Blob Storage for vCon: %s", vcon_uuid)
    try:
        vcon_redis = VconRedis()
        vcon = vcon_redis.get_vcon(vcon_uuid)
        container_client = ContainerClient.from_connection_string(
            opts["azure_blob_connection_string"],
            opts["azure_blob_container"]
        )
        blob_name = f"{vcon_uuid}.vcon"
        container_client.upload_blob(
            blob_name,
            vcon.dumps()
        )
        logger.info(f"Finished Azure Blob Storage for vCon: {vcon_uuid}")
    except Exception as e:
        logger.error(
            f"Azure Blob Storage plugin: failed to insert vCon: {vcon_uuid}, error: {e}"
        )
        raise e

def get(vcon_uuid: str, opts=default_options) -> Optional[dict]:
    """Get a vCon from Azure Blob Storage by UUID."""
    try:
        container_client = ContainerClient.from_connection_string(
            opts["azure_blob_connection_string"],
            opts["azure_blob_container"]
        )
        blob_name = f"{vcon_uuid}.vcon"
        blob_client = container_client.get_blob_client(blob_name)
        response = blob_client.download_blob().readall()
        return json.loads(response.decode('utf-8'))
        
    except Exception as e:
        logger.error(f"Azure Blob Storage plugin: failed to get vCon: {vcon_uuid}, error: {e}")
        return None
