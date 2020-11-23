# recovery_ring_builder

Emergency recovery of ring builder files¶
Problem¶
An emergency might prevent a successful backup from restoring the cluster to operational status.

Solution¶
You should always keep a backup of swift ring builder files. However, if an emergency occurs, this procedure may assist in returning your cluster to an operational state.

Using existing swift tools, there is no way to recover a builder file from a ring.gz file. However, if you have a knowledge of Python, it is possible to construct a builder file that is pretty close to the one you have lost.
