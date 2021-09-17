#### Challenge:

Attached is a packet capture taken from a building management network. One of the analog sensors reported values way outside of its normal operating range. Can you determine the object name of this analog sensor? Flag Format: flag{Name-of-sensor}. For example if the object name of this analog sensor was "Sensor_Temp1", the flag would be flag{Sensor_Temp1}. (Note: because there are a limited number of sensors, we're only giving you two guesses for this challenge, so please check your input carefully.)

[bacnet.pcap](./bacnet.pcap ":ignore")

---

#### Solution:

- `pcap` contains communication of multiple sensors, with the their readings in `bacapp.present_value.real` field
- sensors at the beginning of transmission propagate their `name` along side with their `instance_number` which could be used to assign value to sensor

```bash
for sensor in $( tshark -r ./bacnet.pcap -T fields -e bacapp.object_name -e bacapp.instance_number -Y 'bacapp.object_name' | sort | uniq | tr '\t' -); do
    tshark -r ./bacnet.pcap -T fields -e bacapp.present_value.real -Y "bacapp.present_value.real && bacapp.instance_number == ${sensor##*-}" | \
        gnuplot -p -e "set title '${sensor%%-*}' offset 0,1; plot '<cat' with lines"
done
```

---

<details><summary>FLAG:</summary>

```
flag{Sensor_12345}
```

</details>
<br/>
