"""
Define all the business models of the application.
"""

from dataclasses import dataclass
from typing import Dict, List, NewType, Set

Module = NewType("Module", str)
Dependencies = Set[Module]
SourceCode = NewType("SourceCode", str)

ModuleWildcard = NewType("ModuleWildcard", str)
Rules = List[ModuleWildcard]

DependencyRules = Dict[str, Rules]

GlobalDependencies = Dict[Module, Dependencies]


def get_parent(module: Module) -> Module:
    """
    Get the parent module of a given one.
    """
    return Module(module.rpartition(".")[0])


def wildcard_to_regex(module: ModuleWildcard) -> str:
    """
    Return a regex expression for the Module from wildcard
    """
    module_regex = module.replace(".", "\\.").replace("*", ".*")
    module_regex = module_regex.replace("[!", "[^").replace("?", ".?")

    # Special char including a module along with all its submodules:
    module_regex = module_regex.replace("%", r"(\..*)?$")
    return module_regex


@dataclass
class SourceFile:
    """
    A complete information about a source file.
    """

    module: Module
    code: SourceCode
