# Scheme for Communications

Now that we have obtained the optimal action for each edge device at the central server, we need to communicate this information to them. We will use serial communication for this purpose. A desired situation is that the central server will send the optimal action to each edge device one by one. However, this is not possible because the central server may not be able to reach all edge devices, and we may need extra intermediate devices.

To resolve this issue, every node in the network will try to spread all information to its neighbors as soon as it receives it, unless it has already done so. This way, the information will spread through the network and reach all edge devices. This is a very simple and effective way to spread information in a network.

Each message is formatted as follows:

```
<time_step> <edge_device_id> <action>
```

