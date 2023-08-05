#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
from collections import namedtuple, Mapping
from pathlib import Path, PosixPath
from warnings import warn

import wrapt

from warg.named_ordered_dictionary import NOD

__author__ = "cnheider"


class UpperAttrMetaclass(type):
    def __new__(cls, clsname, bases, dct):

        uppercase_attr = {}
        for name, val in dct.items():
            if not name.startswith("__"):
                uppercase_attr[name.upper()] = val
            else:
                uppercase_attr[name] = val

        return super(UpperAttrMetaclass, cls).__new__(cls, clsname, bases, uppercase_attr)


class ConfigObject(object):
    pass


def to_lower_properties(C_dict):
    if not isinstance(C_dict, dict):
        C_dict = config_to_mapping(C_dict)

    a = ConfigObject()

    for (k, v) in C_dict.items():
        assert isinstance(k, str)
        lowered = k.lower()
        if isinstance(v, (PosixPath, Path)):
            setattr(a, lowered, str(v))
        else:
            setattr(a, lowered, v)

    return a


def get_upper_case_vars_or_protected_of(module, lower_keys=True) -> Mapping:
    v = vars(module)
    check_for_duplicates_in_args(**v)
    if v:
        if lower_keys:
            return {
                key.lower(): value
                for key, value in module.__dict__.items()
                if (key.isupper() or (key.startswith("_")) and not key.endswith("_"))
            }
        return {
            key: value
            for key, value in module.__dict__.items()
            if (key.isupper() or (key.startswith("_")) and not key.endswith("_"))
        }
    return {}


def config_to_mapping(C: object, only_upper_case: bool = True) -> NOD:
    if only_upper_case:
        return NOD(get_upper_case_vars_or_protected_of(C))
    else:
        return NOD(vars(C))


def parse_arguments(desc, C):
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument(
        "--ENVIRONMENT_NAME",
        "-E",
        type=str,
        default=C.ENVIRONMENT_NAME,
        metavar="ENVIRONMENT_NAME",
        help="Name of the environment to run",
    )
    parser.add_argument(
        "--PRETRAINED_PATH", "-T", metavar="PATH", type=str, default="", help="Path of pre-trained model"
    )
    add_bool_arg(
        parser,
        "render",
        dest="RENDER_ENVIRONMENT",
        default=C.RENDER_ENVIRONMENT,
        help="Rendering of the environment",
    )
    parser.add_argument(
        "--NUM_WORKERS",
        "-N",
        type=int,
        default=4,
        metavar="NUM_WORKERS",
        help="Number of threads for agent (default: 4)",
    )
    add_bool_arg(
        parser,
        "connect_to_running",
        dest="CONNECT_TO_RUNNING",
        default=C.CONNECT_TO_RUNNING,
        help="Connect to already running simulation or start an instance",
    )
    parser.add_argument(
        "--SEED", "-S", type=int, default=C.SEED, metavar="SEED", help=f"Random seed (default: {C.SEED})"
    )
    parser.add_argument(
        "--VERBOSE", "-V", action="store_true", default=C.VERBOSE, help="Enable verbose debug prints"
    )
    parser.add_argument(
        "--skip_confirmation",
        "-skip",
        action="store_true",
        default=False,
        help="Skip confirmation of config to be used",
    )
    parser.add_argument(
        "--ROLLOUTS", "-rollouts", type=int, default=C.ROLLOUTS, metavar="ROLLOUTS", help="Number of rollouts"
    )
    parser.add_argument(
        "--CONFIG",
        "-config",
        type=str,
        default=None,
        metavar="CONFIG",
        help="Path to a config (nullifies all other arguments, if specified)",
    )
    add_bool_arg(parser, "cuda", dest="USE_CUDA", default=C.USE_CUDA, help="Cuda flag")

    args = parser.parse_args()

    return args


def add_bool_arg(parser, name, *, dest=None, default=False, **kwargs):
    if not dest:
        dest = name

    group = parser.add_mutually_exclusive_group(required=False)

    group.add_argument(f"--{name.upper()}", f"-{name.lower()}", dest=dest, action="store_true", **kwargs)
    group.add_argument(
        f"--NO-{name.upper()}", f"-no-{name.lower()}", dest=dest, action="store_false", **kwargs
    )
    parser.set_defaults(**{dest: default})


def check_for_duplicates_in_args(**kwargs) -> None:
    for key, value in kwargs.items():

        occur = 0

        if kwargs.get(key) is not None:
            occur += 1
        else:
            pass

        if key.isupper():
            k_lowered = f"_{key.lower()}"
            if kwargs.get(k_lowered) is not None:
                occur += 1
            else:
                pass
        else:
            k_lowered = f'{key.lstrip("_").upper()}'
            if kwargs.get(k_lowered) is not None:
                occur += 1
            else:
                pass

        if occur > 1:
            warn(f"Config contains hiding duplicates of {key} and {k_lowered}, {occur} times")


def namedtuple_args(n_tuple):
    @wrapt.decorator(adapter=n_tuple)
    def wrapper(wrapped, instance, args, kwargs):
        if isinstance(args[0], n_tuple):
            n = args[0]
        else:
            n = n_tuple(*args, **kwargs)
        return wrapped(n)

    return wrapper


if __name__ == "__main__":

    c = namedtuple("C", ("a", "b"))

    @namedtuple_args(c)
    def add(v):
        return v.a + v.b

    def add2(a, b):
        return a + b

    h = add(2, 2)
    print(h)

    j = add(c(1, 4))
    print(j)

    wq = add2(2, 4)
    print(wq)

    wc = add2(*c(4, 3))
    print(wc)
