# performs a simple device inquiry followed by a remote name request of each discovered device.
import bluetooth

print 'performing inquiry...'
nearby_devices = bluetooth.discover_devices(duration=8, lookup_names=True, flush_cache=True, lookup_class=False)
print 'found %d devices' % len(nearby_devices)

for addr, name in nearby_devices:
    print " %s - %s" % (addr, name)