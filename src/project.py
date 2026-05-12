"""Project 2: Moonlight Museum After Dark.

Implemented by: [Your Name/Team Name]
"""

from __future__ import annotations
from collections import deque
from dataclasses import dataclass
from typing import Deque


@dataclass(frozen=True)
class Artifact:
    """A museum artifact stored in the archive BST."""
    artifact_id: int
    name: str
    category: str
    age: int
    room: str


@dataclass(frozen=True)
class RestorationRequest:
    """A request to inspect or repair an artifact."""
    artifact_id: int
    description: str


class TreeNode:
    """A node for the artifact BST."""
    def __init__(
        self,
        artifact: Artifact,
        left: TreeNode | None = None,
        right: TreeNode | None = None,
    ) -> None:
        self.artifact = artifact
        self.left = left
        self.right = right


class ArtifactBST:
    """Binary search tree keyed by artifact_id."""
    def __init__(self) -> None:
        self.root: TreeNode | None = None

    def insert(self, artifact: Artifact) -> bool:
        if not self.root:
            self.root = TreeNode(artifact)
            return True
        return self._insert_recursive(self.root, artifact)

    def _insert_recursive(self, node: TreeNode, artifact: Artifact) -> bool:
        if artifact.artifact_id == node.artifact.artifact_id:
            return False
        if artifact.artifact_id < node.artifact.artifact_id:
            if node.left is None:
                node.left = TreeNode(artifact)
                return True
            return self._insert_recursive(node.left, artifact)
        else:
            if node.right is None:
                node.right = TreeNode(artifact)
                return True
            return self._insert_recursive(node.right, artifact)

    def search_by_id(self, artifact_id: int) -> Artifact | None:
        current = self.root
        while current:
            if artifact_id == current.artifact.artifact_id:
                return current.artifact
            current = current.left if artifact_id < current.artifact.artifact_id else current.right
        return None

    def inorder_ids(self) -> list[int]:
        result = []
        def traverse(node):
            if node:
                traverse(node.left)
                result.append(node.artifact.artifact_id)
                traverse(node.right)
        traverse(self.root)
        return result

    def preorder_ids(self) -> list[int]:
        result = []
        def traverse(node):
            if node:
                result.append(node.artifact.artifact_id)
                traverse(node.left)
                traverse(node.right)
        traverse(self.root)
        return result

    def postorder_ids(self) -> list[int]:
        result = []
        def traverse(node):
            if node:
                traverse(node.left)
                traverse(node.right)
                result.append(node.artifact.artifact_id)
        traverse(self.root)
        return result


class RestorationQueue:
    """FIFO queue of restoration requests."""
    def __init__(self) -> None:
        self._items: Deque[RestorationRequest] = deque()

    def add_request(self, request: RestorationRequest) -> None:
        self._items.append(request)

    def process_next_request(self) -> RestorationRequest | None:
        return self._items.popleft() if not self.is_empty() else None

    def peek_next_request(self) -> RestorationRequest | None:
        return self._items[0] if not self.is_empty() else None

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def size(self) -> int:
        return len(self._items)


class ArchiveUndoStack:
    """LIFO stack of recent archive actions."""
    def __init__(self) -> None:
        self._items: list[str] = []

    def push_action(self, action: str) -> None:
        self._items.append(action)

    def undo_last_action(self) -> str | None:
        return self._items.pop() if not self.is_empty() else None

    def peek_last_action(self) -> str | None:
        return self._items[-1] if not self.is_empty() else None

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def size(self) -> int:
        return len(self._items)


class ExhibitNode:
    """A node in the singly linked exhibit route."""
    def __init__(self, stop_name: str, next_node: ExhibitNode | None = None) -> None:
        self.stop_name = stop_name
        self.next = next_node


class ExhibitRoute:
    """Singly linked list of exhibit stops."""
    def __init__(self) -> None:
        self.head: ExhibitNode | None = None

    def add_stop(self, stop_name: str) -> None:
        new_node = ExhibitNode(stop_name)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def remove_stop(self, stop_name: str) -> bool:
        if not self.head:
            return False
        if self.head.stop_name == stop_name:
            self.head = self.head.next
            return True
        curr = self.head
        while curr.next:
            if curr.next.stop_name == stop_name:
                curr.next = curr.next.next
                return True
            curr = curr.next
        return False

    def list_stops(self) -> list[str]:
        stops = []
        curr = self.head
        while curr:
            stops.append(curr.stop_name)
            curr = curr.next
        return stops

    def count_stops(self) -> int:
        return len(self.list_stops())


def count_artifacts_by_category(artifacts: list[Artifact]) -> dict[str, int]:
    counts = {}
    for a in artifacts:
        counts[a.category] = counts.get(a.category, 0) + 1
    return counts


def unique_rooms(artifacts: list[Artifact]) -> set[str]:
    return {a.room for a in artifacts}


def sort_artifacts_by_age(artifacts: list[Artifact], descending: bool = False) -> list[Artifact]:
    return sorted(artifacts, key=lambda x: x.age, reverse=descending)


def linear_search_by_name(artifacts: list[Artifact], name: str) -> Artifact | None:
    for a in artifacts:
        if a.name == name:
            return a
    return None


def demo_museum_night() -> None:
    print("--- Moonlight Museum Demo ---")
    bst = ArtifactBST()
    # Add at least 8 artifacts
    data = [
        Artifact(101, "Jade Dragon", "Sculpture", 500, "East Wing"),
        Artifact(50, "Cursed Map", "Paper", 200, "Basement"),
        Artifact(150, "Golden Crown", "Jewelry", 1000, "Vault"),
        Artifact(75, "Stone Tablet", "Inscription", 3000, "Great Hall"),
        Artifact(125, "Iron Shield", "Weapon", 400, "Armory"),
        Artifact(25, "Silk Robe", "Textile", 150, "East Wing"),
        Artifact(175, "Obsidian Mirror", "Tool", 800, "Dark Room"),
        Artifact(60, "Silver Coin", "Currency", 1200, "Basement")
    ]
    for a in data:
        bst.insert(a)

    print(f"Sorted IDs (Inorder): {bst.inorder_ids()}")
    
    # Queue Demo
    rq = RestorationQueue()
    rq.add_request(RestorationRequest(50, "Clean moss off map"))
    print(f"Next Restoration: {rq.peek_next_request().description}")
    
    # Stack Demo
    stack = ArchiveUndoStack()
    stack.push_action("Moved Jade Dragon to East Wing")
    print(f"Undo action available: {stack.peek_last_action()}")
    
    # Linked List Demo
    route = ExhibitRoute()
    route.add_stop("Entrance")
    route.add_stop("East Wing")
    route.add_stop("Basement")
    print(f"Exhibit Route: {' -> '.join(route.list_stops())}")
    print("Demo completed successfully.")

if __name__ == "__main__":
    demo_museum_night()