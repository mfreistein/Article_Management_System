#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init
import os
import sys
import inspect

use_plugin("python.core")
use_plugin('python.install_dependencies')
use_plugin('python.pydev')
use_plugin("python.unittest")
use_plugin("python.coverage")
use_plugin("python.distutils")

use_plugin("python.flake8")
use_plugin("python.pycharm")
use_plugin("python.sphinx")
use_plugin('python.pycharm')


name = "PyBuilder"
default_task = ["install_dependencies", "analyze", "publish", "sphinx_generate_documentation"]



@init
def set_properties(project):
    project.set_property("dir_source_main_python", "../src")
    project.set_property("dir_source_unittest_python", "../src/Conception")
    project.set_property("dir_source_main_scripts", "PyBuilder/scripts")
    project.set_property("dir_docs", "PyBuilder/docs")
    project.build_depends_on("mysql.connector")
    project.set_property("verbose", True)

    # define unittest coverage properties
    project.set_property("coverage_threshold_warn", 0)
    project.set_property("coverage_break_build", True)
    # define linting properties
    project.set_property("flake8_break_build", False)
    project.set_property("flake8_max_line_length", 300)
    project.set_property("flake8_verbose_output", True)
    # define documentation properties
    project.set_property("sphinx_builder", "html")
    project.set_property("sphinx_config_path", "Sphinx")
    project.set_property("sphinx_source_dir", "../src")
    project.set_property("sphinx_output_dir", "Sphinx/_build")
