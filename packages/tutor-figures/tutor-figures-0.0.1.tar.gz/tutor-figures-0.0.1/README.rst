Figures plugin for `Tutor <https://docs.tutor.overhang.io>`_
============================================================

`Figures <https://github.com/appsembler/figures>`_ is a data retrieval and reporting app for Open edX; this is a plugin for Tutor that allows quick and easy integration in an Open edX platform. It works both locally and on a Kubernetes-based platform.

.. image:: ./e-logo.svg
    :alt: E-ducation
    :target: https://www.e-ducation.cn/

This plugin was developed with support from `E-ducation <https://www.e-ducation.cn/>`_. Thanks!

Installation
------------

::
  
    pip install tutor-figures

Then, to enable this plugin, run::
  
    tutor plugins enable figures

You will have to re-generate the environment and rebuild the "openedx" docker image::
  
    tutor config save
    tutor images build openedx

You will then have to run LMS migrations. To do so, run::
  
    tutor local init

This last step is unnecessary if you run instead ``tutor local quickstart``.