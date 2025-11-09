# Using Bruno with Databricks and Azure CLI

## Using Bruno with Azure Databricks and Azure CLI, without a Key Vault

---

Fenno Vermeij, November 9, 2025

---

I couldn't find any good documentation on this (I probably didn't look good enough, because this seems like a very common usecase)

Also, this blog is not going to be as long and wordy as previous ones, since the goal is just to show how I solved it. I will assume you are already familliar and have installed Bruno and the Azure CLI. Also, this tutorial is intended to work with Azure Databricks, not AWS or Google Cloud. I will not be using Databricks PAT tokens, since with them, the solution becomes trivial.

However, to make it easier for myself, I will use the `az cli` as a child process, rather than making a rest api call to `login.microsoftonline.com`, which is the default way to obtain tokens (examples: [here](https://blog.jongallant.com/2021/02/azure-rest-apis-postman-2021/) and [here](https://github.com/fennovj/azure-api-auth/).)

Bruno now has [Azure CLI for Key Vault integration](https://docs.usebruno.com/secrets-management/secret-managers/azure-key-vault/cli-authentication), but just for using the Key Vault as a secret manager. I don't need a secret manager, since I just want to use my Azure CLI Credentials.

Also, I hope/think there is probably a better way to do this natively in Bruno, but I haven't found it.

## Connecting to Azure Databricks

1) Create a collection for your Azure Databricks requests. Under 'script', enter the following:

    const { execSync } = require('child_process');
    
    const expiresOn = bru.getVar('expires_on') ?? 0;
    const now = Math.floor(Date.now() / 1000);
    
    if ((expiresOn - now) < 60) {
      // Get access token from Azure CLI
      const resp = execSync('/opt/homebrew/bin/az account get-access-token --scope=2ff814a6-3304-4ab8-85cb-cd0e6f879c1d/.    default');  
      const tokenData = JSON.parse(resp);
      bru.setVar('databricks_token', tokenData.accessToken);
      bru.setVar('expires_on', tokenData.expires_on);
    }


This script will, before every request, see if the token is still valid (for at least 60 more seconds), and if not, request one using the Azure CLI. This means you must have an active Azure CLI credential, which is created with `az login`. (This step is not done in Bruno, since in practice, I always have an active Azure CLI credential.)

Here, you may want to replace the `/opt/homebrew/bin/az` with whatever path to your az cli executable. The `2ff..c1d` token is global, and simply refers to the resource ID for the Azure Databricks service.

Next, under 'auth', select Bearer token, and enter `{{databricks_token}}`

I would also recommend, under 'Vars', create variables such as 'account_id' and 'workspace_instance_name', although the latter may be difficult if you have many workspaces.

Some example requests to test if it is working:

- `GET https://accounts.azuredatabricks.net/api/2.0/accounts/{{account_id}}/metastores` (must be account admin to call this endpoint)
- `GET https://{{workspace_instance_name}}/api/2.1/clusters/list`

## Connecting to the ARM/Graph API

We can use a nearly-identical trick to obtain tokens for the ARM and Graph API. We just need to change the scopes when requesting tokens:

- `/opt/homebrew/bin/az account get-access-token --scope=https://graph.microsoft.com/.default`
- `/opt/homebrew/bin/az account get-access-token --scope=https://management.core.windows.net/.default`

Here is an example script:

    const { execSync } = require('child_process');
    
    const expiresOn = bru.getVar('expires_on') ?? 0;
    const now = Math.floor(Date.now() / 1000);
    
    if ((expiresOn - now) < 60) {
      // Get Graph access token from Azure CLI
      const resp = execSync('/opt/homebrew/bin/az account get-access-token --scope=https://graph.microsoft.com/.default');  
      const tokenData = JSON.parse(resp);
      bru.setVar('token', tokenData.accessToken);
      bru.setVar('expires_on', tokenData.expires_on);
    }

Again, go to `auth`, select `Bearer token`, and enter `{{token}}` as the token.

Some example requests to test:

- `GET https://graph.microsoft.com/v1.0/groups/` (requires Graph scope)
- `GET https://management.azure.com/subscriptions/{{subscription_id}}/providers/Microsoft.Storage/storageAccounts?api-version=2024-01-01` (requires ARM scope)