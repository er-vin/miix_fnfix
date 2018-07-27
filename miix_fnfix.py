#! /usr/bin/env python3
# -*- coding: utf-8 -*-

#
# Copyright 2018 Kevin Ottens <ervin@ipsquad.net>
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
#

from argparse import ArgumentParser

import usb.core
import usb.util

reattach_needed = False

def claim_device(device, interface):
    global reattach_needed
    if device.is_kernel_driver_active(interface):
        reattach_needed = True
        device.detach_kernel_driver(interface)

    usb.util.claim_interface(device, interface)

def release_device(device, interface):
    usb.util.release_interface(device, interface)

    if reattach_needed:
        device.attach_kernel_driver(interface)

if __name__ == "__main__":
    arg_parser = ArgumentParser(description="A tool for forcing fnlock mode on Lenovo MIIX keyboards")
    arg_parser.add_argument("-u", "--unlock", action='store_true', help="Unlocks")
    args = arg_parser.parse_args()

    # Find the MIIX keyboard
    device = usb.core.find(idVendor=0x17ef, idProduct=0x60bb)
    if device is None:
        raise ValueError('No MIIX keyboard attached to this system')

    interface = 0x01

    claim_device(device, interface)

    value = 0x02
    if (args.unlock):
        value = 0x01

    try:
        device.ctrl_transfer(0x21, 0x09, 0x0209, interface, bytes([0x09, 0x54, value]))
    except:
        release_device(device, interface)
        raise

    release_device(device, interface)

