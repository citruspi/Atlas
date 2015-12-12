#!/usr/bin/env python
# -*- coding: utf-8 -*-

from atlas.providers.ec2 import ec2_instances
from atlas.providers.env import env

providers = {
    'ec2_instances': ec2_instances,
    'env': env
}
