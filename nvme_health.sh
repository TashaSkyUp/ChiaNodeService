#!/bin/bash
for nvme in /dev/nvme???; do sudo nvme smart-log $nvme -H;done
