#!/usr/bin/env python
# -*- coding: utf-8 -*-
import copy

from cpt.packager import ConanMultiPackager

if __name__ == "__main__":
    builder = ConanMultiPackager()
    builder.add(
        settings={"arch": "x86_64", "build_type": "Release"},
        options={"dart:shared": False},
    )
    builder.add(
        settings={"arch": "x86_64", "build_type": "Debug"},
        options={"dart:shared": False},
    )

    # add c++17 build configs
    new_builds = []
    for settings, options, env_vars, build_requires, reference in builder.items:
        new_settings = copy.copy(settings)
        new_settings["compiler.cppstd"] = "17"
        new_settings["compiler.libcxx"] = "libstdc++11"
        new_options = copy.copy(options)
        new_options["dart:build_dartpy"] = True
        new_options["dart:python_version"] = "3.7"
        new_builds.append([settings, options, env_vars, build_requires])
        new_builds.append([new_settings, options, env_vars, build_requires])
        new_builds.append([settings, new_options, env_vars, build_requires])
        new_builds.append([new_settings, new_options, env_vars, build_requires])
    builder.builds = new_builds

    builder.run()
