# Zendesk ST2 Integration Pack

This integration allows ticket management between StackStorm and Zendesk REST API using Zenpy python module 
Zendesk Rest API reference: https://developer.zendesk.com/rest_api/docs/core/introduction 
Zenpy python API reference: https://github.com/facetoe/zenpy

# Setup
## Configuration

* `subdomain` - zendesk subdomain name  
* `email` - Username of service account
* `token` - API token for zendesk service account


## Actions

* `zendesk.update` - Update a ticket in  zendesk 
* `zendesk.insert` - Add/Insert a new ticket in  zendesk 
* `zendesk.delete` - Delete existing ticket from  zendesk 
* `zendesk.close` - Close a ticket from  zendesk with status 'closed' 
