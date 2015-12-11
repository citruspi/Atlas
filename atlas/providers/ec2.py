#!/usr/bin/env python
# -*- coding: utf8 -*-

from boto import ec2


def ec2_instances(profile, region):

    conn = ec2.connect_to_region(region, profile_name=profile)

    return conn.get_only_instances()
