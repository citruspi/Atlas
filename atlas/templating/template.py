#!/usr/bin/env python
# -*- coding: utf-8 -*-

from jinja2 import Template as Jinja2Template
from atlas.providers import providers


class Template(Jinja2Template):

    def __init__(self, *args, **kwargs):
        super(Template, self).__init__(*args, **kwargs)

        for provider in providers:
            self.globals[provider] = providers[provider]
