# Project 2: Moonlight Museum After Dark

## Team information
- Team name: Midnight Coders
- Members: Shakti, Team Member 2
- Repository name: moonlight-museum-after-dark

---

## Project summary
Our project builds a system for organizing mysterious museum artifacts after dark.  
The system uses multiple data structures including a Binary Search Tree, Queue, Stack, and Linked List to manage artifacts, restoration requests, exhibit routes, and archive actions efficiently.

---

# Full Python Code

```python
from collections import deque


# ==========================================
# Artifact Class
# ==========================================

class Artifact:
    def __init__(self, artifact_id, name, category, room, age):
        self.artifact_id = artifact_id
        self.name = name
        self.category = category
        self.room = room
        self.age = age

    def __str__(self):
        return f"[{self.artifact_id}] {self.name} | {self.category} | Room {self.room} | Age: {self.age}"


# ==========================================
# BST Node
# ==========================================

class ArtifactNode:
    def __init__(self, artifact):
        self.artifact = artifact
        self.left = None
        self.right = None


# ==========================================
# Artifact BST
# ==========================================

class ArtifactBST:
    def __init__(self):
        self.root = None

    def insert(self, artifact):
        self.root = self._insert_recursive(self.root, artifact)

    def _insert_recursive(self, node, artifact):
        if node is None:
            return ArtifactNode(artifact)

        if artifact.artifact_id < node.artifact.artifact_id:
            node.left = self._insert_recursive(node.left, artifact)

        elif artifact.artifact_id > node.artifact.artifact_id:
            node.right = self._insert_recursive(node.right, artifact)

        else:
            print(f"Duplicate ID {artifact.artifact_id} ignored.")

        return node

    def search_by_id(self, artifact_id):
        return self._search_recursive(self.root, artifact_id)

    def _search_recursive(self, node, artifact_id):
        if node is None:
            return None

        if artifact_id == node.artifact.artifact_id:
            return node.artifact

        if artifact_id < node.artifact.artifact_id:
            return self._search_recursive(node.left, artifact_id)

        return self._search_recursive(node.right, artifact_id)

    def inorder_traversal(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.artifact)
            self._inorder(node.right, result)

    def preorder_traversal(self):
        result = []
        self._preorder(self.root, result)
        return result

    def _preorder(self, node, result):
        if node:
            result.append(node.artifact)
            self._preorder(node.left, result)
            self._preorder(node.right, result)

    def postorder_traversal(self):
        result = []
        self._postorder(self.root, result)
        return result

    def _postorder(self, node, result):
        if node:
            self._postorder(node.left, result)
            self._postorder(node.right, result)
            result.append(node.artifact)


# ==========================================
# Restoration Queue
# ==========================================

class RestorationQueue:
    def __init__(self):
        self.queue = deque()

    def add_request(self, request):
        self.queue.append(request)

    def process_next_request(self):
        if self.is_empty():
            return None
        return self.queue.popleft()

    def peek_next_request(self):
        if self.is_empty():
            return None
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


# ==========================================
# Archive Undo Stack
# ==========================================

class ArchiveUndoStack:
    def __init__(self):
        self.stack = []

    def push_action(self, action):
        self.stack.append(action)

    def undo_last_action(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def peek_last_action(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


# ==========================================
# Linked List for Exhibit Route
# ==========================================

class RouteNode:
    def __init__(self, stop_name):
        self.stop_name = stop_name
        self.next = None


class ExhibitRoute:
    def __init__(self):
        self.head = None

    def add_stop(self, stop_name):
        new_node = RouteNode(stop_name)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    def remove_stop(self, stop_name):
        if self.head is None:
            return False

        if self.head.stop_name == stop_name:
            self.head = self.head.next
            return True

        current = self.head

        while current.next:
            if current.next.stop_name == stop_name:
                current.next = current.next.next
                return True
            current = current.next

        return False

    def list_stops(self):
        stops = []
        current = self.head

        while current:
            stops.append(current.stop_name)
            current = current.next

        return stops

    def count_stops(self):
        count = 0
        current = self.head

        while current:
            count += 1
            current = current.next

        return count


# ==========================================
# Utility Functions
# ==========================================

def category_counts(artifacts):
    counts = {}

    for artifact in artifacts:
        counts[artifact.category] = counts.get(artifact.category, 0) + 1

    return counts


def unique_rooms(artifacts):
    return set(artifact.room for artifact in artifacts)


def sort_artifacts_by_age(artifacts):
    return sorted(artifacts, key=lambda a: a.age)


def linear_search_by_name(artifacts, name):
    for artifact in artifacts:
        if artifact.name.lower() == name.lower():
            return artifact
    return None


# ==========================================
# Demo Function
# ==========================================

def demo_museum_night():
    print("\n===== MOONLIGHT MUSEUM AFTER DARK =====\n")

    artifacts = [
        Artifact(50, "Ancient Mask", "Relic", "A1", 500),
        Artifact(20, "Golden Skull", "Treasure", "B2", 300),
        Artifact(70, "Phantom Painting", "Artwork", "C1", 150),
        Artifact(10, "Moon Clock", "Machine", "D4", 700),
        Artifact(30, "Crystal Orb", "Magic", "A2", 250),
        Artifact(60, "Dragon Statue", "Relic", "B1", 1000),
        Artifact(80, "Silver Sword", "Weapon", "E5", 450),
        Artifact(25, "Shadow Book", "Magic", "C3", 120)
    ]

    # BST
    bst = ArtifactBST()

    for artifact in artifacts:
        bst.insert(artifact)

    print("=== Inorder Traversal ===")
    for item in bst.inorder_traversal():
        print(item)

    print("\n=== Search Artifact ID 30 ===")
    print(bst.search_by_id(30))

    # Queue
    queue = RestorationQueue()

    queue.add_request("Repair Ancient Mask")
    queue.add_request("Clean Dragon Statue")

    print("\n=== Restoration Queue ===")
    print("Next Request:", queue.peek_next_request())
    print("Processing:", queue.process_next_request())

    # Stack
    stack = ArchiveUndoStack()

    stack.push_action("Archived Crystal Orb")
    stack.push_action("Moved Silver Sword")

    print("\n=== Undo Stack ===")
    print("Last Action:", stack.peek_last_action())
    print("Undo:", stack.undo_last_action())

    # Linked List
    route = ExhibitRoute()

    route.add_stop("Entrance Hall")
    route.add_stop("Mystic Room")
    route.add_stop("Ancient Vault")

    print("\n=== Exhibit Route ===")
    print(route.list_stops())

    # Reports
    print("\n=== Reports ===")
    print("Category Counts:", category_counts(artifacts))
    print("Unique Rooms:", unique_rooms(artifacts))

    print("\n=== Sorted By Age ===")
    for item in sort_artifacts_by_age(artifacts):
        print(item)

    print("\n=== Linear Search By Name ===")
    print(linear_search_by_name(artifacts, "Crystal Orb"))


if __name__ == "__main__":
    demo_museum_night()
```

---

## Feature checklist

### Core structures
- [x] `Artifact` class/record
- [x] `ArtifactBST`
- [x] `RestorationQueue`
- [x] `ArchiveUndoStack`
- [x] `ExhibitRoute` singly linked list

### BST features
- [x] insert artifact
- [x] search by ID
- [x] preorder traversal
- [x] inorder traversal
- [x] postorder traversal
- [x] duplicate IDs ignored

### Queue features
- [x] add request
- [x] process next request
- [x] peek next request
- [x] empty check
- [x] size

### Stack features
- [x] push action
- [x] undo last action
- [x] peek last action
- [x] empty check
- [x] size

### Linked list features
- [x] add stop to end
- [x] remove first matching stop
- [x] list stops in order
- [x] count stops

### Utility/report features
- [x] category counts
- [x] unique rooms
- [x] sort by age
- [x] linear search by name

### Integration
- [x] `demo_museum_night()`
- [x] at least 8 artifacts in demo
- [x] demo shows system parts working together

---

## Design note (150-250 words)

The project uses multiple data structures because each structure solves a different problem efficiently. A Binary Search Tree (BST) is used for artifact IDs because searching, inserting, and organizing IDs becomes faster compared to using a normal list. The BST also allows different traversals such as preorder, inorder, and postorder to display artifacts in different ways.

A queue is used for restoration requests because restoration tasks follow the First-In-First-Out (FIFO) principle. The oldest request should be processed first. A stack is used for archive actions because undo systems naturally follow the Last-In-First-Out (LIFO) rule where the most recent action is undone first.

The exhibit route uses a singly linked list because museum stops are connected in sequence, and linked lists are suitable for adding or removing stops dynamically without shifting large amounts of data. Utility functions are separated from the main classes to improve organization and readability. The system is divided into classes for each major structure, making the code modular, reusable, and easier to maintain. The demo function connects all components together and demonstrates how the entire museum system works during nighttime operations.

---

## Complexity reasoning

- `ArtifactBST.insert`: `O(h)` where `h` is the height of the BST because insertion follows one path down the tree.
- `ArtifactBST.search_by_id`: `O(h)` because the search only travels through one branch at a time.
- `ArtifactBST.inorder_ids`: `O(n)` because every node is visited once.
- `RestorationQueue.process_next_request`: `O(1)` because deque removal from the front is constant time.
- `ArchiveUndoStack.undo_last_action`: `O(1)` because popping from the end of a list is constant time.
- `ExhibitRoute.remove_stop`: `O(n)` because the linked list may need to traverse all nodes.
- `sort_artifacts_by_age`: `O(n log n)` because Python sorting uses Timsort.
- `linear_search_by_name`: `O(n)` because each artifact may need to be checked once.

---

## Edge-case checklist

### BST
- [x] insert into empty tree
- [x] search for missing ID
- [x] empty traversals
- [x] duplicate ID

### Queue
- [x] process empty queue
- [x] peek empty queue

### Stack
- [x] undo empty stack
- [x] peek empty stack

### Exhibit route linked list
- [x] empty route
- [x] remove missing stop
- [x] remove first stop
- [x] remove middle stop
- [x] remove last stop
- [x] one-stop route

### Reports
- [x] empty artifact list
- [x] repeated categories
- [x] repeated rooms
- [x] missing artifact name
- [x] same-age artifacts

---

## Demo plan / how to run

Run the following commands:

```bash
python museum_project.py
```

Or:

```bash
python -c "from museum_project import demo_museum_night; demo_museum_night()"
```

---

## Assistance & sources

- AI used? (Y/N): Y
- What it helped with:
  - Code structure
  - README formatting
  - Complexity explanations
  - Debugging ideas
- Non-course sources used:
  - Python official documentation
- Links:
  - https://docs.python.org/3/