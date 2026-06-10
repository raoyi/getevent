#!/usr/bin/env python3
#
# Copyright (C) 2015 The Android Open Source Project
#
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import argparse
import re

input_prop_list = []
ev_list = []
syn_list = []
key_list = []
rel_list = []
abs_list = []
sw_list = []
msc_list = []
led_list = []
rep_list = []
snd_list = []
mt_tool_list = []
ff_status_list = []
ff_list = []

r = re.compile(r'#define\s+(\S+)\s+((?:0x)?\d+)')

parser = argparse.ArgumentParser(description='Generate input.h label arrays for getevent.c')
parser.add_argument('input_h', nargs='?',
                    default='/usr/arm-linux-gnueabihf/include/linux/input.h',
                    help='path to linux/input.h (default: /usr/arm-linux-gnueabihf/include/linux/input.h)')
args = parser.parse_args()

with open(args.input_h, 'r') as f:
    for line in f:
        m = r.match(line)
        if m:
            name = m.group(1)
            if name.startswith("INPUT_PROP_"):
                input_prop_list.append(name)
            elif name.startswith("EV_"):
                ev_list.append(name)
            elif name.startswith("SYN_"):
                syn_list.append(name)
            elif name.startswith("KEY_") or name.startswith("BTN_"):
                key_list.append(name)
            elif name.startswith("REL_"):
                rel_list.append(name)
            elif name.startswith("ABS_"):
                abs_list.append(name)
            elif name.startswith("SW_"):
                sw_list.append(name)
            elif name.startswith("MSC_"):
                msc_list.append(name)
            elif name.startswith("LED_"):
                led_list.append(name)
            elif name.startswith("REP_"):
                rep_list.append(name)
            elif name.startswith("SND_"):
                snd_list.append(name)
            elif name.startswith("MT_TOOL_"):
                mt_tool_list.append(name)
            elif name.startswith("FF_STATUS_"):
                ff_status_list.append(name)
            elif name.startswith("FF_"):
                ff_list.append(name)


def dump(struct_name, values):
    print(f'static struct label {struct_name}[] = {{')
    for value in values:
        print(f'    LABEL({value}),')
    print('    LABEL_END,')
    print('};')


dump("input_prop_labels", input_prop_list)
dump("ev_labels", ev_list)
dump("syn_labels", syn_list)
dump("key_labels", key_list)
dump("rel_labels", rel_list)
dump("abs_labels", abs_list)
dump("sw_labels", sw_list)
dump("msc_labels", msc_list)
dump("led_labels", led_list)
dump("rep_labels", rep_list)
dump("snd_labels", snd_list)
dump("mt_tool_labels", mt_tool_list)
dump("ff_status_labels", ff_status_list)
dump("ff_labels", ff_list)
