# Azure Blob Storage

This module implements object storage using Azure Blob Storage for the vCon server.

## Overview

Azure Blob Storage provides scalable, durable object storage capabilities, making it ideal for storing vCon data with high availability and reliability.

## Configuration

Required configuration options:

```yaml
storages:
  azureblob:
    module: storage.azureblob
    options:
      azure_blob_connection_string: DefaultEndpointsProtocol=https;AccountName=...;AccountKey=...;EndpointSuffix=core.windows.net
      azure_blob_container: vcons
```

## Usage

```python
from storage import Storage

# Initialize Azure Blob Storage
azureblob_storage = Storage("azureblob")

# Save vCon data
azureblob_storage.save(vcon_id)

# Retrieve vCon data
vcon_data = azureblob_storage.get(vcon_id)
```

## Dependencies

- azure-storage-blob
