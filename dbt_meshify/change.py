import dataclasses
from enum import Enum
from pathlib import Path
from typing import Dict, Optional, Set

from dbt.node_types import NodeType


class Operation(str, Enum):
    """An operation describes the type of work being performed."""

    add = "add"
    update = "update"
    remove = "remove"


class EntityType(str, Enum):
    """An EntityType represents the type of entity being operated on in a Change"""

    Model = "model"
    Analysis = "analysis"
    Test = "test"
    Snapshot = "snapshot"
    Operation = "operation"
    Seed = "seed"
    # TODO: rm?
    RPCCall = "rpc"
    SqlOperation = "sql_operation"
    Documentation = "doc"
    Source = "source"
    Macro = "macro"
    Exposure = "exposure"
    Metric = "metric"
    Group = "group"
    SemanticModel = "semantic_model"
    Project = "project"
    Code = "code"

    def pluralize(self) -> str:
        if self is self.Analysis:
            return "analyses"
        return f"{self}s"


@dataclasses.dataclass
class Change:
    """A change represents a unit of work that should be performed on a dbt project."""

    operation: Operation
    entity_type: EntityType
    identifier: str
    path: Path
    data: Dict


class ChangeSet:
    """A collection of Changes that will be performed"""

    def __init__(self, changes: Set[Change]) -> None:
        self.changes = changes
