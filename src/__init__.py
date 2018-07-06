#!/usr/bin/python3

import config
import subscriber_openhab
import loader

configfilename="test.ini"


config = config.Config(configfilename)

sub = subscriber_openhab.SubscriberOpenHAB(config)
loader = loader.Loader(config, sub)
