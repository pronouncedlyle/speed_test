#!/usr/bin/env python3
import os

import aws_cdk as cdk

from speed_test.speed_test_stack import SpeedTestStack


app = cdk.App()
SpeedTestStack(app, "SpeedTestStack",)

app.synth()
