from swift.common.ring import RingData, RingBuilder
from array import array
import math
import pickle

"""
    https://docs.openstack.org/swift/pike/admin/objectstorage-troubleshoot.html

    Using existing swift tools, there is no way to recover a builder file from a ring.gz file. However, 
    if you have a knowledge of Python, it is possible to construct a builder file that is pretty close to the one you have lost.
"""


ring = RingData.load('/home/shahbazi/Desktop/rings/account.ring.gz')

partitions = len(ring._replica2part2dev_id[0])

replicas = len(ring._replica2part2dev_id)

builder = RingBuilder(int(math.log(partitions, 2)), replicas, 1)

builder.devs = ring.devs

builder._replica2part2dev = ring._replica2part2dev_id

builder._last_part_moves_epoch = 0

builder._last_part_moves = array('B', (0 for _ in range(partitions)))

builder.change_min_part_hours(24)

# builder._set_parts_wanted()

for d in builder._iter_devs():
        d['parts'] = 0

for p2d in builder._replica2part2dev:
            for dev_id in p2d:
                builder.devs[dev_id]['parts'] += 1

builder.validate()

pickle.dump(builder.to_dict(), open('account.builder', 'wb'), protocol=2)