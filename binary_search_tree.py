from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Iterable, Iterator, Optional, List


@dataclass
class BSTNode:
    value: Any
    left: Optional["BSTNode"] = None
    right: Optional["BSTNode"] = None


class BinarySearchTree:
    """
    Binary Search Tree with common operations:
    - insert
    - search / contains
    - delete
    - min / max
    - height
    - traversals: inorder, preorder, postorder, level order
    - kth smallest
    - predecessor / successor
    - is_valid_bst
    - clear
    - to_sorted_list / from_iterable

    Convention used here:
    - Duplicate values are ignored.
    - Smaller values go left, larger values go right.
    """

    def __init__(self, iterable: Optional[Iterable[Any]] = None) -> None:
        self.root: Optional[BSTNode] = None
        self._size: int = 0

        # "iterable" means anything you can loop over (list, tuple, range, generator, etc.).
        # If the caller passes one, we insert each value into the BST.
        if iterable is not None:
            self.extend(iterable)

    # -------------------------
    # Basic dunder helpers
    # -------------------------
    def __len__(self) -> int:
        return self._size

    def __contains__(self, value: Any) -> bool:
        return self.find(value) is not None

    def __iter__(self) -> Iterator[Any]:
        # Iterating over the tree yields values in sorted order (inorder traversal).
        yield from self._inorder_nodes(self.root)

    def __repr__(self) -> str:
        return f"BinarySearchTree({self.to_sorted_list()})"

    # -------------------------
    # Conversions / utilities
    # -------------------------
    def to_sorted_list(self) -> List[Any]:
        return list(iter(self))

    @classmethod
    def from_iterable(cls, it: Iterable[Any]) -> "BinarySearchTree":
        return cls(it)

    def is_empty(self) -> bool:
        return self._size == 0

    def clear(self) -> None:
        self.root = None
        self._size = 0

    def extend(self, iterable: Iterable[Any]) -> None:
        for x in iterable:
            self.insert(x)

    # -------------------------
    # Insert
    # -------------------------
    def insert(self, value: Any) -> bool:
        """
        Inserts value into the BST.
        Returns True if inserted, False if value already exists.
        """
        if self.root is None:
            self.root = BSTNode(value)
            self._size += 1
            return True

        cur = self.root
        while True:
            if value < cur.value:
                if cur.left is None:
                    cur.left = BSTNode(value)
                    self._size += 1
                    return True
                cur = cur.left
            elif value > cur.value:
                if cur.right is None:
                    cur.right = BSTNode(value)
                    self._size += 1
                    return True
                cur = cur.right
            else:
                return False  # duplicate ignored

    # -------------------------
    # Search
    # -------------------------
    def find(self, value: Any) -> Optional[BSTNode]:
        cur = self.root
        while cur is not None:
            if value < cur.value:
                cur = cur.left
            elif value > cur.value:
                cur = cur.right
            else:
                return cur
        return None

    # -------------------------
    # Min / Max
    # -------------------------
    def min_node(self, start: Optional[BSTNode] = None) -> Optional[BSTNode]:
        cur = self.root if start is None else start
        if cur is None:
            return None
        while cur.left is not None:
            cur = cur.left
        return cur

    def max_node(self, start: Optional[BSTNode] = None) -> Optional[BSTNode]:
        cur = self.root if start is None else start
        if cur is None:
            return None
        while cur.right is not None:
            cur = cur.right
        return cur

    def min_value(self) -> Any:
        node = self.min_node()
        if node is None:
            raise ValueError("BST is empty")
        return node.value

    def max_value(self) -> Any:
        node = self.max_node()
        if node is None:
            raise ValueError("BST is empty")
        return node.value

    # -------------------------
    # Delete
    # -------------------------
    def delete(self, value: Any) -> bool:
        """
        Deletes value from the BST.
        Returns True if deleted, False if not found.
        """
        self.root, deleted = self._delete(self.root, value)
        if deleted:
            self._size -= 1
        return deleted

    def _delete(self, node: Optional[BSTNode], value: Any) -> tuple[Optional[BSTNode], bool]:
        if node is None:
            return None, False

        if value < node.value:
            node.left, deleted = self._delete(node.left, value)
            return node, deleted

        if value > node.value:
            node.right, deleted = self._delete(node.right, value)
            return node, deleted

        # Case 1: no child
        if node.left is None and node.right is None:
            return None, True

        # Case 2: one child
        if node.left is None:
            return node.right, True
        if node.right is None:
            return node.left, True

        # Case 3: two children
        # Replace current node's value with inorder successor (smallest in right subtree),
        # then delete that successor node from the right subtree.
        successor = self.min_node(node.right)
        assert successor is not None
        node.value = successor.value
        node.right, _ = self._delete(node.right, successor.value)
        return node, True

    # -------------------------
    # Height / validation
    # -------------------------
    def height(self) -> int:
        """
        Returns height measured in number of edges.
        Empty tree = -1, single node tree = 0.
        """
        return self._height(self.root)

    def _height(self, node: Optional[BSTNode]) -> int:
        if node is None:
            return -1
        return 1 + max(self._height(node.left), self._height(node.right))

    def is_valid_bst(self) -> bool:
        def helper(node: Optional[BSTNode], low: Any, high: Any) -> bool:
            if node is None:
                return True
            if not (low < node.value < high):
                return False
            return helper(node.left, low, node.value) and helper(node.right, node.value, high)

        return helper(self.root, float("-inf"), float("inf"))

    # -------------------------
    # Traversals
    # -------------------------
    def _inorder_nodes(self, node: Optional[BSTNode]) -> Iterator[Any]:
        if node is not None:
            yield from self._inorder_nodes(node.left)
            yield node.value
            yield from self._inorder_nodes(node.right)

    def inorder(self) -> List[Any]:
        return list(self._inorder_nodes(self.root))

    def _preorder_nodes(self, node: Optional[BSTNode]) -> Iterator[Any]:
        if node is not None:
            yield node.value
            yield from self._preorder_nodes(node.left)
            yield from self._preorder_nodes(node.right)

    def preorder(self) -> List[Any]:
        return list(self._preorder_nodes(self.root))

    def _postorder_nodes(self, node: Optional[BSTNode]) -> Iterator[Any]:
        if node is not None:
            yield from self._postorder_nodes(node.left)
            yield from self._postorder_nodes(node.right)
            yield node.value

    def postorder(self) -> List[Any]:
        return list(self._postorder_nodes(self.root))

    def level_order(self) -> List[Any]:
        if self.root is None:
            return []

        out: List[Any] = []
        queue: List[BSTNode] = [self.root]
        front = 0

        # We use "front" instead of pop(0) so the queue stays efficient.
        while front < len(queue):
            node = queue[front]
            front += 1

            out.append(node.value)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

        return out

    # -------------------------
    # Order-statistics helpers
    # -------------------------
    def kth_smallest(self, k: int) -> Any:
        """
        1-based: k=1 returns the smallest value.
        """
        if k <= 0 or k > self._size:
            raise IndexError("k out of range")

        count = 0
        for value in self:
            count += 1
            if count == k:
                return value

        raise RuntimeError("unexpected state")

    def predecessor(self, value: Any) -> Optional[Any]:
        """
        Largest value strictly smaller than 'value'.
        """
        cur = self.root
        pred: Optional[Any] = None
        while cur is not None:
            if value <= cur.value:
                cur = cur.left
            else:
                pred = cur.value
                cur = cur.right
        return pred

    def successor(self, value: Any) -> Optional[Any]:
        """
        Smallest value strictly larger than 'value'.
        """
        cur = self.root
        succ: Optional[Any] = None
        while cur is not None:
            if value >= cur.value:
                cur = cur.right
            else:
                succ = cur.value
                cur = cur.left
        return succ


# -------------------------
# Example usage
# -------------------------
if __name__ == "__main__":
    bst = BinarySearchTree([8, 3, 10, 1, 6, 14, 4, 7, 13])

    print("tree:", bst)
    print("inorder:", bst.inorder())          # sorted order
    print("preorder:", bst.preorder())
    print("postorder:", bst.postorder())
    print("level order:", bst.level_order())

    print("contains 6:", 6 in bst)
    print("contains 99:", 99 in bst)
    print("min:", bst.min_value())
    print("max:", bst.max_value())
    print("height:", bst.height())
    print("3rd smallest:", bst.kth_smallest(3))
    print("pred(6):", bst.predecessor(6))
    print("succ(6):", bst.successor(6))

    print("delete 3:", bst.delete(3))
    print("after delete:", bst.inorder())
    print("valid BST:", bst.is_valid_bst())
