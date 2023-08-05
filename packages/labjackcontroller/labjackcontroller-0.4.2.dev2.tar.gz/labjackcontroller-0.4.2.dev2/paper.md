---
title: 'labjack-controller: Robust and Easy Data Collection with Labjack T-Series DAQs in Python'
tags:
  - Python
  - experimental
  - daq
  - labjack
  - parallel
authors:
  - name: Benjamin A. Montgomery
    orcid: 0000-0002-1240-5385
    affiliation: 1
  - name: Paul A. Nakroshis
    orcid: 0000-0003-1887-354X
    affiliation: 1
affiliations:
- name: University of Southern Maine
  index: 1
date: 5 April 2019
bibliography: paper.bib
---

# Summary

The ability to accurately collect and computationally process data from
sensors in both a logging and interactive sense is crucial to many scientific
experiments. Researchers in many field are results driven and want to be able
to easily and inexpensively gather data at high speeds with uniform sampling
rates without having to invest  weeks of time learning a complicated API.
Common (expensive) paid solutions are found in  Digital Acquisition Devices
(DAQs) provided by companies like National Instruments (NI). These pre-built
DAQs are generally understood to be tied to proprietary analysis software or
languages, such as NI's paid language LabView. In light of this, there has
been a recent surge in DAQ offerings from multiple manufacturers to capture
the market.  These solutions tend to have cost-effective, versatile hardware,
but interfaces that are poorly designed or immature [@Lawson], which makes it
difficult for non-specialists to use. Current offerings from Labjack [@Labjack]
are one such example; their hardware is used in major industrial applications,
but the interface is exceedingly nuanced and provides little in the way of
error recovery.

`labjack-controller` is a Python package for Labjack's most recent DAQs, the
T-series devices, and serves a similar overall purpose as NI's 
nidaqmx-python [@ni] data collection package for NI devices.
It focuses on providing thread-safe functions that abstract and automate data
collection, error handling, and configuration procedures that are normally
exceedingly nuanced or complex. Care was given to writing efficient code for
streaming data from and communicating to these devices, and using as many
optimized tools as possible, such as Labjack's provided low-level C interface.
In the interest of versatility, `labjack-controller` fully supports Linux,
OSX, and Windows, along with any connection method or protocol supported by
any of the T-series devices.

`labjack-controller` is designed to be used by anyone who has at least an
introductory knowledge of Python and intends to involve a computer in the
process of reading sensor data, from data backup purposes to live
reaction to sensor readings. We emphasize that this package is a huge time
saver for researchers interested in gathering data so that they can focus on the science
rather than losing valuable time in development or being forced into expensive
proprietary options.  It is currently used in upper-level undergraduate
physics laboratory courses and a research lab at the University of Southern
Maine for the purposes of reacting to live data, most notably with a
torsion pendulum with dynamic electromagnetic damping. We expect that the
speed, error handling abilities, and parallelization support of this library
will make robust and reliable data collection one of the least challenging
aspects of experimental science.

# Acknowledgements

We acknowledge funding through the University of Southern Maine.


# References
