# RBX Platform

The **RBX Platform** is the core service powering the **Rig**.
Its purpose is to house the business logic for planning and distributing campaigns,
and provide a web interface to manipulating its data, via a Public API.

\[ [Platform Formats](#platform-formats) ]
\[ [Platform Permissions](#platform-permissions) ]
\[ [Public API](#public-api) ]
\[ [PyPI](#pypi) ]
\[ [VIOOH](#viooh) ]
\[ [IPONWEB Publishing](#iponweb-publishing) ]
\[ [Google Cloud Platform](#google-Cloud-platform) ]
\[ [Contribute](#contribute) ]

## Platform Formats

The JSON-formatted Ad Unit and Creative **Formats** definitions are available at the following URLs:

```
/fixtures/ad-formats.json
/fixtures/creative-formats.json
```

## Platform Permissions

**Platform Permissions** define **actions** a user can perform.

An action represents a particular feature in the Rig.
For instance, _"Create a Campaign"_, _"Update a Strategy"_, or _"Access the Custom Report"_.

These permissions are represented as strings in the Platform.
For instance, the permissions representing the _"Create a Campaign"_ action is `create_campaign`.

They are implemented on top of the Django's simple permissions system.

> The full list of Permissions is defined in the `rbx.platform.types.permission` module.
>
> Note that these permissions are never assigned to users.
> Instead, **Roles** (Django Groups) are created and given specific sets of permissions.
> These Roles are then assigned to users.

Access to these actions is implemented in the **Public API**.

> The [**Platform API**](./docs/platform/README.md) controls access to individual Campaigns.

## Public API

The Public API is used exclusively by the Rig UIs.

- The JSON-RPC API is the main public entrypoint.
  See the full [API Reference](./docs/api/README.md) for details.
- The HTTP API provides endpoints that are not compliant with JSON-RPC 2.0.

## PyPI

The project is distributed as a PyPI package at [pypi.python.org/pypi/rbx](https://pypi.python.org/pypi/rbx/).

> The package does not provide any use apart from reserving the namespace in PyPI.

## VIOOH

Creatives are submitted to VIOO's SmartContent via a [client interface](./docs/platform/VIOOH.md).

## IPONWEB Publishing

Real-time bidding (RTB) is the process by which the decision about which ad to serve to a user
browsing a site happens in real time, by means of a bidding process where the highest bidder wins.
Without going into detail about what that process entails, our interface to the RTB world is via
a platform developed by our partner IPONWEB.

Our "API" to the IPONWEB platform consists of uploading an XML file that contains the whole set of
live campaigns that participate in bidding.

> All IPONWEB-related documentation can be found on their
> [Confluence Wiki](https://confluence.iponweb.net/display/UPLATFORMKB/u-Platform+Knowledge+Base).

### XML Feed

The XML feed sent to the IPONWEB SFTP server is generated on the fly.
An endpoint is available to display it in its entirety when troubleshooting,
and is accessible at the following URL:

```
/iponweb/rtb_data.xml
```

The XML must match the RelaxNG schema, the latest version of which can be found on IPONWEB's
Mercurial repository:

    https://hg.iponweb.net/rockabox/trunk/file/tip/scripts/validate.rng

### U-Slicer

The **Media Cost**, a.k.a. _Spend_, is queried via IPONWEB's u-Slicer API.

A client implementation is available in the `rbx.iponweb` package.

e.g.:

```python
from rbx.iponweb.client import Client
>>> client = Client(slicer_name='Traffic', project_name='rockabox', token='eyJhbGciO...')
>>> client.actual_pub_payout(start_date='2017-08-10',
...                          end_date='2017-08-25',
...                          strategies=[1073745495, 1073745496])

{1073745496: 988.07, 1073745495: 1369.36}
```

> The `token` is a permanent API token, generated via the IPONWEB UI: https://uauth.iponweb.com/

### Automated Delivery Control

The Platform always ensures that Campaigns don't over-deliver. The controlling factor is spend,
which we get from the bidder (IPONWEB) via their u-Slicer API.

Once the total spend for a Strategy has reached its budget, the Strategy is flagged as `FINISHED`.

These Strategies will resume when more budget is assigned to them.

> There are no restrictions on the budget users can allocate, apart from it being within the
> Campaign budget.
> It is therefore up to the user to make sure enough budget is added.

The bidder doesn't support overall impression or spend cap. It does, however, support daily spend
capping. Using the total spend for LIVE Strategies, and the total budget assigned to them, we can
regularly adjust the daily capping to ensure that they never overspend.

The data processing latency of the u-Slicer API is ~3h. Therefore the schedule for this regular
adjustment check runs every 3 hours.

> Although we do store the spend figure for this feature, we do not expose it to the UI.

#### Notifications

Ad Operations (`opsuk@scoota.com`) and all users assigned to the affected Strategies with the
`CREATE_CAMPAIGN` permission are notified via email:

- When a daily cap is automatically adjusted.
- When a Strategy is flagged as having reached its total budget.

### Currency Exchange Rates

When required (for instance, for VIOOH distribution), the bidder will need to know which exchange
rate against the USD to use to calculate media costs. The effective rate used is the _15 Day
Moving Average_, based on historical data retrieved from the **Open Exchange Rates API**.

> Historical data are End-Of-Day values.

## Google Cloud Platform

Access to the **Google Cloud Platform** is granted via a JSON credentials file.
The testing and development setup uses the **Pub/Sub Publisher** service account to
access the Google APIs.

> This service account already exists.
> See the [GCP API Manager](https://console.cloud.google.com/apis/credentials).

### Master Data Management Notifications

MDM notifications are published to the `platform-notifications` Pub/Sub topic.

> This topic must exist.
> Check the [GCP Console](https://console.cloud.google.com/cloudpubsub/topicList).

The MDM is notified about:

 - New Campaigns.
 - Campaign updates.
 - New Strategies (when they become `READY`).
 - Strategy updates (`READY` and above only).
 - New Ad Units (when they become `READY`).
 - Ad Unit updates (`READY` only).
 - Creatives and Components (when the Creatives are released).
 - New Placements (when they become `READY`).

## Contribute

[Contributors Guide](./CONTRIBUTING.md)
