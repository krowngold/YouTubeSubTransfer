# YouTubeSubTransfer
This script simplifies copying YouTube channel subscriptions between Google accounts.
Online resources can be untrustworthy as they command too much access to your channel and often shield their implementation details. The simple implementation in this repo plainly reveals how calls are made, allowing users to use their own GCP project for added peace of mind.

Suppose you have two YouTube channels: channel A and channel B. Channel A and B have their own separate sets of subscriptions. YouTubeSubTransfer copies all subscriptions from channel A to channel B as long as channel B does not already contain that subscription.

### Getting Started
The YouTube Data API is subject to quota limits on GCP, with a limit of 10,000 units. Each call to `subscriptions.list` consumes one unit, while `subscriptions.insert` consumes 50. YouTube channels can have a maximum of 2,000 subscriptions, so just copying these subscriptions would require around 100,000 quota units to add the maximum number of subscriptions to another channel, not including costs incurred by listing subscriptions.

Follow [these instructions](https://developers.google.com/youtube/v3/getting-started) to get started making calls to the YouTube Data API (v3). Download your `client_secret.json` and place it in the same directory as the `main.py` file.
This file operates entirely from the command line, simply requiring `python main.py` to execute.

### Things to consider

No flags/arguments are provided. Upon execution, the user is prompted twice to authorize the application to read their YouTube credentials (as necessary for the user's GCP project) for both their channels. After authorization is granted, subscription sets are retrieved for both channel A (the source) and channel B (the destination. A set of 'pending' subscriptions is created from both retrieved sets. `subscriptions.insert` calls are made for each pending subscription.

As a result of this implementation, if the user runs into quota throttling they can either request more quota for their project within GCP, or wait 24 hours before re-running the script. While not the ideal implementation, it should be rare that users need all of their subscriptions moved between accounts within 24 hours, and this will only be necessary if channel A has enough subscriptions that channel B doesn't to incur rate throttling. In the absolute worst case, about 200 subscriptions can be moved per day, so transferring all 2,000 subscriptions from a single channel to one that has zero subscriptions would take 10 days.
