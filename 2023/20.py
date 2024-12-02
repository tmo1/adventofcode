# https://adventofcode.com/2023/day/20

ff_modules, con_modules = {}, {}
for line in open(0):
    module_name, destinations = line.strip().split(' -> ')
    destinations = destinations.split(', ')
    if module_name == 'broadcaster':
        broadcast = destinations
    elif module_name[0] == '%':
        ff_modules[module_name[1:]] = {'state': 'off', 'dest': destinations}
    else:
        con_modules[module_name[1:]] = {'inputs': {}, 'dest': destinations}
for destination in [d for d in broadcast if d in con_modules]:
    con_modules[destination]['inputs']['broadcaster'] = 'low'
for k, v in (ff_modules | con_modules).items():
    for destination in [d for d in v['dest'] if d in con_modules]:
        con_modules[destination]['inputs'][k] = 'low'
total_high, total_low = 0, 0
for i in range(1000):
    pulses = [{'value': 'low', 'source': 'button', 'dest': 'broadcaster'}]
    while pulses:
        new_pulses = []
        for pulse in pulses:
            if pulse['value'] == 'high':
                total_high += 1
            else:
                total_low += 1
            if pulse['dest'] == 'broadcaster':
                new_pulses.extend([{'value': pulse['value'], 'source': 'broadcaster', 'dest': new_dest} for new_dest in broadcast])
            elif pulse['dest'] in ff_modules:
                if pulse['value'] == 'low':
                    ff_modules[pulse['dest']]['state'], new_value = ('on', 'high') if ff_modules[pulse['dest']]['state'] == 'off' else ('off', 'low')
                    new_pulses.extend([{'value': new_value, 'source': pulse['dest'], 'dest': new_dest} for new_dest in ff_modules[pulse['dest']]['dest']])
            elif pulse['dest'] in con_modules:
                con_modules[pulse['dest']]['inputs'][pulse['source']] = pulse['value']
                new_value = 'high' if 'low' in con_modules[pulse['dest']]['inputs'].values() else 'low'
                new_pulses.extend([{'value': new_value, 'source': pulse['dest'], 'dest': new_dest} for new_dest in con_modules[pulse['dest']]['dest']])
        pulses = new_pulses
print(total_high * total_low)
